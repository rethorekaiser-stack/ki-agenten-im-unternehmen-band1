# DL-113 Leervorlage Verwaltungssatz (EXTF-Buchungsstapel)

Version 1.3 · Stand 04.11.2026 · Aufbau nach dem Beispiel in Kapitel 14.7, Platzhalter nach Baustein B-14.7 der Agentendatei Version 1.21 (DL-101)

Ersetzen Sie die Platzhalter in Großbuchstaben und eckigen Klammern. Feld 21 „Festschreibung“ bleibt immer 0. Trennzeichen ist das Semikolon, Beträge stehen mit Dezimalkomma. Zeile 1 ist der Verwaltungssatz, Zeile 2 enthält die Spaltenüberschriften, ab Zeile 3 folgen die Buchungen.

```
"EXTF";700;21;"Buchungsstapel";13;[ERZEUGT JJJJMMTTHHMMSS000];;"RE";"KI-Buchhalter";"";[BERATERNUMMER];[MANDANTENNUMMER];[WJ-BEGINN JJJJMMTT];[SACHKONTENLÄNGE];[DATUM VON JJJJMMTT];[DATUM BIS JJJJMMTT];"[BEZEICHNUNG DES STAPELS]";"KI";1;0;0;"EUR";;"";;;"[03/04]";;;"";"KI-Buchhalter [VERSION]"
Umsatz (ohne Soll/Haben-Kz);Soll/Haben-Kennzeichen;WKZ Umsatz;Kurs;Basis-Umsatz;WKZ Basis-Umsatz;Konto;Gegenkonto (ohne BU-Schlüssel);BU-Schlüssel;Belegdatum;Belegfeld 1;Belegfeld 2;Skonto;Buchungstext
[BETRAG];"[S/H]";"EUR";;;;[KONTO];[GEGENKONTO];"[BU-SCHLÜSSEL ODER LEER]";[BELEGDATUM TTMM];"[BELEGNUMMER]";"";;"[BUCHUNGSTEXT]"
```

## Felder des Verwaltungssatzes

| Feld | Inhalt | Woher |
|---|---|---|
| 1 bis 5 | Kennung „EXTF“, Formatangaben und „Buchungsstapel“ wie im Beispiel | Kapitel 14.7; Formatversion nach der aktuellen Formatbeschreibung von DATEV |
| 6 | Zeitpunkt der Erzeugung | setzt das Programm (DL-113 py) |
| 11 | [BERATERNUMMER] | Einrichtungsgespräch, Fragen 5 und 6 (B-14.7) |
| 12 | [MANDANTENNUMMER] | Einrichtungsgespräch, Fragen 5 und 6 (B-14.7) |
| 13 | [WJ-BEGINN JJJJMMTT], Beginn des Wirtschaftsjahres | Einrichtungsgespräch (B-14.7) |
| 14 | [SACHKONTENLÄNGE] | Einrichtungsgespräch (B-14.7) |
| 15 und 16 | Zeitraum des Stapels, Datum von und bis | Monat der Vorschlagsliste |
| 17 | Bezeichnung des Stapels | frei, etwa „Buchungsvorschlaege Oktober 2026“ |
| 21 | Festschreibung | **immer 0** (B-14.7) |
| 27 | Sachkontenrahmen [03/04] | Einrichtungsgespräch (B-14.7) |
| letztes Feld | „KI-Buchhalter [VERSION]“ mit der Version Ihrer Agentendatei | Kapitel 14.7 |

Die übrigen Felder bleiben wie im Beispiel. Ihre Bedeutung, die genauen Spaltenüberschriften und die Steuerschlüssel richten sich nach der aktuellen Formatbeschreibung und der Steuerschlüsseltabelle von DATEV in der jeweils gültigen Fassung.

## Buchungszeilen
- Betrag ohne Vorzeichen mit Dezimalkomma; die Richtung steht im Soll/Haben-Kennzeichen.
- Belegdatum als TTMM; das Jahr ergibt sich aus dem Verwaltungssatz.
- Bei Automatikkonten (AV/AM) bleibt das Feld BU-Schlüssel leer. Bei anderen Konten nur ein Steuerschlüssel, der im freigegebenen Wissen steht (B-14.7).
- Nur freigegebene bzw. freigabefreie Vorschläge kommen in den Stapel (B-08.2).
