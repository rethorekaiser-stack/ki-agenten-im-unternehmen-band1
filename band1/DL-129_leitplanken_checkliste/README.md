# DL-129 Leitplanken-Checkliste

| | |
|---|---|
| Kennung | DL-129 |
| Version | 1.13 |
| Stand | 04.11.2026 |
| Kapitelbezug | Kapitel 16 Leitplanken: 16.1 Technische Grenzen, 16.2 Freigabeschritte, 16.3 Protokollierung und Überwachung, 16.4 Schutzmaßnahmen; 12.1; 14.6; Bausteine B-14.6, B-16.1 bis B-16.4, B-10.4, B-11.4 |
| Fundstellen im Buch | 16 (Anhang B.3) |

## Zweck
Leitplanken sind die technischen Grenzen, die auch dann halten, wenn das Modell sich irrt. Die Checkliste prüft alle vier Arten aus Kapitel 16: technische Grenzen für Verbrauch und Laufzeit, Freigabeschritte, die Wertgrenzen durchsetzen, Protokollierung und Überwachung nach den GoBD und Schutzmaßnahmen gegen eingeschleuste Anweisungen und für die Daten. Je Punkt wird eingetragen, wer oder was ihn durchsetzt und wer ihn geprüft hat.

## Dateien
- `leervorlage.md` – Checkliste zum Ausfüllen.
- `beispiel_ki_buchhalter.md` – ausgefüllt für den KI-Buchhalter mit den Werten aus Kapitel 16.

## Anpassungshinweis
Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele. Die Grenzen setzt das Programm oder die Plattform, nicht das Modell; die Agentendatei sagt zusätzlich, wie sich der Agent verhält (B-16.1). Die Richtwerte 15 Werkzeugaufrufe je Beleg und 60 Minuten je Lauf sind Beispiele des Buches (Startwert, anpassbar). Agentenprotokolle 10 Jahre Aufbewahrung: Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrem Steuerberater ab. Auf No Code sind die meisten Leitplanken organisatorisch; tragen Sie dann ein, welcher Mensch die Regel durchsetzt.

## Änderungen in Version 1.1
- Version der Agentendatei 1.8.
- Abschnitt 2: Reifegrad je Vorgangsart (B-21.2).
- Abschnitt 4: B-08.1 neu (kein Vorschlag bei Verdacht auf Einschleusung); Testfälle N-03 und N-07 bis N-09 nach Kapitel 22.4.

## Änderungen in Version 1.2
- Testfall-Nummern nach DL-110 neu: Einschleusungsfälle aus 22.4 heißen N-07 bis N-09.
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.3
- Richtwerte 15 Aufrufe je Beleg und 60 Minuten je Lauf als „Startwert, anpassbar“ gekennzeichnet, die zugehörigen Prüfmarken entfernt (Entscheidungen Thore 19.10.2026, 11:06).
- Freigabestufen: Summengrenze über 7 Kalendertage, Lohnbuchungen immer einzeln zur Freigabe, mindestens Stufe 2 (B-08.5).

## Änderungen in Version 1.4
- Anpassungshinweis: Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ (Umentscheidung Lizenz 11:21).

## Änderungen in Version 1.5
- Aufbewahrung der Agentenprotokolle: Prüfmarken in Beispiel und README durch den Leserhinweis „Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrer steuerlichen Beratung ab.“ ersetzt; doppelten Hinweis „Kein Rechtsrat.“ entfernt.

## Änderungen in Version 1.6
- Freigabestufe; Leserhinweis mit Ihrem Steuerberater; Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
- „E-Mail“ statt „Mail“ (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 1.7
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Kopf des Beispiels) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.8
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.9
- Beispiel, Zeile Reifegrad je Vorgangsart: „über 10.000 € gilt weiter das Vieraugenprinzip“ (Kapitel 21.2) (Achtundzwanzigster Auftrag, Lektorat Runde 17, 19.10.2026 22:50).
- Nachtrag Runde 18: Testfälle aus 22.4 nur noch mit Verweis auf DL-110 (nicht mehr DL-131) (Achtundzwanzigster Auftrag, Nachtrag Lektorat Runde 18, 19.10.2026 22:55).

## Änderungen in Version 1.10
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.11
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.12
- Abschnitt Schutzmaßnahmen: drei neue Prüfpunkte nach Kapitel 14.6 und B-14.6 (Verweis statt Wert und Schwärzen, `.gitignore` und `.env.example`, Schlüsselrotation und Widerruf); Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.13
- Beispiel: Version der Agentendatei 1.21. (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
