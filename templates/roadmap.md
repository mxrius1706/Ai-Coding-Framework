# Fahrplan

**Jetzt:** Aufbau, Schritt 1 · **Als Nächstes:** Wissensbasis einrichten und dieses Dokument in den Vault legen

Dieser Fahrplan beantwortet, wo das Projekt steht und was als Nächstes kommt. Er ist die einzige Datei, die das beantwortet. Wer einen Schritt abschließt, trägt ihn hier ein, bevor er weitergeht.

Zeichen: `⬜` offen · `🔄` läuft · `✅` fertig · `❌` bewusst entfallen

---

## Aufbau

Der Weg von der Idee bis zu vollständigen Spezifikationen. Jeder Schritt hat den Skill, der ihn ausführt.

| # | Schritt | Skill | Stand | Notiz |
|---|---|---|---|---|
| 1 | Wissensbasis | `project-init` Phase 0 | ⬜ | Vault einrichten, Struktur anlegen |
| 2 | Produktdefinition | `prd` | ⬜ | Interview zuerst, dann schreiben |
| 3 | Stack | `stack-decisions` | ⬜ | Getrennt vom Produktgespräch |
| 4 | Design-System | `design-system` | ⬜ | Entfällt ohne Oberfläche |
| 5 | Projektkonfiguration | `project-init` Phasen 3 bis 5 | ⬜ | Wurzel, Bereiche, Pfad-Regeln, Hooks |
| 6 | Komponentenkarte | `create-specs` | ⬜ | Grenzen werden gegrillt, nicht abgeleitet |
| 7 | Specs | `write-spec` | ⬜ | 0 von 0, eine Komponente je Aufruf |
| 8 | Seitenplanung | `plan-pages` | ⬜ | Je Oberfläche eine Übersicht, aus den Specs abgeleitet |
| 9 | UI-Specs | `write-ui-spec` | ⬜ | 0 von 0, je Seite eine, Mockup vor dem Dokument |
| 10 | Konsistenzprüfung | `spec-consistency` | ⬜ | Kein fester Takt, siehe Regel unten |

Schritte, die dieses Projekt nicht braucht, werden auf `❌` gesetzt und nicht als offen mitgeschleppt. Ein Projekt ohne Oberfläche hat kein Design-System und keine UI-Specs.

### Konsistenzläufe

**Letzter Lauf:** noch keiner · **Seitdem:** 0 Specs · **Offene Annahmebrüche:** 0

Kein fester Takt. Ein Lauf ist fällig, wenn einer dieser Fälle eintritt:

- Eine **Entscheidung wurde geändert**, die bestehende Specs zitieren. Sofort, gezielt über die zitierenden Specs.
- Eine Spec hat **bewusst eine Annahme gebrochen** und die Gegenseite ist noch nicht nachgezogen.
- Ein **Cluster ist fertig**, dessen Specs gegeneinander geschrieben wurden.
- **Vor der Seitenplanung und vor dem Ableiten der Bauphasen**, jeweils vollständig, weil beide die Specs als Ganzes lesen.
- **Als Netz:** fünf oder mehr Specs seit dem letzten Lauf, ohne dass einer der Fälle gefeuert hat.

Der Grund gegen einen festen Takt: Widersprüche entstehen durch **Ändern**, nicht durch Schreiben. Ein Lauf nach fünf Specs, in denen nichts umentschieden wurde, sucht eine Fehlerklasse, die es dort nicht gibt. Und ein Lauf, der erst fünf Specs nach einer geänderten Entscheidung kommt, findet den Fehler in sechs Dokumenten statt in einem.

---

## Bauphasen

Bleibt leer, bis die Specs stehen. Die Baureihenfolge wird **aus den fertigen Specs abgeleitet**, nicht vorher geplant: erst wenn die Komponenten beschrieben sind, ist zu sehen, was worauf aufbaut und was zuerst Wert liefert.

Das ist eine andere Frage als die Schreibreihenfolge aus Schritt 6. Schreibreihenfolge folgt den Verweisen, Baureihenfolge folgt dem Nutzen.

---

## Regeln für dieses Dokument

**Als Nächstes trägt eine Handlung, keinen Schrittnamen.** „Specs schreiben" sagt einer neuen Sitzung nichts. „Zuerst das Datenmodell, alles andere zeigt darauf" sagt, wo sie anfängt und warum. Die Begründung ist der Teil, der nach ein paar Tagen fehlt.

**Eintragen, was wahr ist, nicht was geplant war.** Ein halb gelaufener Schritt ist `🔄` mit Notiz, was fehlt, nie `✅`, weil es fast geklappt hat.

**Nichts zusammenfassen, was anderen gehört.** Der Spec-Index besitzt den Status je Spec, hier steht höchstens eine Zahl und ein Verweis. Beim Widerspruch gewinnt der Index.
