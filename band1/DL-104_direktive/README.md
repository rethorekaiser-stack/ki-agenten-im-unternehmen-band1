# DL-104 Vorlage Direktive

| | |
|---|---|
| Kennung | DL-104 |
| Version | 1.10 |
| Stand | 04.11.2026 |
| Kapitelbezug | 9.1 Die Direktive; 9.2 Rangfolge der Ebenen; 9.3 Startprompt; 13.3 Systemprompt; 13.7 Unternehmensserver; Bausteine B-09.1, B-09.2 |
| Fundstellen im Buch | 4.1, 9.1, Anhang D5 (Anhang B.3) |

## Zweck
Die Direktive ist die oberste der drei Anweisungsebenen. Sie gilt für **alle** Agenten des Unternehmens. Darunter stehen die Agentendatei (Stellenbeschreibung, nur dieser Agent, DL-101/DL-105) und der Startprompt (nur dieser Lauf, DL-106). Rangfolge nach B-09.2: Direktive vor Agentendatei vor Startprompt. Eine untere Ebene darf eine obere eingrenzen, nie erweitern oder aufheben.

Die Vorlage enthält die sechs Grundsätze aus Kapitel 9.1 und eine Liste möglicher absoluter Verbote. In die Direktive gehören nur Verbote, die für alle Agenten gelten, etwa „keine Zahlungen auslösen“ oder „keine Verträge abschließen“. Was nur einen Agenten betrifft, etwa „nie festschreiben“ beim KI-Buchhalter, gehört in seine Stellenbeschreibung.

## Dateien
- `leervorlage.md` – Direktive zum Ausfüllen: Geltung und Rang, sechs Grundsätze, absolute Verbote, Erlass und Ablage, Versionsvermerk.
- `beispiel_ki_buchhalter.md` – Direktive eines Unternehmens, das den KI-Buchhalter einsetzt, mit Verweis auf die Bausteine, die sie im KI-Buchhalter umsetzen.

## Anpassungshinweis
Die Direktive erlässt die Geschäftsleitung, abgestimmt mit Datenschutz, IT und, wo vorhanden, dem Betriebsrat (Kapitel 9.1). Sie wird versioniert und liegt im Unternehmenswissen, beim KI-Buchhalter auf dem Unternehmensserver (Kapitel 13.7). Jeder Agent ruft sie zu Laufbeginn ab und nennt ihre Version im Protokoll (B-09.1). Ist sie nicht abrufbar, macht der Agent keinen Vorschlag. Gibt es noch keine Direktive, tragen Sie in der Agentendatei „keine“ ein.

Die Liste möglicher absoluter Verbote ist eine Auswahl. Kapitel 9.1 nennt ausdrücklich nur „keine Zahlungen auslösen“ und „keine Verträge abschließen“; die übrigen sind aus den Bausteinen der Agentendatei verallgemeinert (Quelle jeweils in Klammern). Streichen Sie, was nicht für alle Agenten gilt. Kein Rechtsrat.

Änderung gegenüber Version 1.0: Direktive aus Kapitel 9.1 ausformuliert (sechs Grundsätze, Erlass, Ablage, Abruf).

## Änderungen in Version 1.2
- Version der Agentendatei 1.8. Geprüft nach Kapitel 24.3: Die Direktive enthält kein Datum und keine Lauf-Nummer.

## Änderungen in Version 1.3
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.4
- Verweis auf Agentendatei Version 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
- Beispiel: „E-Mail“ statt „Mail“ (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 1.5
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.6
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.7
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.8
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.9
- Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.10
- Beispiel: Bezug auf die Agentendatei auf Version 1.21 gehoben (DL-101, freigegeben am 04.11.2026 um 20:02 MEZ). (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
