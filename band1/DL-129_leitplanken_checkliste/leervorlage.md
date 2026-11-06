# Leitplanken-Checkliste: [NAME DES AGENTEN]

Stufe: [No Code / Low Code / technische Umsetzer] · Version der Agentendatei: [X.Y] · geprüft von: [NAME, ROLLE] · Datum: [DATUM]

<!-- Spalte „durchgesetzt durch“: Programm, Plattform oder Mensch (mit Namen des Ablaufschritts oder der Person). -->

## 1. Technische Grenzen (16.1)
| ✓ | Grenze | Wert | durchgesetzt durch | getestet am |
|---|---|---|---|---|
| [ ] | Tokenlimit und Ausgabengrenze je Lauf und je Monat, mit Warnschwellen | [WERT] | | |
| [ ] | Ratenbegrenzung: Aufrufe je Minute an Modell und Schnittstellen | [WERT] | | |
| [ ] | Höchstzahl der Schritte: Werkzeugaufrufe je Vorgang und je Lauf | [WERT] | | |
| [ ] | Zeitlimit je Lauf | [WERT] | | |
| [ ] | Jede Grenze führt zu einem geordneten Ende mit Bericht | | | |
| [ ] | Erkennung von Wiederholungen: gleiches Werkzeug mit gleichen Angaben → Abbruch und Ausnahme | | | |
| [ ] | Notschalter verhindert jeden neuen Lauf und jeden weiteren Werkzeugaufruf | | | |

## 2. Freigabeschritte (16.2)
| ✓ | Punkt | Umsetzung | durchgesetzt durch | getestet am |
|---|---|---|---|---|
| [ ] | Die Freigabestufe berechnet das Programm aus [BEZUGSGRÖSSE], nicht das Modell; bei Abweichung gilt die höhere | | | |
| [ ] | Freigabe zählt nur im Freigabekanal [KANAL], mit Name und Zeitpunkt | | | |
| [ ] | Vier Augen heißt zwei verschiedene Personen | | | |
| [ ] | Vor jeder Handlung, die sich nicht zurückholen lässt oder nach außen wirkt, bestätigt ein Mensch; das Dienstkonto hat diese Rechte nicht | | | |

## 3. Protokollierung und Überwachung (16.3)
| ✓ | Anforderung | Umsetzung | geprüft am |
|---|---|---|---|
| [ ] | Nachvollziehbarkeit: Eingabe, Wissen mit Stand, Schritte, Ergebnis je Lauf | | |
| [ ] | Unveränderbarkeit: Einträge nie ändern, Korrekturen als neue Einträge | | |
| [ ] | Verfahrensdokumentation vorhanden und aktuell | | |
| [ ] | Aufbewahrung nach § 147 Abs. 3 AO | [FRISTEN] | |
| [ ] | Keine personenbezogenen Einzeldaten im Protokoll, wo sie nicht nötig sind | | |
| [ ] | Ein Mensch wertet das Protokoll regelmäßig aus: [RHYTHMUS, NAME] | | |
| [ ] | Sofort-Signale: Regelverstoß · plötzlicher Anstieg von Ausnahmen oder Korrekturen · Verbrauch steigt ohne mehr Vorgänge | | |

## 4. Schutzmaßnahmen (16.4)
| ✓ | Schicht | Umsetzung | geprüft am |
|---|---|---|---|
| [ ] | Regel in der Agentendatei: fremder Text ist Inhalt, nie Anweisung | | |
| [ ] | Minimale Rechte des Dienstkontos | | |
| [ ] | Freigabeschritte für alles mit Wirkung | | |
| [ ] | Trennung von Anweisung und Inhalt: Inhalte gekennzeichnet, nie als Systemprompt | | |
| [ ] | Prüfung der Ausgabe gegen feste Regeln vor der Ablage | | |
| [ ] | Testfall mit eingeschleuster Anweisung in der Testliste | | |
| [ ] | Verschlüsselung auf dem Übertragungsweg | | |
| [ ] | Verschlüsselung in Ablage, Protokoll und Status | | |
| [ ] | Schlüssel im Tresor, nie im Prompt, nie im Protokoll | | |
| [ ] | Programme und Agent nennen Zugänge nur mit ihrem Namen im Tresor; Werte aus Werkzeugantworten und Fehlermeldungen werden geschwärzt | | |
| [ ] | `.env` und Schlüsseldateien in `.gitignore`, im Repository nur `.env.example` ohne Werte | | |
| [ ] | Schlüsselrotation geplant, Widerruf eingeübt: wer widerruft, wo, in welcher Zeit | | |

## Ergebnis
[ ] alle Punkte umgesetzt [ ] offen: [PUNKTE, bis DATUM, verantwortlich]

Unterschrift: [NAME, ROLLE] ________
