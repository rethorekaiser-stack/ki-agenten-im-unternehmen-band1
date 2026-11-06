# Stellenprofil KI-Buchhalter – Kurzform und Verweis

Das vollständig ausgefüllte Stellenprofil des KI-Buchhalters steht in **DL-103** (`band1/DL-103_stellenprofil/beispiel_ki_buchhalter.md`). Es wird nur dort gepflegt, damit es keine zwei abweichenden Fassungen gibt.

Kurzform aus Kapitel 4.3 (Festlegungen des Buches; Ihr Unternehmen setzt eigene ein):

| Block | Inhalt am KI-Buchhalter | Bausteine | Kapitel |
|---|---|---|---|
| 1 Stelle | Rolle, sieben Aufgaben, Ziel „Richtigkeit vor Geschwindigkeit“, Kennzahlen; Einsatzbereich Deutschland, Industrie, Groß- und Einzelhandel, SKR 03, SKR 04 oder IKR; sieben Vorgangsarten | B-06.2, B-06.3, B-06.2-E, B-03.1, B-03.3 | 3, 6 |
| 2 Einordnung | Vorgesetzter, Bericht je Lauf, Eskalation an Buchhalter und Vertretung | B-07.4, B-16.3 | 7 |
| 3 Befugnisse und Pflichten | Rechte und Verbote, Wertgrenzen nach Rechnungsbetrag (brutto) mit Probezeit 500 €, Zugriffsmatrix, Außenauftritt, Lohnbuchungen | B-08.1 bis B-08.5 | 8 |
| 4 Anweisungen | Direktive, Stellenbeschreibung als Agentendatei, Startprompt mit Wissensabruf zum Belegdatum | B-09.4, B-13.3 | 9, 13 |
| 5 Budget | Kostenstelle, monatliches Budget in Euro, Tokenlimit und Warnschwellen | Platzhalter, technisch in Kapitel 16.1 | 10 |
| 6 Lebenszyklus | Probezeit vier Wochen, Ausweitungskriterien, Änderungsprotokoll, Abschaltung | B-05.2, B-05.3, B-05.4, B-11.3 | 5, 11 |

Entscheidung „ein Agent oder mehrere“ am KI-Buchhalter (Kapitel 4.2):

| Frage | Am KI-Buchhalter in Band 1 |
|---|---|
| Anweisungen ohne Widersprüche in einer Datei? | ja, eine Agentendatei |
| Werkzeuge klar unterschieden? | ja, wenige Werkzeuge: Beleg lesen, Wissen abrufen, Vorschlag übergeben |
| Getrennte Rechte für Teilaufgaben nötig? | nein, alle Vorgangsarten nutzen dasselbe Muss-Wissen Finanzen |
| Zweiter Agent als unabhängige Prüfung? | später möglich, als Prüfschleife (Kapitel 19.5) |
| **Entscheidung** | **ein einzelner Agent** (B-04.2). Die Verbund-Ergänzungen zu B-04.2 und B-15.1 ruhen, solange in B-18.1 kein Verbund eingetragen ist; einen Verbund planen Sie mit DL-123 (Kapitel 18.1). |
