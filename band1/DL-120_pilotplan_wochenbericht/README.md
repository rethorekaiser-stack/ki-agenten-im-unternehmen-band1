# DL-120 Pilotplan, Korrekturliste mit Fehlerklassen, Wochenbericht

| | |
|---|---|
| Kennung | DL-120 |
| Version | 1.5 |
| Stand | 19.10.2026 |
| Kapitelbezug | 5.2 Pilotbetrieb; 11.1 Probezeit; Bausteine B-05.2 Probezeit im Betrieb, B-03.3 Kennzahlen im Laufbericht, B-08.2 (Zeile Probezeit) |
| Fundstellen im Buch | 5.2 (Anhang B.3) |

## Zweck
Die Probezeit eng führen: erst Abnahmetest (DL-110), dann ein Pilot mit festgelegter **Dauer, Nutzern, Umfang und Freigabe**. Jede Korrektur durch einen Menschen wird mit **Fehlerklasse** und Grund erfasst, einmal pro Woche legt der Agent einen **Wochenbericht** vor. Ertrag der Probezeit ist die Liste fehlender Regeln und die Grundlage für die Entscheidung über die Ausweitung (DL-121).

## Dateien
- `leervorlage_pilotplan.md` / `beispiel_ki_buchhalter_pilotplan.md` – Plan mit den vier Regeln, Voraussetzungen und Ende der Probezeit.
- `leervorlage_korrekturliste.csv` / `beispiel_ki_buchhalter_korrekturliste.csv` – eine Zeile je Korrektur, mit Fehlerklasse und Folge.
- `leervorlage_wochenbericht.md` / `beispiel_ki_buchhalter_wochenbericht.md` – Kennzahlen aus B-03.3, Abweichungen nach Fehlerklasse, Einschätzung des Buchhalters.

CSV: UTF-8 mit BOM, Semikolon.

## Fehlerklassen (Kapitel 5.2, B-05.2)
| Fehlerklasse | Beispiel | Folge |
|---|---|---|
| kritisch | Verstoß gegen eine feste Regel, zu niedrige Freigabestufe, erfundenes Konto | sofort melden, Rückstufung (jeder Vorschlag einzeln), Ursache klären |
| wesentlich | falsches Konto oder falscher Steuerschlüssel, falscher Betrag | in die Kennzahl Korrekturquote, Regel ergänzen |
| formal | Begründung unvollständig, Ausgabeformat nicht eingehalten | sammeln, Anweisung präzisieren |

## Anpassungshinweis
Dauer, Nutzerkreis und Umfang sind Festlegungen des Buches für den KI-Buchhalter. Die 500-€-Grenze bezieht sich auf den Rechnungsbetrag (brutto). Bewerten Sie Abweichungen nach der Tabelle, nicht nach Gefühl. Auf der Low-Code-Stufe wird die Probezeit eine feste Bedingung im Freigabeschritt, die Korrektur mit Fehlerklasse ein Feld im Freigabeformular und der Wochenbericht eine Auswertung des Protokolls.

## Änderungen in Version 1.1
- Titel nach Anhang B.3 (vorher: „Pilotplan und Wochenbericht“).

## Änderungen in Version 1.2
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.3
- Steuerberater legt Kontierung fest (Kapitel 5.2) (Spiegelung Manuskript 15:56 / Festlegung Buch-Autor 16:09).

## Änderungen in Version 1.4
- Freigabestufe in Wochenbericht und Korrekturliste (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.5
- Beispiel Wochenbericht: Bezug auf das Buch vereinheitlicht (Siebzehnter Auftrag, 19.10.2026 21:30).
