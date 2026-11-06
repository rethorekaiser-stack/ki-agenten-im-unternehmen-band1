# DL-122 Pflegekalender und Versionsübersicht

| | |
|---|---|
| Kennung | DL-122 |
| Version | 1.14 |
| Stand | 05.11.2026 |
| Kapitelbezug | 5.4 Pflege im laufenden Betrieb; Baustein B-05.4 Pflege und Jahreswechsel; 11.2, 11.3; 17.4 Regressionstests |
| Fundstellen im Buch | 5.4 (Anhang B.3) |

## Zweck
Ein Agent, der heute richtig bucht, kann es nächstes Jahr falsch tun, ohne dass jemand etwas an ihm geändert hat: Steuersätze, Wertgrenzen, Kontenrahmen, Status des Unternehmens und das Modell der Plattform ändern sich. Der Pflegekalender legt fest, was **monatlich, vierteljährlich, jährlich und bei Anlass** zu tun ist und wer es tut. Die **Versionsübersicht** hält fest, mit welchen Fassungen von Agentendatei, Einrichtungsprotokoll und Muss-Wissen gearbeitet wird. Grundsatz: Der Agent meldet, der Mensch ändert, nach jeder Änderung wird neu getestet.

## Dateien
- `leervorlage_pflegekalender.csv` / `beispiel_ki_buchhalter_pflegekalender.csv` – Termine und Anlässe.
- `leervorlage_versionsuebersicht.csv` / `beispiel_ki_buchhalter_versionsuebersicht.csv` – Versionen mit Gültigkeit und Freigabe.

Format: UTF-8 mit BOM, Semikolon.

## Anpassungshinweis
Die Stichprobe von 20 Vorschlägen im Monat ist eine Empfehlung des Buches [Empfehlung des Buches] (Startwert, anpassbar). Anlässe gibt es mehr, als man denkt: Ein Statuswechsel (z. B. Kleinunternehmer wird regelbesteuert) ist ein neues Einrichtungsprotokoll; ein Modellwechsel der Plattform ist ein Grund für den Abnahmetest, auch wenn an der Agentendatei kein Wort geändert wurde.

## Änderungen in Version 1.1
- Titel nach Anhang B.3 (vorher: „Pflegekalender“).
- Pflegekalender: Abkündigungen (22.5), Reifegrad (21.2), Zielzeiten (24.1). Versionsübersicht: Zeile Agentendatei 1.8.

## Änderungen in Version 1.2
- Pflegekalender, Zeile Reifegrad: Eintrag im Betriebsprotokoll durch einen Menschen. Reifegrad im Betriebsprotokoll, nicht im Einrichtungsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“ (Entscheidung des Buch-Autors, 19.10.2026).

## Änderungen in Version 1.3
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.4
- Stichprobe von 20 Vorschlägen im Monat als „Startwert, anpassbar“ gekennzeichnet (Pflegekalender und README) (Entscheidungen Thore 19.10.2026, 11:06).

## Änderungen in Version 1.5
- GWG-Grenze: „im Entwurf zum Jahressteuergesetz 2026, Stand 19.10.2026“ nach Kapitel 13.7 statt Prüfmarke (Abgleich mit dem Manuskript, Stand 19.10.2026 11:17).

## Änderungen in Version 1.6
- Buchhalter mit Steuerberater; neue Fassung durch den Steuerberater (Kapitel 5.4) (Spiegelung Manuskript 15:56 / Festlegung Buch-Autor 16:09).

## Änderungen in Version 1.7
- Versionsübersicht: Zeile Agentendatei 1.10 ergänzt (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
- Zeile Agentendatei 1.10: Lektorat Runden 1 und 4, „E-Mail“ einheitlich, B-17.2 Fall 5 mit Anhang D2.4 (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 1.8
- Versionsübersicht: Zeilen Agentendatei 1.11 und 1.12 nach Teil 9 der Agentendatei Version 1.12 (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.9
- Versionsübersicht: Zeilen Agentendatei 1.13 und 1.14 nach Teil 9 der Agentendatei Version 1.14 (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.10
- Versionsübersicht: Zeilen Agentendatei 1.15 bis 1.18 nach Teil 9 der Agentendatei Version 1.18 (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.11
- Versionsübersicht: Zeile Agentendatei 1.19 ergänzt, die Übersicht führt damit die Zeilen 1.15 bis 1.19 nach Teil 9 der Agentendatei Version 1.19 (Semikolons im Text als Punkt, weil Semikolons in der CSV Trenner sind) (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.12
- Versionsübersicht: Zeile Agentendatei 1.20 ergänzt, die Übersicht führt damit die Zeilen 1.15 bis 1.20 nach Teil 9 der Agentendatei Version 1.20 (Semikolons im Text als Punkt) (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.13
- Versionsübersicht: Zeile Agentendatei 1.21 nach Teil 9 der Agentendatei ergänzt (Semikolons im Text als Punkt). (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)

## Änderungen in Version 1.14
- Pflegekalender: GWG-Zeile mit [PRÜFEN bis Drucklegung: JStG 2026, 2./3. Lesung 13.11.2026] (B03). (Einundvierzigster Auftrag, Lektorat Runde 32, 05.11.2026)
