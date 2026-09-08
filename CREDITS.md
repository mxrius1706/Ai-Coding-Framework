# Herkunft der übernommenen Skills

Der Baukasten enthält fremde Skills, teils unverändert, teils angepasst. Diese Datei hält fest, was woher kommt und was daran geändert wurde.

| Skill | Quelle | Lizenz | Zustand |
|---|---|---|---|
| `skill-creator` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official), `plugins/skill-creator` | Apache 2.0 (`skills/skill-creator/LICENSE.txt`) | unverändert |
| `prd` | [github/awesome-copilot](https://github.com/github/awesome-copilot), `skills/prd` | siehe Quelle | **angepasst** |
| `grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills), `skills/productivity/grill-me` | siehe Quelle | **angepasst** |
| `grilling` | mit `grill-me` ausgeliefert, nicht separat in der Lock-Datei geführt | siehe Quelle | unverändert |
| `claude-statusbar` | [leeguooooo/claude-code-usage-bar](https://github.com/leeguooooo/claude-code-usage-bar), Paket `claude-statusbar` 3.42.0 | MIT | unverändert |

## Vorgenommene Anpassungen

**`prd`** - Phase 1 hieß im Original „Discovery (The Interview)" und stellte ein paar Standardfragen. Sie heißt jetzt „Discovery (Grill the Idea)" und ruft verbindlich den `grill-me`-Skill auf. Begründung im Skill selbst: ein PRD aus oberflächlichen Antworten wird zu „aspirational fiction". Zusätzlich darf der Nutzer das Interview abkürzen, offene Punkte werden dann als `TBD` markiert statt erfunden.

**`grill-me`** - `disable-model-invocation` von `true` auf `false` gesetzt. Ohne diese Änderung kann `prd` den Skill nicht selbst aufrufen und die Kopplung oben läuft ins Leere.

**`claude-statusbar`** - unverändert übernommen. Der Skill steuert das externe Werkzeug `cs`, das nicht Teil dieses Repos ist und über `cs --setup` installiert wird. `project-init` bietet das in Phase 0 an, wenn drei Bedingungen zusammenkommen: Arbeit im Terminal, noch keine `statusLine` konfiguriert, und Zustimmung des Nutzers. Es ist eine Einstellung je Rechner, nicht je Projekt, deshalb wird bei bereits gesetzter `statusLine` stillschweigend übersprungen statt erneut gefragt.

## Aufrufkette

```
prd  ->  grill-me  ->  grilling
```

`grill-me` ist nur ein Shim von sieben Zeilen. Die eigentliche Methode steht in `grilling`: ein Entscheidungsbaum, der in Runden abgearbeitet wird. Pro Runde werden alle Fragen gestellt, deren Voraussetzungen geklärt sind, jeweils mit einer Empfehlung. Fakten beschafft der Agent selbst, Entscheidungen trifft der Nutzer.
