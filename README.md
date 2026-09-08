# AI-Coding-Framework

Ein Baukasten für die Arbeit mit Claude Code: Skills, die von der Produktidee bis zur laufend korrigierten Projektkonfiguration ineinandergreifen.

Der Ausgangspunkt ist eine Beobachtung. Ein Agent, der bei jeder Sitzung bei null anfängt, ist ein teurer Praktikant. Er stellt dieselben Fragen, trifft dieselben Entscheidungen neu und macht denselben Fehler ein zweites Mal. Was fehlt, ist nicht ein besseres Modell, sondern eine Struktur, in der Wissen liegen bleibt und sich selbst korrigiert.

**Wie die Teile zusammenspielen, steht in [LOOP.md](LOOP.md).**

## Was drin ist

| Skill | Wozu |
|---|---|
| `prd` | Produkt spezifizieren. Führt vorher ein Interview, statt Absichten aufzuschreiben |
| `stack-decisions` | Technische Entscheidungen treffen und als Datensatz festhalten. Auch einzeln, wenn später etwas getauscht wird |
| `design-system` | Visuelle Richtung, Tokens im Code, Begründungen im Vault, Beispielseite zur Freigabe |
| `create-specs` | Das Produkt in Komponenten zerlegen und als verbundenen Spec-Graph anlegen |
| `write-spec` | Eine Komponente spezifizieren, gegen den Code verifiziert, mit Ripple- und Reverse-Abgleich |
| `grill-me` → `grilling` | Das Interview-Verfahren. Entscheidungsbaum in Runden, bis keine Verzweigung offen ist |
| `project-init` | Der Einstiegspunkt. Wissensbasis, PRD, Stack, Bereiche und die CLAUDE.md-Schichten eines Projekts aufbauen |
| `skill-creator` | Skills bauen, verbessern und ihre Trefferquote messen |

Dazu `hooks/session-state.py`: ein SessionStart-Hook, der `.claude/state.md` in jede Sitzung injiziert. Die Datei trägt oben den Loop-Stand und darunter die Übergabe der letzten Sitzung, weil die Planungsphase über viele Sitzungen läuft und keine davon Kontext von der vorigen erbt.

Der Kreislauf ist noch nicht geschlossen. Die Tabelle am Ende von [LOOP.md](LOOP.md) sagt, was fehlt.

## Voraussetzungen

- [Claude Code](https://claude.com/claude-code)
- Ein Obsidian-MCP-Server für die Wissensbasis. `project-init` führt durch die Einrichtung, falls noch keiner läuft
- Python 3 mit `pyyaml`, nur für die Prüf- und Messskripte von `skill-creator`

## Installation

Global, für alle Projekte:

```bash
git clone https://github.com/mxrius1706/Ai-Coding-Framework.git
cp -r Ai-Coding-Framework/skills/* ~/.claude/skills/
```

Oder projektlokal, dann nach `.claude/skills/` statt `~/.claude/skills/`.

Prüfen, ob es angekommen ist: in Claude Code `/project-init` tippen. Erscheint der Skill nicht, hilft ein Neustart der Sitzung.

## Loslegen

Im leeren Projektordner:

```
Neues Projekt aufsetzen
```

`project-init` übernimmt von dort: erst die Wissensbasis, dann das PRD, dann ein eigenes Interview über den Stack, dann ein Plan zur Freigabe. Geschrieben wird erst danach.

## Zwei Regeln, die alles zusammenhalten

**Eine Wahrheit, ein Ort.** Keine Aussage steht in zwei Dateien. Wo eine zweite sie braucht, verweist sie. Zwei Kopien einer Regel werden irgendwann uneins, und dann folgt die Arbeit der falschen.

**Bestand mit Ablaufdatum.** Was noch läuft, aber abgelöst wird, sagt das in seinem eigenen Dokument: was heute gilt, was es ersetzt und worauf nicht mehr aufgebaut werden darf.

## Herkunft

Der Baukasten enthält fremde Skills, teils angepasst. Quellen, Lizenzen und die vorgenommenen Änderungen stehen in [CREDITS.md](CREDITS.md).
