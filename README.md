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
| `plan-pages` | Welche Seiten es gibt und wie man zwischen ihnen navigiert, aus den Specs abgeleitet |
| `write-ui-spec` | Eine Seite spezifizieren, Mockup vor dem Dokument, am Bild iteriert |
| `spec-consistency` | Den Spec-Graph auf Widersprüche prüfen. Auslöser statt Takt, reiner Bericht |
| `plan-build` | Aus den fertigen Specs die Bauphasen mit Gates ableiten und in den Fahrplan schreiben |
| `planning` | Plan je Bauphase, im Planungsmodus geschrieben, vor dem Branch, mit Out of Scope |
| `execute-plan` | Den freigegebenen Plan abarbeiten, frischer Subagent je Task, zwei Reviews dazwischen |
| `testing` | Testdisziplin. Zuerst der fehlschlagende Test, Verify Red ist Pflicht |
| `review-changes` | Gate am Phasenende. Drei Linsen parallel, Gate-Abgleich, reiner Bericht |
| `session-recap` | Handoff am Sitzungsende, prüft dabei den Fahrplan auf Drift |
| `grill-me` → `grilling` | Das Interview-Verfahren. Entscheidungsbaum in Runden, bis keine Verzweigung offen ist |
| `project-init` | Der Einstiegspunkt. Wissensbasis, PRD, Stack, Bereiche und die Anweisungsebenen eines Projekts aufbauen |
| `skill-creator` | Skills bauen, verbessern und ihre Trefferquote messen |

Zwei Dateien tragen über Sitzungsgrenzen. Der **Fahrplan** `roadmap.md` in der Wissensbasis beantwortet, wo das Projekt steht und was als Nächstes kommt; er wird gleich zu Beginn aus `templates/roadmap.md` kopiert, bereits mit dem Ablauf ausgefüllt, und wächst später um die Bauphasen, die `plan-build` aus den fertigen Specs ableitet. Ab dann ist er zu groß für jede Sitzung, deshalb injiziert der Hook nur noch den Kopf und den Abschnitt, auf den die Zeile `Aktuelle Bauphase` zeigt. `.claude/state.md` im Repo trägt die Übergabe der letzten Sitzung. Dazu zwei Hooks in `hooks/`: `session-state.py` injiziert Fahrplan und Übergabe bei Sitzungsstart und lässt die Sitzung mit dem nächsten Schritt eröffnen, `session-recap-trigger.py` erzwingt sie bei Abschiedsformeln.

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
