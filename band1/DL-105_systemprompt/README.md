# DL-105 Vorlage Systemprompt

| | |
|---|---|
| Kennung | DL-105 |
| Version | 1.11 |
| Stand | 04.11.2026 |
| Kapitelbezug | 13.3 Der Systemprompt; 13.4; 9.1 bis 9.3; 12.1 Spiegeltabelle; 14.6 |
| Fundstellen im Buch | 13.3 (Anhang B.3) |

## Zweck
Der Systemprompt ist die Anweisung, die der Agent vor jeder Aufgabe liest. Er beantwortet nach Kapitel 13.3 sechs Fragen in fester Reihenfolge: **Rolle, Ziel, Regeln, Wissen und Arbeitsbeginn, Ausgabeformat, Beispiele**. Darüber steht die Direktive (DL-104); der Auftrag des einzelnen Laufs kommt als Startprompt (DL-106). Vier Grundsätze: klar statt höflich, jede Regel einmal, Beispiele zeigen das Format, Gleichbleibendes zuerst.

## Dateien
- `leervorlage.md` – die sechs Teile zum Ausfüllen, mit Prüfliste nach 13.3 und 13.4.
- `beispiel_ki_buchhalter.md` – Systemprompt des KI-Buchhalters in Kurzform; Wortlaut der Regeln in der Agentendatei DL-101.

## Anpassungshinweis
Beim KI-Buchhalter ist die vollständige Agentendatei (DL-101) der Systemprompt. Das Beispiel zeigt die Struktur und übernimmt Rolle und Ausgabeformat wörtlich; die Regeln stehen als Verweis, damit es keine zwei abweichenden Fassungen gibt.

## Änderungen in Version 1.3
- Grundlage Agentendatei Version 1.8 mit 92 Bausteinen; Regel-Tabelle um B-21.2, B-22.x, B-23.x, B-24.x und B-25.x ergänzt.
- Hinweis nach Kapitel 24.3: Datum und Lauf-Nummer in den Auftrag, nicht in den Systemprompt.

## Änderungen in Version 1.4
- Regel-Tabelle, Zeile Reifegrad und Grenzen: Reifegrad im Betriebsprotokoll, nicht im Einrichtungsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“ (Entscheidung des Buch-Autors, 19.10.2026).

## Änderungen in Version 1.5
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.6
- Ausgabeformat „Freigabestufe“ statt „Wertgrenzen-Stufe“ (B-13.3); Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.7
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.8
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.9
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.10
- Ausgabeformat (B-13.3): „A′ Ist“ mit Strich U+2032 wie Agentendatei 1.19; Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.11
- Beispiel Zeile 3: Vollständiger Wortlaut nach Agentendatei DL-101 Version 1.21 (vorher noch 1.19). (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
