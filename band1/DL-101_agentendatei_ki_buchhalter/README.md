# DL-101 Komplette Agentendatei KI-Buchhalter

| | |
|---|---|
| Kennung | DL-101 |
| Version | 1.21 (gleich der Version der Agentendatei) |
| Stand | 05.11.2026 |
| Autor | Charlie Moore |
| Kapitelbezug | Anhang D5; Bausteine aus den Kapiteln 1 bis 25 (Teil I bis VII) und Anhang D1–D3; Übersicht aller Bausteine in DL-102 |
| Fundstellen im Buch | Einleitung, 1, 2, 9, 13.3, Anhang D5; Kopf jedes Bausteinkastens (Anhang B.3) |

## Zweck
Die vollständige, plattformneutrale Muster-Agentendatei des Referenzagenten in neun Teilen: Rolle, Ziel, Einsatzbereich; Anweisungen, Wissen und Arbeitsbeginn; feste Regeln und Rechte; Fachwissen-Regeln; Ausgabeformat; Eskalation, Zusammenarbeit, Protokoll und Berichte; Einrichtungsgespräch; Abnahmetest und Betrieb; Versionsvermerk und Änderungsprotokoll. 92 Bausteine.

Neu in Version 1.7 der Agentendatei (Teil VI, Kapitel 21 bis 23): B-21.2 Reifegrad je Vorgangsart, B-22.1 Keine Angabe ohne Grundlage, B-22.2 Unsicherheit weitergeben, B-22.3 Lange Unterlagen und Kontext, B-22.5 Plattform und Bindung, B-23.1 Personenbezogene Daten, B-23.2 Ausgeschlossene Einsatzzwecke, B-23.5 Keine Steuerberatung, keine Haftungsübernahme.

Neu in Version 1.8 (Teil VII, Kapitel 24 und 25): B-24.1 Laufzeit messen, B-24.3 Zwischengespeicherte Stände, B-24.5 Abrufe bündeln, B-24.6 Zwischenstände, B-25.2 Übernommene und unpassende Abschnitte, B-25.3 Prüfung vor dem ersten Lauf. B-08.1 geändert: Bei Verdacht auf eingeschleuste Anweisung gibt es keinen Buchungsvorschlag, sondern eine Ausnahme mit Zitat der Stelle und Vorlage beim Buchhalter.

**Wichtig:** Steht in B-18.1 „keiner“, ruhen B-18.2, B-19.1 bis B-20.3 und die Verbund-Sätze in B-04.2 und B-15.1. Am Verhalten des einzelnen Agenten ändert sich dann nichts. Vorgangsarten ohne Reifegrad-Eintrag im Betriebsprotokoll (B-21.2) gelten als „in Erprobung“; ihre Vorschläge gehen einzeln zur Freigabe. Über 10.000 € gilt auch hier das Vieraugenprinzip.

## Dateien
- `beispiel_ki_buchhalter.md` – die Agentendatei Version 1.21 aus dem Buch (Anhang D5, freigegeben am 04.11.2026 um 20:02 MEZ), byte-gleich mit der Quelle (MD5 DA3C67BEE3E8972DF735B4CC4B4EE8B4).
- `leervorlage.md` – dieselbe Gliederung mit allen 92 Baustein-IDs; Abschnitte mit Kurzvorgabe oder Hinweis auf Wortlaut und Platzhalter im Beispiel.

## So verwenden Sie die Datei
1. Vor dem Einfügen alle Platzhalter in Großbuchstaben und eckigen Klammern ersetzen, etwa [FIRMA] und [VERSION STELLENPROFIL]. Was im Einrichtungsgespräch (Teil 7) erfragt wird, bleibt Platzhalter.
2. In B-18.1 „keiner“ eintragen, solange Sie keinen Verbund betreiben. Einen Verbund planen Sie mit DL-123.
3. Reifegrad je Vorgangsart im Betriebsprotokoll führen (B-21.2), Ablageort bei [ABLAGE BETRIEBSPROTOKOLL] eintragen (DL-131), Zielzeiten in B-24.1 (DL-133).
4. Datei als Ganzes in das Anweisungsfeld Ihres KI-Werkzeugs einfügen; ist es zu kurz, Teile 4 bis 6 als Wissensdatei ablegen.
5. Vor dem ersten Lauf nach B-25.3 prüfen, Einrichtungsgespräch führen lassen (DL-107), Protokoll bestätigen, Abnahmetest bestehen lassen (DL-110). Erst dann echte Belege, zunächst in der Probezeit (DL-120).
6. Für einen zweiten Agenten die Bausteine nach DL-102 (Abschnitt „Einordnung für einen zweiten Agenten“) und Kapitel 25 übernehmen.

## Anpassungshinweis
Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele. Hintergrund: Kapitel 23, DL-132. Zwingend an Ihr Unternehmen anpassen, vorbehaltlich der Prüfung durch Ihren Steuerberater. Feste Regeln (Teil 3) ändern Sie nur in der Datei, mit Eintrag im Änderungsprotokoll (B-11.3, Teil 9).

## Änderungen in Version 1.4
- B-21.2 wörtlich nach Agentendatei Version 1.8 bzw. Anhang D5 (Bereinigung 4): Reifegrad im Betriebsprotokoll mit Platzhalter [ABLAGE BETRIEBSPROTOKOLL], Start „in Erprobung“, vier Spiegelstriche. B-11.3 Zeile 1.8 um B-21.2 ergänzt. Version der Agentendatei bleibt 1.8 mit 92 Bausteinen. Leervorlage B-21.2 angepasst; Anleitung Schritt 3 neu.
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.5
- README: Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ ersetzt den bisherigen Hinweis (Umentscheidung Lizenz 11:21).
- Beispiel B-08.2: Prüfmarke zum Zeitraum 7 Tage entfernt (Summengrenze über 7 Kalendertage, Entscheidung 11:06). Die Agentendatei im Manuskript hat die Marke noch.

## Änderungen in Version 1.6
- Beispiel wortgleich mit der aktualisierten Agentendatei des Manuskripts (Stand 19.10.2026, 11:17), Abgleich per Diff ohne Abweichung. Damit unter anderem: B-08.2 endet mit „(Festlegung des Stellenprofils.)“, mehrere Prüfmarken des Manuskripts sind dort aufgelöst, die Dok.-Nr. der DATEV-Steuerschlüsseltabelle steht nicht mehr im Text, der Hinweis im Kopf lautet jetzt „keine Steuer- oder Rechtsberatung“.

## Änderungen in Version 1.7
- Anpassungshinweis: Satz zu offenen Prüfmarken entfernt, die Agentendatei enthält keine mehr (Abgleich mit dem Manuskript, Stand 19.10.2026 11:17).

## Änderungen in Version 1.8
- Anpassungshinweis: „vorbehaltlich der Prüfung durch Ihren Steuerberater“ statt Abnahme durch die Steuerkanzlei (Festlegung Thore 11:42). Agentendatei unverändert, wortgleich mit der Quelle.

## Änderungen in Version 1.9
- Einleitung B-05.1: „mit Ihrem Steuerberater abzustimmen“ statt „mit Ihrer Steuerkanzlei abzustimmen“ (Festlegung Buch-Autor 15:57; Quelle auf dem PC hatte den Satz um 15:57 noch nicht, Abweichung gemeldet). Leervorlage ohne diesen Satz.

## Änderungen in Version 1.10
- Beispiel byte-gleich zur Agentendatei Stand 15:56 (MD5 F04DEFDEE22CEBD552451C75516AAEC1): Steuerkanzlei/Kanzlei → Steuerberater laut Quelle (Spiegelung Manuskript 15:56 / Festlegung Buch-Autor 16:09).

## Änderungen in Version 1.11
- Beispiel byte-gleich zur Agentendatei Version 1.10 (MD5 536F156D960EA2ED25DC48617DD7EC7F). Leervorlage: Freigabestufe, Start „in Erprobung“ (B-21.2), Teil 9 „Versionsvermerk und Änderungsprotokoll“, B-02.5 „Teil 3 gilt auf jeder Ausbaustufe gleich“ (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.12
- README: Bezug „aus dem Buch (Anhang D5)“; Beispiel unverändert (MD5 536F156D960EA2ED25DC48617DD7EC7F) (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.13
- Beispiel byte-gleich zur Agentendatei Version 1.12 (MD5 A5D448DA2448733E94C2BB41B12ACC54). Leervorlage: Gliederung nach Version 1.12, B-05.1 mit Frage 5 „Wie heißt Ihr Steuerberater oder Ihre Kanzlei?“ und Folge „Füllt [NAME STEUERBERATER] (B-23.5).“, B-23.5 mit Platzhalter [NAME STEUERBERATER] (Neunzehnter Auftrag, Agentendatei v1.12, 19.10.2026 21:40).

## Änderungen in Version 1.14
- Leervorlage „Zu dieser Datei“ und README Schritt 1: „Platzhalter in Großbuchstaben und eckigen Klammern“ nach dem Kopf der Agentendatei Version 1.12; Beispiel unverändert (MD5 A5D448DA2448733E94C2BB41B12ACC54) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.15
- Beispiel byte-gleich zur Agentendatei Version 1.14 (MD5 21BF0AD8C9C214A0E6C43FE789F38326), B-23.5 „Ich lege sie ihm vor ([NAME STEUERBERATER]).“; Leervorlage Gliederung nach Version 1.14, B-23.5 mit Platzhalter [NAME STEUERBERATER] unverändert; README (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen Repo-Stand 2026-10-19-b
- Versionszählung auf Wunsch des Buch-Autors: DL-101 trägt ab jetzt die Version der Agentendatei, derzeit 1.14. Die bisherige Repo-Zählung mit den Versionen 1.13 bis 1.15 ist abgelöst; die Vermerke dazu bleiben unverändert. Ist ohne neue Agentendatei eine eigene Zählung nötig, gilt die Form „Repo-Stand 2026-10-19-b“. Beispiel und Leervorlage unverändert (MD5 Beispiel 21BF0AD8C9C214A0E6C43FE789F38326) (Zweiundzwanzigster Auftrag, 19.10.2026 22:02).

## Änderungen in Version 1.18
- Beispiel byte-gleich zur Agentendatei Version 1.18 (freigegeben am 19.10.2026 um 22:51 MESZ, MD5 9065DB03F1E5AC1A9F384AEA0E2F37FA): B-21.2 „Über 10.000 € gilt auch hier das Vieraugenprinzip.“ (1.15), B-03.3 „Ausnahmequote und Korrekturquote weist du für den ganzen Lauf und je Vorgangsart (B-03.1) aus.“ (1.16), B-23.5 mit eigenem Hinweissatz (1.17), B-16.3 mit Feld „Vorgangsart (B-03.1)“ (1.18), Teil 9 mit Zeilen 1.15 bis 1.18. Die Versionen 1.15 bis 1.17 wurden im Repository übersprungen. Leervorlage: Gliederung nach Version 1.18, B-03.3, B-16.3, B-21.2 und B-23.5 sinngleich ergänzt, Teil 9 bleibt leer (nur Erstfassung). README: Version 1.18 gleich der Agentendatei, Repo-Stand-Zählung entfällt (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.19
- Beispiel byte-gleich zur Agentendatei Version 1.19 (freigegeben am 19.10.2026 um 23:16 MESZ, MD5 15DB132560BFE285816DE087C355C62F, SHA256 CCDF60242F2FB8A1217BC324949C8BF230111C67572F5E18DC337B56676C22D7): B-D2 „Gelangensnachweis (§§ 17a, 17b UStDV).“, B-D3 GWG-Satz mit dem Vorschlag des Bundesrats, Status-Zeichen A′ (U+2032) in B-D2, B-13.3 und B-05.1, Teil 9 mit Zeile 1.19. Leervorlage: nur die Versionsangabe, Teil 9 bleibt bei „Erstfassung“ (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.20
- Beispiel byte-gleich zur Agentendatei Version 1.20 (freigegeben am 03.11.2026 um 23:30 MEZ, MD5 3DFA8D5E304E93E52B4331C061310F79, SHA256 7FE7DC0B77B224CEEC6A710589461314288335211012C3B791D1524F94F6BAAA): B-14.6 um den Verweis auf Zugänge nur mit ihrem Namen im Tresor (etwa DATEV_CLIENT_SECRET) und das Schwärzen von Werten aus Werkzeugantworten ergänzt; B-D1 Kernkonten um die Konten der Geschäftsvorfälle G-01 bis G-11 (Anhang D4) ergänzt; Teil 9 mit Zeile 1.20. Leervorlage: nur Versionsangabe, Abschnitte B-14.6 und B-D1 bleiben Platzhalter (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.21
- Beispiel byte-gleich zur Agentendatei Version 1.21 (freigegeben am 04.11.2026 um 20:02 MEZ, MD5 DA3C67BEE3E8972DF735B4CC4B4EE8B4, SHA256 BA5E9A0989F3DD2DB66718D05D80D97CEDFE56ABD170A13CCEC6FD4989BDCC11): B-D1 Kernkonten nach Zweck geordnet und um die Zeile Umsatzsteuer 7 % (SKR 03 1771, SKR 04 3801) ergänzt; B-D2 Saldenabgleich um 1771/3801, 1571/1401 und 1588/1433 ergänzt, Kennzahlen um Kz. 62; Teil 9 mit Zeile 1.21. Leervorlage: Bezug auf Version 1.21.
- Berichtigung: Die Agentendatei Version 1.20 wurde am 03.11.2026 um 22:30 MEZ freigegeben, nicht um 23:30 MEZ wie im Vermerk zu Version 1.20 oben und in der Datei 1.20 eingetragen. Der Vermerk oben bleibt als Verlauf stehen (Achtunddreißigster Auftrag, Lektorat Runde 29, 04.11.2026).

## Änderungen Repo-Stand 2026-11-05-r32
- README-Hinweis: GWG-Grenze und Sammelposten in B-D3 vor Druck prüfen (JStG 2026, 2./3. Lesung 13.11.2026) [PRÜFEN bis Drucklegung]. Die Datei beispiel_ki_buchhalter.md bleibt byte-gleich zur Agentendatei 1.21 (B03: Marke nur außerhalb des Kastens / hier in der README). (Einundvierzigster Auftrag, Lektorat Runde 32, 05.11.2026)
