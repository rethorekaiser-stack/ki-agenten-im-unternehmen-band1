# DL-119 Stellenprofil-Vorlage (leer) mit Ausfüllhilfe

| | |
|---|---|
| Kennung | DL-119 |
| Version | 1.10 |
| Stand | 19.10.2026 |
| Kapitelbezug | 4.1 Rolle, Ziel und Grenzen; 4.2 Ein Agent oder mehrere; 4.3 Das Stellenprofil des Agenten; Blöcke aus Kapitel 5 bis 11; 25.1 Vorlagen und Stellenprofile; 25.3 Das Skelett als Kopiervorlage |
| Fundstellen im Buch | 4.3, 25.1, 25.3 (Anhang B.3) |

## Zweck
Die **einzige leere Stellenprofil-Vorlage** des Repositorys. Das Stellenprofil hält den Entwurf eines Agenten auf Papier fest, damit Geschäftsführung, Fachbereich, Datenschutz und gegebenenfalls Betriebsrat über dasselbe Dokument sprechen. Es ist der Bauplan für jede Stufe: Aus ihm entstehen die Agentendatei (No Code), das Pflichtenheft für den Ablauf (Low Code) oder das technische Gegenstück je Block (technische Umsetzer).

## Dateien
- `leervorlage.md` – Entwurf auf einer Seite plus sechs Blöcke zum Ausfüllen.
- `beispiel_ki_buchhalter.md` – Verweis auf das ausgefüllte Beispiel in DL-103 und die Kurzform der sechs Blöcke aus Kapitel 4.3.

## Ausfüllhilfe (aus Kapitel 4)
1. **Erst drei Listen, dann Text.** Was tut der Agent? Was tut er nie? Wann übergibt er an einen Menschen? Die Listen kommen vor jedem Satz für den Agenten.
2. **Rolle in einem Satz.** Wer der Agent im Unternehmen ist, nicht was er technisch kann. Beispiel: „Assistent des menschlichen Buchhalters, bereitet Buchungen vor und entscheidet nichts mit Wirkung.“
3. **Ziel als Ergebnis.** Ein überprüfbarer Zustand, keine Tätigkeit. Beispiel: „Jeder Beleg ist zum Monatsende als prüfbarer Vorschlag mit Begründung erfasst.“
4. **Grenzen nach Art trennen** und jeweils festhalten, wer sie setzt:

   | Art der Grenze | Beispiel am KI-Buchhalter | Wer sie setzt |
   |---|---|---|
   | rechtlich | nie festschreiben, keine Voranmeldung übermitteln, nicht für Dritte buchen | Geschäftsleitung mit Steuerberater |
   | wirtschaftlich | Wertgrenzen-Staffel nach Rechnungsbetrag (brutto), Probezeit 500 € | Geschäftsleitung, Kompetenzordnung |
   | organisatorisch | nur freigegebene Vorgangsarten, kein Zugriff auf Lohndaten Einzelner, nach außen nur Entwürfe | Fachbereich, Datenschutz |

5. **Verbote mit Beispiel**, damit klar ist, was gemeint ist. **Übergabe an eine benannte Person oder Rolle**, nicht an eine Abteilung.
6. **Ein Agent oder mehrere** (Kapitel 4.2): Lassen sich die Anweisungen ohne Widerspruch in einer Datei pflegen? Unterscheiden sich die Werkzeuge klar? Brauchen Teilaufgaben getrennte Rechte? Soll ein zweiter Agent unabhängig prüfen? Die ersten beiden „Ja“ sprechen für einen Agenten, die letzten beiden für mehrere. Beginnen Sie mit einem.
7. **Fest oder abgefragt.** Fest ist, was für jedes Unternehmen gleich gilt, das diesen Agenten einsetzt (Wertgrenzen-Staffel, Verbote, Protokollpflicht, Vorgangsarten). Abgefragt wird im Einrichtungsgespräch, was vom Unternehmen abhängt (Status, Versteuerungsart, Kontenrahmen, Namen der Freigebenden, Probezeit ja/nein; DL-107). Markieren Sie jedes Feld.
8. **Wer füllt aus:** Fachleitung und Sachbearbeitung gemeinsam (am KI-Buchhalter: Leitung Rechnungswesen und Buchhalter); Datenschutz und IT prüfen Block 3 und 5; die steuerlichen Festlegungen gelten vorbehaltlich der Prüfung durch Ihren Steuerberater; der Vorgesetzte des Agenten gibt frei.
9. **Versionieren:** Jede Änderung bekommt eine neue Versionsnummer. Die Version des Stellenprofils steht in der Agentendatei (Platzhalter [VERSION STELLENPROFIL], B-04.3); bei Widerspruch gilt die strengere Regel.
10. **Eigene Kompetenzordnung übernehmen.** Weicht Ihre Freigaberegel für Menschen ab (etwa netto statt brutto), rechnen Sie sie auf die Bezugsgröße des Agenten um, statt die Buchwerte ungeprüft zu übernehmen (Praxisbeispiel 4.3).

Hilfsmittel für einzelne Blöcke: Eignungscheck DL-116 und Ablaufzerlegung DL-117 (vor Block 1), Kennzahlenblatt DL-118 (Block 1), Zugriffsmatrix DL-112 (Block 3), Direktive DL-104, Systemprompt DL-105, Startprompt DL-106 (Block 4), Rechenvorlage DL-109 (Block 5), Pilotplan DL-120, Checkliste Ausweitung DL-121, Pflegekalender DL-122 (Block 6), Spiegeltabelle DL-108 (technisches Gegenstück je Block).

## Anpassungshinweis
Die Vorlage ist ein Gerüst. Streichen oder ergänzen Sie Felder für Ihre Stelle, aber lassen Sie keinen Block leer: Ein leerer Block ist eine nicht getroffene Entscheidung.

## Änderungen in Version 1.1
- Beispiel, Entscheidung „ein einzelner Agent“: Verbund-Ergänzungen zu B-04.2 und B-15.1 ruhen, solange in B-18.1 kein Verbund eingetragen ist; Verweis auf den Verbundplan DL-123 (Kapitel 18.1).

## Änderungen in Version 1.2
- Titel nach Anhang B.3 (vorher: „Stellenprofil-Vorlage (sechs Blöcke, mit Ausfüllhilfe)“).

## Änderungen in Version 1.3
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.4
- Leervorlage Block 5: Hinweis auf das Buchbeispiel 25 Millionen Token im Monat (Kapitel 10.4, DL-109) ergänzt (Entscheidungen Thore 19.10.2026, 11:06).

## Änderungen in Version 1.5
- Kopfzeile der Leervorlage und Schritt 8 der Anleitung: „Prüfung durch Ihren Steuerberater“ statt Abnahme durch die Steuerkanzlei (Festlegung Thore 11:42).

## Änderungen in Version 1.6
- Wertgrenzen-Staffel mit Freigabestufe (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.7
- README: „Geschäftsleitung mit Steuerberater“ (Person) (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.8
- Beispiel, Entscheidung: Tippfehler „ruht“ → „ruhen“. Verweis „Kapitel 18.1“ geprüft, stimmt (Wann ein Agent nicht reicht) (Lektorat Runde 15, Kapitel 19, 19.10.2026 22:25).

## Änderungen in Version 1.9
- Leervorlage: Blocknamen nach Kapitel 4.3 „Stelle, Einordnung, Befugnisse und Pflichten, Anweisungen, Budget, Lebenszyklus“ (vorher „Die Stelle“, „Einordnung in die Organisation“, „Anweisungen auf drei Ebenen“, „Budget und Beschaffung“); Kurzform im Beispiel war schon gleich (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.10
- Kapitelbezug um 25.1 und 25.3 ergänzt; Fundstellen 4.3, 25.1, 25.3 wie Anhang B.3 (unverändert); Blocknamen geprüft (Dreiunddreißigster Auftrag, Lektorat Runde 23, 19.10.2026 23:07).
