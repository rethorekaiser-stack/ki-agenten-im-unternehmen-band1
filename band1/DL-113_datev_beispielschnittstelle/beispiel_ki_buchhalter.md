# DL-113 Beispiel KI-Buchhalter: EXTF-Buchungsstapel aus den Musterfällen 1 und 2

Version 1.4 · Stand 04.11.2026 · Bezug: Agentendatei Version 1.21 (DL-101), Baustein B-14.7 · Wortlaut aus Kapitel 14.7 des Buchs

Ein Buchungsstapel hat drei Teile: Zeile 1 ist der Verwaltungssatz, Zeile 2 enthält die Spaltenüberschriften, ab Zeile 3 folgen die Buchungen. Trennzeichen ist das Semikolon, Beträge stehen mit Dezimalkomma. Das Beispiel zeigt den Wareneinkauf mit Skonto (Musterfall 1) und den Warenverkauf (Musterfall 2) aus Kapitel 17.2 im SKR 03, gekürzt auf die ersten Spalten.

```
"EXTF";700;21;"Buchungsstapel";13;20261031120000000;;"RE";"KI-Buchhalter";"";1001;10001;20260101;4;20261001;20261031;"Buchungsvorschlaege Oktober 2026";"KI";1;0;0;"EUR";;"";;;"03";;;"";"KI-Buchhalter [VERSION]"
Umsatz (ohne Soll/Haben-Kz);Soll/Haben-Kennzeichen;WKZ Umsatz;Kurs;Basis-Umsatz;WKZ Basis-Umsatz;Konto;Gegenkonto (ohne BU-Schlüssel);BU-Schlüssel;Belegdatum;Belegfeld 1;Belegfeld 2;Skonto;Buchungstext
5950,00;"S";"EUR";;;;3400;1600;"";0610;"ER-2026-0815";"";;"Wareneingang Handelsware"
119,00;"S";"EUR";;;;1600;3736;"";1410;"ER-2026-0815";"";;"Skonto 2 % ER-2026-0815"
29750,00;"S";"EUR";;;;1400;8400;"";1510;"AR-2026-047";"";;"Lieferung Baumarkt"
```

Im Verwaltungssatz stehen Beraternummer (1001) und Mandantennummer (10001) als Beispielwerte, dazu Beginn des Wirtschaftsjahres, Sachkontenlänge 4, der Zeitraum und der Sachkontenrahmen 03. Das Feld 21 „Festschreibung“ ist 0. Im letzten Feld steht die Version Ihrer Agentendatei. Die Konten 3400, 3736 und 8400 sind Automatikkonten; die Steuer entsteht ohne Steuerschlüssel, das Feld bleibt leer. In der Praxis bucht man gegen Personenkonten der Lieferanten und Kunden statt gegen die Sammelkonten; für das Beispiel reicht die Sachkonten-Fassung. Die Zahlung aus Musterfall 1 und der Zahlungseingang aus Musterfall 2 fehlen in der gekürzten Fassung. Formatversion, genaue Spaltenüberschriften und die Behandlung des Skontos richten sich nach der aktuellen Formatbeschreibung von DATEV. Das Beispiel zeigt den Aufbau; es ist keine geprüfte Importdatei.

## Versionsstand
Im letzten Feld des Verwaltungssatzes steht die Version Ihrer Agentendatei. Für die Muster-Agentendatei (DL-101) ist das Version 1.21. Den Platzhalter [VERSION] ersetzen Sie durch Ihre Version.

Das Programm `datev_schnittstelle_beispiel.py` erzeugt aus den Musterfällen genau diese Zeilen. Nur Feld 6, der Zeitpunkt der Erzeugung, ist der Zeitpunkt des Laufs; der Selbsttest setzt ihn fest auf 31.10.2026, 12:00 Uhr.

Das Beispiel enthält Platzhalter; vor dem Einsatz passen Sie es an die aktuelle Formatbeschreibung von DATEV an.
