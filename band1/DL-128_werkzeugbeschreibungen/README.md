# DL-128 Vorlage Werkzeugbeschreibungen

| | |
|---|---|
| Kennung | DL-128 |
| Version | 1.4 |
| Stand | 19.10.2026 |
| Kapitelbezug | 14.5 Werkzeuge gut beschreiben; 14.1 Wie Agenten Werkzeuge nutzen; 14.6 Identität und Zugriffsrechte; 13.7 Werkzeuge des Servers; 17.4; Bausteine B-14.1, B-14.2, B-14.5 |
| Fundstellen im Buch | 14.5, 14.7, Anhang D5 (Anhang B.3) |

## Zweck
Das Modell kennt ein Werkzeug nur aus Name, Beschreibung und Angaben. Die Vorlage beschreibt jedes Werkzeug mit sechs Feldern: **Name, Zweck, Angaben, Rückgabe, Fehlerfälle, Rechte**, und prüft die fünf Regeln aus Kapitel 14.5: wenige, durchdachte Werkzeuge; sprechende Namen mit Bereich; Beschreibung wie für eine neue Kollegin; aussagekräftige Rückgaben; sparsam mit Umfang.

## Dateien
- `leervorlage.md` – Steckbrief je Werkzeug und Prüfliste der fünf Regeln.
- `beispiel_ki_buchhalter.md` – ausgefüllt für die Werkzeuge des KI-Buchhalters aus Kapitel 13.7 und 14.1.

## Anpassungshinweis
Werkzeugbeschreibungen sind Anweisungen: versioniert, geprüft und nach jeder Änderung getestet (Regressionstest nach B-17.4). Rechte richten sich nach der Zugriffsmatrix (DL-112) und dem Dienstkonto (Kapitel 14.6). Das Buch nennt fünf Werkzeuge mit Namen. Für weitere Zugänge, etwa Kontoumsätze und Buchungsstapel, nennt es keine Werkzeugnamen; dort stehen Platzhalter [aus Quelle offen]. Die DATEV-Übergabe beschreibt DL-113.

## Änderungen in Version 1.1
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.2
- Anzeigename „Muss-Wissen abrufen“ zum Werkzeug finanzen_muss_wissen_abrufen (Name unverändert) (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.3
- README: Bezug auf das Buch vereinheitlicht (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.4
- Beispiel (Version 1.1): Werkzeugname `vorschlag_uebergeben` statt `vorschlag_ablegen` wie im Buch, Kapitel 14.1 (Werkzeugliste Nr. 4, Abschnitt 4). Werkzeug für den Buchungsstapel bleibt Platzhalter, das Buch nennt in 14.1 und 14.7 keinen Namen (Dreiundzwanzigster Auftrag, 19.10.2026 22:10).
