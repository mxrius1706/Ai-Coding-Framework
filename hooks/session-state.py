"""SessionStart hook: injiziert den Projektstand in jede neue Sitzung.

Liest `.claude/state.md` im Projekt und gibt sie als zusaetzlichen Kontext
zurueck. Die Datei traegt oben den Loop-Stand (wo stehen wir im Ablauf) und
darunter die Uebergabe der letzten Sitzung.

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
