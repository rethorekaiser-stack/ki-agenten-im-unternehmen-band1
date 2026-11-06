# DL-131 Reifegrad- und Grenzen-Check

| | |
|---|---|
| Kennung | DL-131 |
| Version | 1.11 |
| Stand | 04.11.2026 |
| Autor | Charlie Moore |
| Kapitelbezug | 21.2 Reifegrad nach Aufgabentyp; 1.4 Grade der Eigenständigkeit (Abgrenzung); Bausteine B-03.1, B-03.3, B-16.3, B-21.2 und B-22.1 der Agentendatei Version 1.21 (DL-101) |
| Fundstellen im Buch | 21.2 (Anhang B.3) |

## Zweck
Ein Prüfbogen für das Betriebsprotokoll. Er legt je Vorgangsart (B-03.1) fest, ob sie „erprobt“ oder „in Erprobung“ ist, und hält die drei Kennzahlen fest, die die Einteilung tragen: Korrektur-, Rückfrage- und Ausnahmequote. Vorschläge aus Vorgangsarten in Erprobung legt der Agent immer einzeln vor, auch unter der ersten Wertgrenze; die Staffel gilt erst, wenn ein Mensch die Vorgangsart als erprobt einträgt (B-21.2). Über 10.000 € gilt weiter das Vieraugenprinzip. Der Reifegrad wird im Betriebsprotokoll geführt, nicht im Einrichtungsprotokoll und nicht im Einrichtungsgespräch (B-05.1). Jede Vorgangsart beginnt bei „in Erprobung“; erst ein Mensch trägt sie als „erprobt“ ein. Der Reifegrad ist nicht der Grad der Eigenständigkeit aus Kapitel 1.4: Der Grad legt je Handlung fest, was der Agent selbst tun darf (beim KI-Buchhalter höchstens Grad 4, fest in der Agentendatei, B-01.4); der Reifegrad gehört zur Vorgangsart und hält fest, wie verlässlich sie im eigenen Haus schon läuft. Beide Begriffe stehen am Anfang des Prüfbogens nebeneinander. Die Testfälle zu den Grenzen aus Kapitel 22 (Lücken 22.1, Teilauslesung 22.3, Einschleusung 22.4) stehen in DL-110.

## Dateien
- `leervorlage.md` – leerer Prüfbogen für einen beliebigen Agenten.
- `beispiel_ki_buchhalter.md` – ausgefüllt am KI-Buchhalter, mit dem Praxisbeispiel aus Kapitel 21.2.

## So gehen Sie vor
1. Je freigegebener Vorgangsart (B-03.1) den Reifegrad im Betriebsprotokoll eintragen. Jede Vorgangsart beginnt bei „in Erprobung“; eine Vorgangsart ohne Eintrag gilt als „in Erprobung“.
2. Schwelle für „erprobt“ festlegen und die Kennzahlen als eigene Werte eintragen: Korrektur- und Ausnahmequote je Vorgangsart aus dem Laufbericht (B-03.3), die Rückfragequote aus eigener Zählung (Ausnahmen mit Rückfrage nach B-22.1 („Angabe fehlt auf dem Beleg, Rückfrage.“ oder „Konto unklar, Rückfrage.“) geteilt durch die Zahl der Vorgänge).
3. Die Testfälle zu den Grenzen aus Kapitel 22 führen Sie in DL-110 (L-01 bis L-03, N-06, N-03 und N-07 bis N-09).
4. Jede Änderung des Reifegrads im Betriebsprotokoll festhalten, mit Datum und Namen. Den Reifegrad ändert nur ein Mensch. In das Einrichtungsprotokoll und in B-05.1 gehört er nicht.

## Anpassungshinweis
Die Schwelle für „erprobt“ legen Sie selbst fest ([EIGENER WERT]); das Buch nennt als Beispielwert drei Monate und eine Korrekturquote unter 5 % (Kapitel 21.2). Die Tabelle der Aufgabentypen ist eine redaktionelle Einschätzung mit Stand Oktober 2026, kein Messergebnis, und ersetzt nicht Ihren Abnahmetest. Für einen anderen Agenten ersetzen Sie die Vorgangsarten durch die Ihrer Stelle. [EIGENER WERT] markiert Werte, die Sie selbst aus Ihrem Betrieb eintragen; ein als „Beispielwert“ gekennzeichneter Wert dient nur zur Orientierung und ist keine Messung.

## Änderungen in Version 1.1
- Titel „Reifegrad- und Grenzen-Check“ mit Bindestrich.
- Kennzahlen je Vorgangsart (Korrektur-, Rückfrage-, Ausnahmequote): [EIGENER WERT] statt „aus Quelle offen“; ein Beispielwert (Korrekturquote 3 %, Standard-Eingangsrechnung Inland), als Beispielwert gekennzeichnet.
- Reifegrad im Betriebsprotokoll, nicht im Einrichtungsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“ (Entscheidung des Buch-Autors, 19.10.2026). Ergebniszeile: Eintrag im Betriebsprotokoll statt Übernahme in B-21.2.

## Änderungen in Version 1.2
- Teil A nach Kapitel 21.2 (Bereinigung 4): Tabelle wie im Betriebsprotokoll des Buches (Vorgangsart, drei Quoten, Zeitraum, Reifegrad, Start „in Erprobung“); Schwelle [EIGENER WERT] mit dem Beispielwert „drei Monate und Korrekturquote unter 5 %“; Beispielwert 3 % entfällt.
- Teil B: Testfall zu 22.3 ist N-06; Einschleusungsfälle heißen N-07 bis N-09.
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.3
- Stichprobe „etwa jeden zwanzigsten, ein anpassbarer Startwert“ nach Kapitel 22.1 statt Prüfmarke (Abgleich mit dem Manuskript, Stand 19.10.2026 11:17).

## Änderungen in Version 1.4
- Neuer Abschnitt „Begriffe“: Reifegrad (21.2, B-21.2) und Grad der Eigenständigkeit (1.4, B-01.4) getrennt definiert; Start „in Erprobung“ ohne „niedrigste Stufe“; Freigabestufe; Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.5
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Beispiel und README) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.6
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.7
- Nach Kapitel 21.2 und B-22.1: Korrektur- und Ausnahmequote aus dem Laufbericht (B-03.3), Rückfragequote selbst gezählt (Rückfrage-Ausnahmen nach B-22.1 geteilt durch die Zahl der Vorgänge) in Vorlagentext, Kennzahlenspalten und Ablauf; Beispiel mit den Vorgangsarten nach B-03.1 (Eingangsrechnungen und sonstige Kostenbelege, Ausgangsrechnungen, Anlagenzugänge), Praxisbeispiel nach 21.2, „auch bis 2.500 € (Freigabestufe 1)“; „Über 10.000 € gilt weiter das Vieraugenprinzip.“ in Beispiel, Leervorlage und README. Fundstelle 21.2 unverändert (Achtundzwanzigster Auftrag, Lektorat Runde 17, 19.10.2026 22:50).
- Nachtrag Runde 18: Nur noch Betriebsprotokoll je Vorgangsart nach 21.2; Korrektur- und Ausnahmequote je Vorgangsart aus dem Laufbericht (B-03.3). Entfernt: Teil B „Grenzen“ (Lückenfälle 22.1, Fehlerfortpflanzung 22.2, Kontext 22.3, Einschleusung 22.4, Plattform und Bindung 22.5) und die Umzugsfragen 22.5 in Beispiel und Leervorlage; Testfälle weiter in DL-110. Kapitelbezug (Bausteine B-03.1, B-03.3, B-21.2, B-22.1), Zweck und Ablauf angepasst (Achtundzwanzigster Auftrag, Nachtrag Lektorat Runde 18, 19.10.2026 22:55).

## Änderungen in Version 1.8
- Feld „Vorgangsart (B-03.1)“ im Protokolleintrag (B-16.3) als Grundlage der Quoten je Vorgangsart (Beispiel und Leervorlage), Kapitelbezug mit B-16.3; Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.9
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.10
- Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.11
- README und Beispiel: Version der Agentendatei 1.21. (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
