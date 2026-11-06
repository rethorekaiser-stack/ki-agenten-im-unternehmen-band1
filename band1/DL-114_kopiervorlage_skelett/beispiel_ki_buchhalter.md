# Skelett: KI-Buchhalter

[FIRMA] (Testmandant: Muster Technik GmbH) · Version 1.1 · Stand 04.11.2026 · Vorgesetzter: [NAME VORGESETZTER]

| Schritt | Was | Vorlage | Ergebnis beim KI-Buchhalter |
|---|---|---|---|
| 1 | Anwendungsfall prüfen | DL-116 | zehn Buchhaltungsaufgaben bewertet, sieben Vorgangsarten freigegeben |
| 1a | Ablauf zerlegen | DL-117 | Eingangsrechnung in elf Schritten mit Übergabepunkten |
| 1b | Kennzahlen festlegen, Ausgangswert messen | DL-118 | acht Kennzahlen aus 3.3 plus Laufbericht B-03.3; Ausgangswerte [aus Quelle offen] |
| 2 | Stufe wählen | DL-115 | alle drei Stufen möglich: Kontierungsassistent, automatischer Belegeingang, volle Anbindung (Kontoumsätze nur lesend) |
| 3 | Stellenprofil | DL-119 (Vorlage), DL-103 (Beispiel) | `DL-103/beispiel_ki_buchhalter.md` |
| 4 | Direktive | DL-104 | `beispiel_ki_buchhalter.md` |
| 5 | Wissensinventur | DL-112 | Wissenskatalog Finanzen, Zugriffsmatrix aus Kapitel 8.3 |
| 6 | Agentendatei | DL-101 | Agentendatei Version 1.21, 92 Bausteine |
| 6a | Bausteine einordnen (25.2) | DL-102 | Grundbausteine übernehmen, Musterbausteine B-08.2, B-21.2, B-05.1, B-13.3 anpassen, Fachbausteine B-D1 bis B-D3, B-14.7, B-08.5 ersetzen |
| 6b | Reifegrad je Vorgangsart | DL-131 | Eingangsrechnungen und sonstige Kostenbelege erprobt, Anlagenzugänge und Ausgangsrechnungen in Erprobung (Praxisbeispiel 21.2) |
| 7 | Startprompt | DL-106 | Buchungslauf mit Wissensabruf zum Belegdatum |
| 8 | Ersteinrichtung | DL-107 | zehn Fragen plus 2a |
| 9 | Spiegeltabelle | DL-108 | `beispiel_ki_buchhalter.md` |
| 10 | Budget, ROI, TCO | DL-109 | Beispielwerte aus 10.7: Netto-Nutzen 1.185 € im Monat, Amortisation rund 3,5 Monate (Variante mit doppelter Prüfzeit 540 €, rund 7,8 Monate), erstes Jahr 10.020 €; Tokenlimit 25 Millionen Token im Monat (10.4) |
| 11 | Abnahmetest | DL-110 | sechs Musterfälle und Prüffall 4a in SKR 03 und SKR 04; Empfehlung: drei fehlerfreie Durchläufe; erweiterte Testliste mit Einschleusung (N-03, N-07 bis N-09), ausgeschlossenem Zweck (N-10) und Lückenfällen (L-01 bis L-03) |
| 11a | Prüfung vor dem ersten Lauf | B-25.3 | Prüfung nach B-25.3 bestanden, bevor der erste Lauf startet |
| 12 | Verfahrensdokumentation | DL-111 | `beispiel_ki_buchhalter.md` |
| 12a | Rechtsrahmen | DL-132 | Prüfliste zu Datenschutz, KI-Verordnung, Art. 50, GoBD und Steuerberatungsrecht ausgefüllt (Beispiel) |
| 13 | Bausteine | DL-102 | 92 Bausteine abgehakt |
| 14 | Probezeit | DL-120 | 4 Wochen, Einzelfreigabe über 500 € Rechnungsbetrag (brutto), zusätzlich prüft ein Mensch jeden Vorschlag; Korrekturliste und Wochenbericht |
| 15 | Ausweitung | DL-121 | erste Ausweitung: Ende der Probezeit, Normalbetrieb mit Staffel bis einschließlich 2.500 € / bis einschließlich 10.000 € |
| 16 | Pflege | DL-122 | monatlich, vierteljährlich, jährlich, bei Anlass; Versionsübersicht |
| 17 | Laufzeit messen | DL-133 | Teilzeiten je Beleg, Laufzeit je Lauf, Vorher/Nachher je Maßnahme; Beispielwerte aus 24.1 (zur Orientierung, keine Messergebnisse) |

## Kurzprofil
- **Rolle:** Assistent des menschlichen Buchhalters in der Finanzbuchhaltung, klar als KI benannt.
- **Ziel:** jeder Beleg zum Monatsende als prüfbarer Vorschlag mit Begründung; Richtigkeit vor Geschwindigkeit.
- **Einsatzbereich:** eigene Buchführung, Deutschland, Industrie/Groß-/Einzelhandel, Regelbesteuerung oder § 19 UStG, SKR 03/04/IKR.
- **Darf nie:** festschreiben, UStVA übermitteln, Wahlrechte ausüben, Zahlungen auslösen (kein Bankzugang), Stammdaten ändern, ohne Freigabe nach außen kommunizieren, für Dritte buchen, Lohn rechnen.
- **Freigabe:** über 2.500 € Rechnungsbetrag (brutto) Buchhalter, über 10.000 € Vieraugen, Probezeit 500 €, UStVA und Lohn immer.
- **Muss-Wissen:** Einrichtungsprotokoll, Kontenrahmen mit Jahresfassung, Kontierungsrichtlinie, Steuersätze, Wertgrenzen – gültig zum Belegdatum.
- **Eskalation an:** [NAME BUCHHALTER], Vertretung [NAME VERTRETUNG].

## Was Sie für einen eigenen Agenten ersetzen
| Beim KI-Buchhalter | Bei Ihrem Agenten |
|---|---|
| Fachwissen-Bausteine B-D1 bis B-D3, B-14.7 | Ihr Fachwissen mit Gültigkeit |
| B-08.5 Lohnbuchungen | Ihre stellenspezifische Grenze |
| Wertgrenzen nach Rechnungsbetrag (brutto) | Ihre Bezugsgröße und Schwellen |
| Musterfälle in SKR 03/04 | echte und schwierige Fälle Ihrer Stelle |
| Musterbausteine B-08.2, B-21.2, B-05.1, B-13.3 | Aufbau übernehmen, Inhalt Ihrer Stelle (Kapitel 25.2) |
| Einrichtungsfragen zu USt und Kontenrahmen | Ihre unternehmensbezogenen Angaben |
