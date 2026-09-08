"""SessionStart hook: legt Fahrplan und letzte Uebergabe in jede neue Sitzung.

Zwei Dateien, zwei Fragen:

- Der **Fahrplan** sagt, wo das Projekt steht und was als Naechstes kommt.
  Er liegt in der Wissensbasis ausserhalb des Repos, deshalb muss sein Pfad
  hier konfiguriert werden (siehe ROADMAP_PATH unten).
- Die **Uebergabe** in `.claude/state.md` sagt, was letzte Sitzung lief.

Beide werden injiziert statt nur erwaehnt. Eine Anweisung, eine Datei zu
lesen, ist eine Bitte; injizierter Inhalt liegt einfach da. Genau deshalb
gibt es diesen Hook ueberhaupt.

Konfiguration des Fahrplan-Pfads, erste Fundstelle gewinnt:

1. Umgebungsvariable `PROJECT_ROADMAP`
2. Die Datei `.claude/roadmap-path` im Projekt, eine Zeile mit dem Pfad
3. `roadmap.md` im Projekt (Fallback, falls die Wissensbasis im Repo liegt)

`project-init` schreibt Variante 2, weil es den Vault-Pfad ohnehin kennt.
Fehlt der Pfad, wird nur die Uebergabe injiziert, statt zu scheitern.

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

MAX_ROADMAP_CHARS = 8000
MAX_HANDOFF_CHARS = 6000


def read(path, limit):
    """Datei lesen, gekuerzt. Gibt None zurueck, wenn es sie nicht gibt."""
    if not path or not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            content = handle.read().strip()
    except OSError:
        return None
    if not content:
        return None
    if len(content) > limit:
        content = content[:limit] + f"\n\n[gekuerzt, vollstaendig in {path}]"
    return content


def roadmap_path(project_dir):
    from_env = os.environ.get("PROJECT_ROADMAP")
    if from_env:
        return from_env

    pointer = os.path.join(project_dir, ".claude", "roadmap-path")
    if os.path.exists(pointer):
        try:
            with open(pointer, "r", encoding="utf-8") as handle:
                configured = handle.read().strip()
            if configured:
                return os.path.expanduser(configured)
        except OSError:
            pass

    return os.path.join(project_dir, "roadmap.md")


def main() -> None:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", ".")

    roadmap = read(roadmap_path(project_dir), MAX_ROADMAP_CHARS)
    handoff = read(os.path.join(project_dir, ".claude", "state.md"), MAX_HANDOFF_CHARS)

    if not roadmap and not handoff:
        return

    parts = []
    if roadmap:
        parts.append("FAHRPLAN (wo steht das Projekt, was kommt als Naechstes)\n" + roadmap)
    if handoff:
        parts.append("LETZTE SITZUNG (aus .claude/state.md)\n" + handoff)

    if roadmap:
        parts.append(
            "Beginne die Sitzung damit, wo wir stehen und was als Naechstes ansteht, "
            "und biete diesen Schritt an, statt auf eine Frage zu warten. Wer einen "
            "Schritt abschliesst, traegt ihn im Fahrplan ein, bevor es weitergeht."
        )
    else:
        parts.append(
            "Kein Fahrplan gefunden. Falls das Projekt einen hat, liegt sein Pfad "
            "nicht in .claude/roadmap-path; sonst ist er noch nicht angelegt."
        )

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "\n\n".join(parts),
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001 - ein Hook darf nie die Sitzung kippen
        sys.exit(0)
