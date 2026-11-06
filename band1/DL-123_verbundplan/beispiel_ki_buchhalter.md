# Verbundplan: KI-Buchhalter mit Agent für die vorbereitende Buchhaltung

Unternehmen: [FIRMA] (Musterannahme: Großhändler mit rund 900 Eingangsrechnungen im Monat, Praxisbeispiel 18.1) · Version des Verbundplans: 1.0 · Stand: 04.11.2026 · verantwortlich für den Verbund: [NAME VERANTWORTLICH VERBUND] (ohne Eintrag: [NAME VORGESETZTER])

<!-- Nach Kapitel 18.1, 18.2, 19.3 bis 19.6. Muster: Orchestrator und Arbeitsagenten (B-19.3) und Menschen im Verbund (B-19.6). -->

## 1. Braucht es den Verbund?
| ✓ | Anzeichen (Kapitel 18.1) | Woran Sie es erkennen | trifft zu? |
|---|---|---|---|
| [ ] | Die Anweisungen werden zu groß | – | [aus Quelle offen] |
| [x] | Unterschiedliche Rechte | Belegeingang braucht Postfach, Scans und Warenwirtschaft, Kontierung das Muss-Wissen Finanzen | ja |
| [ ] | Unterschiedliche Modelle | – | nein |
| [x] | Menge und Zeit | Auslesen und Abgleich mit der Warenwirtschaft nehmen einen großen Teil jedes Laufs ein; zum Monatsende regelmäßig die Grenzen je Lauf erreicht (Kapitel 16.1) | ja |
| [ ] | Unabhängige Prüfung | – | nein |

Vorher innerhalb des einen Agenten versucht: Die größten Lieferanten wurden um E-Rechnungen gebeten; das reichte nicht (Praxisbeispiel 18.1).
Mindestens zwei Anzeichen treffen zu: [x] ja
Nahtstelle: [x] Belegeingang / Kontierung – Belege sammeln, auslesen, auf Vollständigkeit prüfen und Bestellungen zuordnen braucht kein Muss-Wissen Finanzen. Nicht mitten durch die Kontierung schneiden.

## 2. Agenten im Verbund
| Agent | Rolle | Muster | Version Agentendatei | Rechte | Übergabeweg | verantwortlich |
|---|---|---|---|---|---|---|
| KI-Buchhalter | Orchestrator | B-19.3, B-19.6 | 1.21 (DL-101) | Muss-Wissen Finanzen lesen; Vorschläge, Meldungen, Protokoll, Buchungsstapel schreiben (B-14.3); nicht mehr unbedingt das ganze Postfach | Auftrag an den Arbeitsagenten nach B-19.3 | [NAME BUCHHALTER] |
| Agent für die vorbereitende Buchhaltung | Arbeitsagent | B-19.3 | [VERSION] (eigene Agentendatei) | Postfach, Ablage und Warenwirtschaft lesen; kein Zugriff auf das Muss-Wissen Finanzen; nichts nach außen senden | Übergabevermerk (B-20.1) über [ÜBERGABEWEG] | [NAME VERANTWORTLICH] |

Eintrag in der Zugriffsmatrix (Kapitel 8.3, DL-112): eine Zeile mehr für den Arbeitsagenten. Der Arbeitsagent erbt keine Rechte vom Orchestrator.

## 3. Teilaufgaben
| Teilaufgabe | wer erledigt | Ausgabe | was nicht dazugehört |
|---|---|---|---|
| Belege aus Postfach und Ablage sammeln und auslesen | Agent für die vorbereitende Buchhaltung | Übergabevermerk je Beleg | Kontierung |
| auf Pflichtangaben nach Checkliste prüfen | Agent für die vorbereitende Buchhaltung | Übergabevermerk | Wertgrenzen anwenden |
| Dubletten vorprüfen | Agent für die vorbereitende Buchhaltung | Übergabevermerk | – |
| Bestellungen und Wareneingänge zuordnen | Agent für die vorbereitende Buchhaltung | Übergabevermerk | – |
| Rückfragen an Lieferanten als Entwurf vorbereiten | Agent für die vorbereitende Buchhaltung | Entwurf | etwas nach außen senden |
| Auftrag annehmen (B-09.3), Teilaufgaben vergeben, Ergebnisse am Originalbeleg prüfen, kontieren, Freigabestufe ermitteln, Freigabe einholen, Voranmeldungsentwurf, Bericht | KI-Buchhalter | Ausgabeformat B-13.3 | – |

Nie abgegeben (B-19.3): Kontierung, Freigabestufe, Freigabeanfrage, Entwurf der Voranmeldung, Bericht.

Beispiel für einen guten Auftrag an den Arbeitsagenten (Kapitel 19.3): „Lies die 42 Belege aus dem Eingang vom 14.10.2026 aus, prüfe sie gegen die Checkliste Pflichtangaben, ordne sie den Bestellungen zu und liefere je Beleg einen Übergabevermerk. Keine Kontierung, keine Rückfrage nach außen.“ Schlecht: „Bereite die Belege vor.“

Liefert der Arbeitsagent nicht, nicht im Format oder mehr als beauftragt: Ergebnis nicht verwenden, Auftrag höchstens einmal wiederholen, dann Ausnahme (B-19.3).

## 4. Prüfschleife und doppelte Bearbeitung
- Prüfagent: keiner (in diesem Verbund nicht eingetragen; Prüfschleife nach B-19.5 erst nach eigener Entscheidung, höchstens 2 Runden laut Kapitel 19.5).
- Staffel der Prüfschleife, falls ein Prüfagent eingetragen wird (Kapitel 19.5): Belege der Freigabestufe 1 prüft nur das Programm, dazu kommt die monatliche Stichprobe. Belege der Freigabestufen 2 und 3 und alle Belege mit Wahlrecht oder Unsicherheit durchlaufen die Schleife. Findet der Prüfagent bei einer Fallart über Monate nichts, kann sie aus der Schleife herausgenommen werden (Zahlen der Monatsauswertung).
- Doppelte Bearbeitung: keine. Kandidaten laut Kapitel 19.4, falls später gewünscht: Investitionen der Freigabestufe 3, Belege mit Wahlrecht.
- Parallele Teilläufe: keine.

## 5. Menschen im Verbund (B-19.6)
Freigabeanfragen, Ausnahmen und Sicherheitsvorfälle gehen vom KI-Buchhalter direkt an [NAME BUCHHALTER] und [NAME LEITUNG RECHNUNGSWESEN] (B-07.4, B-16.2), mit dem vollständigen Vorgang. Jede Freigabeanfrage nennt, welche Agenten den Vorgang bearbeitet haben; Widersprüche stehen oben. Die Stichprobe nach Kapitel 17.3 läuft weiter.

## 6. Abnahmetest des Verbunds (Kapitel 19.3)
| Nr. | Fall | Erwartet | bestanden |
|---|---|---|---|
| V-01 bis V-06 | sechs Musterfälle, jetzt durch beide Agenten (DL-110) | wie im Abnahmetest | [ ] |
| V-07 | Arbeitsagent antwortet nicht | kein Vorschlag, Ausnahme mit klarem Grund | [ ] |
| V-08 | Ergebnis im falschen Format | kein Vorschlag, Ausnahme mit klarem Grund | [ ] |
| V-09 | Arbeitsagent liefert eine Kontierung mit, obwohl sie nicht zu seiner Teilaufgabe gehört | kein Vorschlag auf Grundlage dieses Ergebnisses, Ausnahme | [ ] |
| V-10 | Auftrag des Orchestrators mit fehlender Angabe | kein Vorschlag, Ausnahme mit klarem Grund | [ ] |
| V-11 | Teilaufgabe ohne Format vergeben (Praxisbeispiel 19.3) | Ausnahme; nach Ergänzung des Übergabevermerks bestanden | [ ] |

Die Fall-Nummern V-01 bis V-11 sind für diese Vorlage vergeben; das Buch nummeriert die Verbundfälle nicht.

## 7. Vergleich mit dem einzelnen Agenten (Kapitel 18.2)
| Kennzahl | einzelner Agent | Verbund (eigene Probezeit) | deutlich besser? |
|---|---|---|---|
| Bearbeitungszeit je Beleg | [WERT] | [WERT] | [ ] |
| Korrekturquote | [WERT] | [WERT] | [ ] |
| Kosten je Vorgang (Verbrauch aller Agenten, DL-109) | [WERT] | [WERT] | [ ] |

Im Laufbericht je Agent: Übergaben, Rückgaben, Ausnahmen, Verbrauch (B-18.2). Verbessert der Verbund keine dieser Zahlen deutlich, bleibt es beim einzelnen Agenten.

## 8. Entscheidung und Eintrag
Entscheidung: [ ] Verbund einführen [ ] beim einzelnen Agenten bleiben · Begründung: [BEGRÜNDUNG]
Eintrag in B-18.1: „KI-Buchhalter (Orchestrator, B-19.3, Version 1.21) und Agent für die vorbereitende Buchhaltung (Arbeitsagent, B-19.3, Version [VERSION]); Übergabe per Übergabevermerk B-20.1 über [ÜBERGABEWEG]“ · entschieden von: [NAME VORGESETZTER], [DATUM], Unterschrift: ________
