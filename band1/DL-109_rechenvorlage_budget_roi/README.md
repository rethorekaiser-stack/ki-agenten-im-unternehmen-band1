# DL-109 Rechenvorlage Wirtschaftlichkeit mit Token- und Kostenschätzer

| | |
|---|---|
| Kennung | DL-109 |
| Version | 2.8 |
| Stand | 19.10.2026 |
| Kapitelbezug | Anhang B.6; Kapitel 10: 10.2 Token und Verbrauch (Tabelle 10.2), 10.4 Budget und Warnschwellen, 10.5 Ausgabengrenze, 10.6 Netto-Nutzen, 10.7 Rechenvorlage am KI-Buchhalter; Bausteine B-10.2, B-10.4, B-10.6 |
| Fundstellen im Buch | Einleitung, 3.3, 10.2, 10.7, Anhang B.6 (Anhang B.3) |

## Zweck
Die Wirtschaftlichkeit eines Agenten in den vier Schritten aus Kapitel 10.7 und Anhang B.6 rechnen: (1) eingesparte Zeit pro Monat, also Zeit heute gegen Zeit mit Agent für die Prüfung der Vorschläge und die Bearbeitung der Ausnahmen, (2) laufende Kosten des Agenten pro Monat, (3) einmalige Kosten, (4) Ergebnis: Netto-Nutzen im Monat, Amortisation, Ergebnis im ersten Jahr und Kosten je Beleg vorher und nachher. Dazu die zweite Variante mit doppelter Prüfzeit (6 statt 3 Stunden je Woche), die Posten, die nicht in der Rechnung stehen, und das Budget mit Warnschwellen. Der **Token- und Kostenschätzer** rechnet die Verbrauchsschätzung aus Tabelle 10.2 mit eigenen Werten, Preisen, Cache-Anteil und Wechselkurs durch. Der Token- und Kostenschätzer war früher als eigener Download geplant und ist hier integriert; die damals vorgesehene Nummer DL-124 ist mit Teil V neu vergeben.

## Dateien
| Datei | Inhalt |
|---|---|
| `leervorlage.csv` | Rechenvorlage in vier Schritten, Spalte „Wert“ leer |
| `beispiel_ki_buchhalter.csv` | Rechenvorlage mit den Beispielwerten aus Kapitel 10.7 |
| `leervorlage_tokenschaetzer.csv` | Token- und Kostenschätzer, Spalte „Wert“ leer, zwei Modelle zum Vergleich |
| `beispiel_ki_buchhalter_tokenschaetzer.csv` | Token- und Kostenschätzer mit den Beispielwerten aus Kapitel 10.2 (mittleres Modell und Spitzenmodell) |

Format: UTF-8 mit BOM, Semikolon, Dezimalkomma, keine Tausenderpunkte. Die Spalte „Formel“ ist Text und rechnet nicht selbst; übertragen Sie sie in Ihre Tabellenkalkulation (Spalte „Wert“ der genannten IDs).

## Blöcke der Rechenvorlage
| IDs | Block | Kern der Formel |
|---|---|---|
| A01–A03 | Annahmen | Belege, Stundensatz, Wochen je Monat |
| Z01–Z09 | Schritt 1: eingesparte Zeit | Stunden je Woche × A03, bewertet mit A02 |
| L01–L05 | Schritt 2: laufende Kosten | Lizenzen + Verbrauch + Pflege |
| E01–E07 | Schritt 3: einmalige Kosten | Aufbau + Prüfung durch Ihren Steuerberater + Mehraufwand Probezeit |
| N01–N05 | Schritt 4: Ergebnis | Netto-Nutzen = Z09 − L05, Amortisation = E07 / N01, erstes Jahr = 12 × N01 − E07, Kosten je Beleg |
| V01–V07 | Variante Prüfzeit | doppelte Prüfzeit (6 statt 3 h je Woche): Zeit mit Agent (V06, V07), eingespart, Netto-Nutzen, Amortisation |
| O01–O03 | nicht in der Rechnung | Fehlernutzen, Kosten höherer Ausbaustufe, Wirkung auf Menschen |
| B01–B07 | Budget | Betrag in Euro, Kostenstelle, Warnschwellen 70 / 90 / 100 %, Tokenlimit, Erhöhung der Ausgabengrenze |

## Token- und Kostenschätzer
Verbrauch je Beleg = Aufrufe × (Anweisungen + Wissen + Beleg + Verlauf). Kosten mit Zwischenspeicher = Eingabe-Token × Preis × ((1 − Cache-Anteil) + Cache-Anteil × Lesefaktor) + Ausgabe-Token × Preis, ohne Aufschlag für das Schreiben in den Speicher. Das Ergebnis in Euro (S22) geht mit Reserve als L02 in die Rechenvorlage. S23 gleicht das Tokenlimit mit dem geschätzten Verbrauch ab.

## Anpassungshinweis
**Alle Werte im Beispiel sind Beispielwerte aus Kapitel 10.2 und 10.7, keine Messwerte.** Ersetzen Sie sie in der Probezeit durch Ihre Messwerte; den Verbrauch liefert der Agent nach B-10.2 und B-10.6, die Arbeitszeit der Menschen tragen Sie selbst ein. Rechnen Sie immer zwei Varianten, eine mit Ihrer erwarteten Prüfzeit und eine mit der doppelten (Anhang B.6); erst wenn sich der Agent auch in der zweiten trägt, ist die Entscheidung belastbar. Wie im Buch (Kapitel 10.7) rechnen alle Eurobeträge mit den angezeigten, auf eine Nachkommastelle gerundeten Stunden (erstes Jahr 10.020 €); die ungerundeten Werte stehen im Hinweisfeld. Preise und Wechselkurs ändern sich; notieren Sie Preisliste und Stand. Das Tokenlimit im Beispiel ist 25 Millionen Token im Monat: Schätzung aus 10.2 (rund 20,6 Millionen) plus rund 20 % Puffer, Warnschwellen bei 17,5, 22,5 und 25 Millionen Token (Kapitel 10.4). Das Monatsbudget (B01) tragen Sie selbst ein: [EIGENER WERT] markiert Werte, die Sie selbst aus Ihrem Betrieb eintragen; in der Agentendatei steht dafür [BETRAG] (B-10.4). Der im Hinweisfeld als Beispielwert genannte Betrag (120 € aus dem Praxisbeispiel in Kapitel 10.4) dient nur zur Orientierung. Vertragsfragen stehen in DL-125.

Änderung gegenüber Version 1.0: neue Struktur nach den vier Schritten aus Kapitel 10.7 mit Beispielwerten, Token- und Kostenschätzer (früher als eigener Download geplant) integriert. Die damals vorgesehene Nummer DL-124 ist mit Teil V neu vergeben (Übergabevermerk und Ablaufmuster).

## Änderungen in Version 2.1
- Abgleich mit Kapitel 10.7 und 10.4 (Manuskript komplett, 19.10.2026): N03 Ergebnis im ersten Jahr 10.044 € wie im Manuskript (vorher 10.040 €).
- Variante Prüfzeit wie im Manuskript: V02 17,4 h, V03 868 € (Formel 2.600 € − 1.732 €), V04 538 €; V05 bleibt 7,8 Monate.
- B06 und S23 Tokenlimit 25 Millionen Token im Monat mit Warnschwellen 17,5 / 22,5 / 25 Millionen (vorher 500.000 Token mit Prüfmarke).
- Zwei Varianten nach Anhang B.6 (erwartete und doppelte Prüfzeit).

## Änderungen in Version 2.2
- B01 Budget je Monat: [EIGENER WERT] statt „aus Quelle offen“; Beispielwert 130 €/Monat (L01 + L02) im Hinweisfeld, als Beispielwert gekennzeichnet. Erklärung der Markierung oben im Text. Sonst unverändert.

## Änderungen in Version 2.3
- Werte nach Kapitel 10.7 neu (Euro aus den angezeigten Stunden): Z07 1.085 €, Z09 1.515 €, N01 1.185 €, N03 10.020 €, N05 rund 7,08 €; Variante 1.730 €, V03 870 €, V04 540 €; Amortisation unverändert rund 3,5 bzw. 7,8 Monate.
- B01 Beispielwert 120 €/Monat nach Praxisbeispiel 10.4 statt 130 € (L01 + L02); in der Agentendatei [BETRAG] (B-10.4).
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 2.4
- Onboarding laut Preisliste ohne Prüfmarke (Kapitel 2.5, 10.7); Tokenschätzer: „Messen Sie den Wert am eigenen Modell nach.“ nach Kapitel 10.2 (Abgleich mit dem Manuskript, Stand 19.10.2026 11:17).

## Änderungen in Version 2.5
- Zeile E03 in Beispiel und Leervorlage: „Prüfung durch Ihren Steuerberater“ statt Abnahme durch die Steuerkanzlei, Beträge unverändert; Spaltenübersicht E01–E07 angeglichen (Festlegung Thore 11:42).

## Änderungen in Version 2.6
- Beispiel-CSV, Zeilen L05 und N02: Verweis auf eine nicht veröffentlichte Quelle durch „Rahmen dieses Buches (Kapitel 10.7)“ ersetzt (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 2.7
- Beispiel-CSV (7 Zeilen) und README: Bezug „wie im Buch“ vereinheitlicht (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 2.8
- Vier Schritte im Zweck nach Kapitel 10.7 und Anhang B.6; Variante mit doppelter Prüfzeit (6 statt 3 Stunden): neue Zeilen V06 (34,6 h) und V07 (1.730 €) nach Kapitel 10.7, V02 = Z02 − V06 und V03 = Z03 − V07 rechnen jetzt mit den angezeigten Stunden wie das Buch (vorher ergab die Formel in V03 868 € statt 870 €); alle Werte nachgerechnet (Dreiunddreißigster Auftrag, Lektorat Runde 23, 19.10.2026 23:07).
