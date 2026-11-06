# DL-112 Wissensinventur: Erhebungsbogen, Zugriffsmatrix, Interview-Prompt

| | |
|---|---|
| Kennung | DL-112 |
| Version | 1.16 |
| Stand | 04.11.2026 |
| Kapitelbezug | 13.6 Wissensinventur vor dem Serverbau; 8.3 Datenzugang, Vertraulichkeit und Zugriffsmatrix; 12.1 Zugriffsmatrix als Serverzuschnitt; 13.5; 13.7; 14.6 Minimale Rechte; Baustein B-13.6 |
| Fundstellen im Buch | 13.6, Anhang B.5 (Anhang B.3) |

## Zweck
Vor dem Bau eines Wissensservers erheben, welches Wissen es gibt, wer es sehen darf und wer es pflegt. Der Erhebungsbogen stellt die neun Fragen aus Kapitel 13.6 und Anhang B.5: **Inhalt, Quelle, Aktualität, Gültigkeit, Vertraulichkeit, Zugriff, Freigabe, Aufbewahrung, Verantwortung**, im Wortlaut des Buches; die Ausfüllhinweise stehen in einer eigenen Spalte. Ergebnis sind Wissenskatalog, Zugriffsmatrix und Pflegeplan, erstellt per Interview-Prompt. Grundregel: Muss-Wissen nur für die eigene Abteilung, Kann-Wissen für alle, Vorgangsdaten nur für den Lauf. Die Zugriffsmatrix setzt Kapitel 8.3 kaufmännisch und Kapitel 14.6 technisch um (Rechte des Dienstkontos, siehe auch DL-128). Wissen, das nur im Kopf steht, wird aufgeschrieben; wiederholte Ausnahmen wegen fehlender Regeln weisen auf Lücken im Katalog hin (B-13.6).

## Dateien
| Datei | Inhalt |
|---|---|
| `leervorlage_erhebungsbogen.md` | Erhebungsbogen mit den neun Fragen wörtlich aus Kapitel 13.6 und Anhang B.5, Ausfüllhinweise in eigener Spalte |
| `leervorlage_zugriffsmatrix.csv` | Zugriffsmatrix (Spalten wie Kapitel 8.3) |
| `interview_prompt.md` | Prompt, mit dem ein Agent die Inventur im Gespräch führt (plattformneutral) |
| `beispiel_ki_buchhalter_erhebungsbogen.md` | Wissenskatalog Finanzen des KI-Buchhalters mit der Kontierungsrichtlinie als Beispiel aus Kapitel 13.6 und Pflegeplan |
| `beispiel_ki_buchhalter_zugriffsmatrix.csv` | Zugriffsmatrix aus Kapitel 8.3, ergänzt um die Lohnbuchungsliste (B-08.3/B-08.5) |

CSV: UTF-8 mit BOM, Semikolon.

## Anpassungshinweis
Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele. Fristen und Verantwortliche sind Beispiele aus dem Buch; Agentenprotokolle und Muss-Wissen als Teil der Verfahrensdokumentation mit 10 Jahren: Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrem Steuerberater ab. Die Zeile „Lohnbuchungsliste“ ist aus B-08.3 und B-08.5 abgeleitet; Aufbewahrung und Verantwortung dort sind offen.

## Änderungen in Version 1.3
- Version der Agentendatei 1.8.

## Änderungen in Version 1.4
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.5
- Anpassungshinweis: Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ (Umentscheidung Lizenz 11:21).
- Erhebungsbogen, Zeile Kontierungsrichtlinie: Zusatz „erstellt mit der Steuerkanzlei“ entfernt (keine Aussage über eine Prüfung durch die Steuerberatung).

## Änderungen in Version 1.6
- Aufbewahrung in Erhebungsbogen, Zugriffsmatrix und README: Prüfmarken durch den Leserhinweis „Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrer steuerlichen Beratung ab.“ ersetzt.

## Änderungen in Version 1.7
- Erhebungsbogen: Zuordnungstabelle des Steuerberaters (Spiegelung Manuskript 15:56 / Festlegung Buch-Autor 16:09).

## Änderungen in Version 1.8
- Interview-Prompt: Bankzugänge mit dem Vermerk „kein Bankzugang“; Erhebungsbogen „Eintrag im Änderungsprotokoll (B-11.3)“; Leserhinweis mit Ihrem Steuerberater; Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
- Erhebungsbogen: Verweis auf eine nicht veröffentlichte Quelle durch den Verweis auf das Buch (Kapitel 8.5) ersetzt (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 1.9
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Erhebungsbogen) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.10
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.11
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.12
- Erhebungsbogen: neun Fragen wörtlich nach Kapitel 13.6 und Anhang B.5, bisherige Zusätze als Ausfüllhinweise in eigener Spalte; Beispiel mit den neun Fragen als Spaltenlegende; README angepasst (Dreiunddreißigster Auftrag, Lektorat Runde 23, 19.10.2026 23:07).

## Änderungen in Version 1.13
- Beispiel, Kontierungsrichtlinie: Quelle wörtlich nach Kapitel 13.6 „Ordner Rechnungswesen, am besten mit Ihrem Steuerberater abgestimmt“ (Entscheidung des Buch-Autors; die Streichung in Version 1.5 beruhte auf keiner ausdrücklichen Entscheidung von Thore); Interview-Prompt wörtlich nach Anhang B.5 (Kopfzeile und Kommentar unverändert) (Vierunddreißigster Auftrag, 19.10.2026 23:09).

## Änderungen in Version 1.14
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.15
- Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.16
- Erhebungsbogen: Bezug auf die Agentendatei auf Version 1.21 gehoben (DL-101, freigegeben am 04.11.2026 um 20:02 MEZ). Stand 04.11.2026. (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
