# DL-103 Stellenprofil KI-Buchhalter, ausgefülltes Beispiel

| | |
|---|---|
| Kennung | DL-103 (geht aus der früheren Kennung DL-001 hervor) |
| Version | 1.21 |
| Stand | 05.11.2026 |
| Kapitelbezug | 3.3 Erfolg messbar machen (Kennzahlen des Stellenprofils); 4.1 Rolle, Ziel und Grenzen; 4.3 Das Stellenprofil des Agenten; 5.2–5.4; 6.3 Ziele und Kennzahlen; 6.4 Einsatzzeiten; 7.1 Vorgesetzter, Berichtsweg und Intervall; 9.1 Die Direktive; 10.4 Budget, Kostenstelle und Tokenlimit; Blöcke aus Kapitel 6 bis 11; 25.1 Vorlagen und Stellenprofile; 25.3 Das Skelett als Kopiervorlage |
| Fundstellen im Buch | 3.3, 4.3, 6.3, 6.4, 7.1, 9.1, 10.4, 25.1, 25.3 (Anhang B.3) |

## Zweck
Das ausgefüllte Stellenprofil des KI-Buchhalters, der Bauplan für alle drei Stufen (No Code, Low Code, technische Umsetzer). Sechs Blöcke, einer je Kapitel von Teil III:

| Block | Kapitel | Inhalt | Bausteine |
|---|---|---|---|
| 1 Stelle | 3, 6 | Rolle, sieben Aufgaben, Ziel, Kennzahlen, Einsatzbereich, sieben Vorgangsarten | B-06.2, B-06.3, B-06.2-E, B-03.1, B-03.3 |
| 2 Einordnung | 7 | Vorgesetzter, Bericht je Lauf, Eskalation und Vertretung; ein Agent, Rangfolge | B-07.4, B-16.3, B-04.1–B-04.3 |
| 3 Befugnisse und Pflichten | 8 | Rechte und Verbote, Wertgrenzen nach Rechnungsbetrag (brutto) mit Probezeit 500 €, Zugriffsmatrix, Außenauftritt, Lohnbuchungen | B-08.1 bis B-08.5 |
| 4 Anweisungen | 9, 13 | Direktive, Stellenbeschreibung als Agentendatei, Startprompt mit Wissensabruf zum Belegdatum | B-09.4, B-13.3 |
| 5 Budget | 10 | Kostenstelle, Budget in Euro, Tokenlimit und Warnschwellen | Platzhalter, technisch 16.1 |
| 6 Lebenszyklus | 5, 11 | Probezeit vier Wochen, Ausweitung, Pflege, Änderungsprotokoll, Abschaltung | B-05.2, B-05.3, B-05.4, B-11.3 |

Jede Festlegung braucht ein technisches Gegenstück: siehe Spiegeltabelle DL-108.

## Dateien
- `beispiel_ki_buchhalter.md` – ausgefüllt am KI-Buchhalter, abgeleitet aus der Agentendatei Version 1.21 (DL-101) und den Kapiteln 3, 4, 5, 8, 21, 23 und 24; mit „Entwurf auf einer Seite“ (Kapitel 4.1).
- `leervorlage.md` – nur noch ein Verweis. **Die einzige leere Stellenprofil-Vorlage mit Ausfüllhilfe ist DL-119.**

## Anpassungshinweis
Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele. Werte wie Wertgrenzen, Summengrenze, Probezeit oder Ausweitungskriterien sind Festlegungen bzw. Empfehlungen des Buches, keine gesetzlichen Vorgaben. Ihr Unternehmen setzt eigene Werte ein. Felder mit „[aus Quelle offen]“ sind im Buch nicht festgelegt. [EIGENER WERT] markiert Werte, die Sie selbst aus Ihrem Betrieb eintragen, etwa das Monatsbudget.
## Herkunft
Diese Datei ist die umbenannte frühere Datei `vorlagen/DL-001_stellenprofil_ki_buchhalter.md` (Umbenennung 19.10.2026). Ursprünglicher Inhalt, unverändert erhalten:

```# DL-001: Stellenprofil KI-Buchhalter
(Siehe vorlagen/stellenprofil_ki_buchhalter.md)
```

## Änderungen in Version 1.2
- Wertgrenzen mit „bis einschließlich“ nach B-08.2 (Agentendatei 1.6); der Grenzbetrag gehört immer zur unteren Stufe.
- Zeile „Ein Agent oder mehrere“: Verbund-Ergänzungen zu B-04.2 und B-15.1 ruhen, solange in B-18.1 kein Verbund eingetragen ist (Verbundplan DL-123).

## Änderungen in Version 1.3
- Titel nach Anhang B.3 (vorher: „Stellenprofil KI-Buchhalter (ausgefülltes Beispiel)“).
- Grundlage Agentendatei Version 1.8.
- Block 1: Zeilen „Reifegrad je Vorgangsart“ (B-21.2, DL-131) und „Laufzeit“ (B-24.1, DL-133).
- Block 3: Zeilen „Personenbezogene Daten“ (B-23.1), „Ausgeschlossene Einsatzzwecke“ (B-23.2), „Keine Steuerberatung“ (B-23.5).
- Block 5: Tokenlimit (Kapitel 10.4) und Beispielergebnis der Rechenvorlage (Kapitel 10.7) eingetragen.

## Änderungen in Version 1.4
- Block 1, Reifegrad je Vorgangsart: Reifegrad im Betriebsprotokoll, nicht im Einrichtungsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“ (Entscheidung des Buch-Autors, 19.10.2026).
- Block 5, Budget je Monat: [EIGENER WERT] statt „aus Quelle offen“, Kostenstelle Finanzen (10.4); Erklärung der Markierung im Anpassungshinweis.

## Änderungen in Version 1.5
- ROI und TCO nach Kapitel 10.7 neu (Netto-Nutzen 1.185 €, erstes Jahr 10.020 €, Kosten je Beleg rund 7,08 €, Variante 540 € und rund 7,8 Monate). Budget je Monat: [EIGENER WERT] € mit Beispielwert 120 € aus Kapitel 10.4.
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.6
- Block 3: Summengrenze über 7 Kalendertage festgelegt, Prüfmarke zum Zeitraum entfernt (Entscheidungen Thore 19.10.2026, 11:06).
- Kennzahlen: unter 2 Minuten je Beleg und unter 1 % Fehlerquote als „Beispiel, eigenen Wert festlegen“ gekennzeichnet.
- Ausweitung und Pflege: Richtwerte 200 und 20 Vorschläge als „Startwert, anpassbar“ gekennzeichnet.
- Geprüft, unverändert: Tokenlimit 25 Millionen Token im Monat (wie DL-109), Lohnbuchungen immer Einzelfreigabe mindestens Stufe 2, Grenzbetrag bei der unteren Stufe.

## Änderungen in Version 1.7
- Anpassungshinweis: Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ (Umentscheidung Lizenz 11:21).

## Änderungen in Version 1.8
- Aufbewahrung der Laufprotokolle: Prüfmarke durch den Leserhinweis „Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrer steuerlichen Beratung ab.“ ersetzt.

## Änderungen in Version 1.9
- Zuordnungstabelle des Steuerberaters statt der Kanzlei (Spiegelung Manuskript 15:56 / Festlegung Buch-Autor 16:09).

## Änderungen in Version 1.10
- Kapitelbezug und Fundstellen um 3.3 ergänzt (Anhang B.3); Freigabestufe; Änderungsprotokoll (B-11.3); Leserhinweis mit Ihrem Steuerberater; Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
- Fundstellen und Kapitelbezug nach Anhang B.3: 3.3, 4.3, 6.3, 6.4, 7.1, 9.1, 10.4, 25.1, 25.3. Beispiel: Kennzahlen mit Beispielwerten aus 6.3 (unter 2 Minuten je Standardbeleg, unter 1 %, jeweils „Beispiel, eigenen Wert festlegen“), Einsatzzeiten werktags 08:00 bis 18:00 Uhr (6.4), Vorgesetzter „Leiter Rechnungswesen / CFO“ (7.1), vier Grundsätze der Direktive (9.1) (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 1.11
- README: Formulierung „im Buch nicht festgelegt“ (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.12
- Block 3, Keine Steuerberatung: Platzhalter [NAME STEUERBERATER] passend zur Agentendatei v1.12 (Achtzehnter Auftrag, 19.10.2026 21:38).

## Änderungen in Version 1.13
- Block 3, Keine Steuerberatung: [NAME STEUERBERATER] aus dem Einrichtungsgespräch, Frage 5 (Neunzehnter Auftrag, Agentendatei v1.12, 19.10.2026 21:40).
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Beispiel Zeile 5, README Zeile 26) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.14
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.15
- Beispiel, Zeile Reifegrad je Vorgangsart: „über 10.000 € gilt weiter das Vieraugenprinzip“ (Kapitel 21.2) (Achtundzwanzigster Auftrag, Lektorat Runde 17, 19.10.2026 22:50).

## Änderungen in Version 1.16
- Beispiel, Zeile Reifegrad je Vorgangsart: Vorgangsarten nach B-03.1 mit denselben Bezeichnungen wie in DL-131 („Eingangsrechnungen und sonstige Kostenbelege erprobt, Anlagenzugänge und Ausgangsrechnungen in Erprobung“, Praxisbeispiel 21.2) statt „Standard-Eingangsrechnung Inland … Leistungen aus dem Ausland“ (Dreißigster Auftrag, 19.10.2026 22:55).
- Vollständige Fassung: Blocknamen nach Kapitel 4.3 „Stelle, Einordnung, Befugnisse und Pflichten, Anweisungen, Budget, Lebenszyklus“ in Beispiel und README (vorher „Die Stelle“, „Einordnung in die Organisation“, „Anweisungen auf drei Ebenen“, „Budget und Beschaffung“); Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.17
- Kapitelbezug um 25.3 ergänzt; Fundstellen 3.3, 4.3, 6.3, 6.4, 7.1, 9.1, 10.4, 25.1, 25.3 wie Anhang B.3 (unverändert); Blocknamen geprüft (Dreiunddreißigster Auftrag, Lektorat Runde 23, 19.10.2026 23:07).

## Änderungen in Version 1.18
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.19
- Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.20
- README und Beispiel: Bezug auf die Agentendatei auf Version 1.21 gehoben (DL-101, freigegeben am 04.11.2026 um 20:02 MEZ). (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)

## Änderungen in Version 1.21
- Beispiel: Stand 04.11.2026 (N86). (Neununddreißigster Auftrag, Lektorat Runde 30, 05.11.2026)
