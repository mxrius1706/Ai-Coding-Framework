# Herkunft der übernommenen Skills

Der Baukasten enthält fremde Skills, teils unverändert, teils angepasst. Diese Datei hält fest, was woher kommt und was daran geändert wurde.

Sieben der 21 Skills stammen von anderen und stehen unten in der Tabelle. Die übrigen vierzehn sind Eigenarbeit.

Acht davon sind unmittelbar für diesen Baukasten entstanden: `create-specs`, `design-system`, `plan-pages`, `project-init`, `session-recap`, `stack-decisions`, `plan-build`, `planning`. Die anderen sechs sind aus Skills des Referenzprojekts hervorgegangen, die dort selbst geschrieben wurden: `write-ui-spec`, `spec-consistency`, `execute-plan`, `review-changes`, `testing`, `config-sync`. Das ist vom Autor bestätigt, nicht daraus geschlossen, dass ein Herkunftsvermerk fehlt - bei `write-spec` stand einer da, und der gehört deshalb in die Tabelle.

| Skill | Quelle | Lizenz | Beleg | Zustand |
|---|---|---|---|---|
| `skill-creator` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official), `plugins/skill-creator`; bezogen über einen Marketplace-Spiegel | Apache 2.0 | `skills/skill-creator/LICENSE.txt` liegt bei, Aufbau deckt sich mit der offiziellen Fassung | unverändert |
| `prd` | [github/awesome-copilot](https://github.com/github/awesome-copilot) | MIT | Repo-Lizenz und `license: MIT` im Frontmatter des Skills | **angepasst** |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills), `skills/productivity/grill-me` | MIT | Repo-Lizenz | **angepasst** |
| `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills), mit `grill-me` ausgeliefert | MIT | Repo-Lizenz | unverändert |
| `claude-statusbar` | [leeguooooo/claude-code-usage-bar](https://github.com/leeguooooo/claude-code-usage-bar) | MIT | Metadaten des Pakets `claude_statusbar` 3.42.0 | unverändert |
| `write-spec` | mittelbar [github/awesome-copilot](https://github.com/github/awesome-copilot), `create-specification` | MIT | Herkunftsvermerk in der Vorlage, aus der dieser Skill entstand | **zweistufig angepasst** |
| `thermo-nuclear-code-quality-review` | [cursor/plugins](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md), `cursor-team-kit` | MIT | Repo-Lizenz, dort als Werk von Cursor ausgewiesen | unverändert |

## Vorgenommene Anpassungen

**`prd`** - Phase 1 hieß im Original „Discovery (The Interview)" und stellte ein paar Standardfragen. Sie heißt jetzt „Discovery (Grill the Idea)" und ruft verbindlich den `grill-me`-Skill auf. Begründung im Skill selbst: ein PRD aus oberflächlichen Antworten wird zu „aspirational fiction". Zusätzlich darf der Nutzer das Interview abkürzen, offene Punkte werden dann als `TBD` markiert statt erfunden.

**`grill-me`** - `disable-model-invocation` von `true` auf `false` gesetzt. Ohne diese Änderung kann `prd` den Skill nicht selbst aufrufen und die Kopplung oben läuft ins Leere.

**`write-spec`** - nicht direkt übernommen, sondern aus einer Vorlage entstanden, die sich selbst als Fork von `create-specification` aus `github/awesome-copilot` (MIT) ausweist. Das Original erzeugt leere Template-Specs in einem `spec/`-Ordner. Über zwei Stufen sind daraus geworden: Ablage im Spec-Graph der Wissensbasis statt im Repo, eine erzwungene Ist-Stand-Analyse gegen den echten Code vor jedem Dokument, Redundanz-Sweep, sowie Ripple-Prüfung vorwärts und Reverse-Abgleich über die eingehenden Links. Der Vermerk stand nur in der Zwischenstufe und fehlte hier zunächst - genau die Art Verweis, die beim Ableiten still verloren geht.

**`thermo-nuclear-code-quality-review`** - unverändert übernommen aus dem `cursor-team-kit` in [cursor/plugins](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md), MIT, dort als Werk von Cursor ausgewiesen. Der Skill kursiert zusätzlich in weiteren öffentlichen Repos; maßgeblich für diesen Baukasten ist die genannte Quelle, weil sie der tatsächliche Bezugsweg ist.

Als einziger Bau-Skill wurde er **nicht** umgeschrieben. Bei allen anderen ist die Fassung hier eigen formuliert; hier nicht, weil genau diese Fassung im Referenzprojekt bereits als Gate läuft und erprobt ist. Der Preis dafür ist eine Einschränkung, die bekannt sein sollte: Ein Teil ihrer Beispiele ist auf TypeScript gemünzt (`any`, `unknown`, Casts). Die Regeln dahinter gelten sprachunabhängig, die Formulierung ist es nicht.

**`claude-statusbar`** - unverändert übernommen. Der Skill steuert das externe Werkzeug `cs`, das nicht Teil dieses Repos ist und über `cs --setup` installiert wird. `project-init` bietet das in Phase 0 an, wenn drei Bedingungen zusammenkommen: Arbeit im Terminal, noch keine `statusLine` konfiguriert, und Zustimmung des Nutzers. Es ist eine Einstellung je Rechner, nicht je Projekt, deshalb wird bei bereits gesetzter `statusLine` stillschweigend übersprungen statt erneut gefragt.

## Aufrufkette

```
prd  ->  grill-me  ->  grilling
```

`grill-me` ist nur ein Shim von sieben Zeilen. Die eigentliche Methode steht in `grilling`: ein Entscheidungsbaum, der in Runden abgearbeitet wird. Pro Runde werden alle Fragen gestellt, deren Voraussetzungen geklärt sind, jeweils mit einer Empfehlung. Fakten beschafft der Agent selbst, Entscheidungen trifft der Nutzer.
