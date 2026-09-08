"""SessionStart hook: injiziert die Uebergabe der letzten Sitzung.

Liest `.claude/state.md` und gibt sie als zusaetzlichen Kontext zurueck,
zusammen mit dem Hinweis, den Fahrplan zu lesen. Der Fahrplan liegt in der
Wissensbasis ausserhalb des Repos und ist die Quelle fuer "wo stehen wir";
diese Datei sagt nur, was letzte Sitzung passiert ist.

Registrierung in `.claude/settings.json`:

    "hooks": {
      "SessionStart": [
        { "hooks": [ {
            "type": "command",
            "command": "python3 \\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-state.py\\" || true",
            "shell": "bash"
        } ] }
      ]
    }

Das `|| true` ist Absicht: ein Fehler hier darf keine Sitzung blockieren.
"""

import json
import os
import sys

MAX_CHARS = 12000


def main() -> None:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", ".")
    path = os.path.join(project_dir, ".claude", "state.md")

    if not os.path.exists(path):
        return

    try:
        with open(path, "r", encoding="utf-8") as handle:
            content = handle.read().strip()
    except OSError:
        return

    if not content:
        return

    # Der Handoff waechst; der Loop-Stand steht oben und darf nie wegfallen.
    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n\n[gekuerzt, vollstaendig in .claude/state.md]"

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "PROJEKTSTAND (aus .claude/state.md)\n"
                f"{content}\n"
                "Kontext fuer diese Sitzung. Nur erwaehnen, wenn relevant. "
                "Der Loop-Stand oben wird von den Framework-Skills gepflegt, "
                "die Uebergabe darunter am Sitzungsende geschrieben."
            ),
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001 - ein Hook darf nie die Sitzung kippen
        sys.exit(0)
