# Werkzeugbeschreibungen: KI-Buchhalter

Version 1.1 · Stand 19.10.2026 · verantwortlich: [NAME VERANTWORTLICH, ROLLE] · Server: Server Finanzen, Belegeingang, Ablage Vorschläge

<!-- Werkzeuge und Inhalte aus Kapitel 13.7 (Werkzeuge des Servers), 14.1 (Ablauf eines Belegs), 14.5 (Beispiel) und 14.6 (Rechte).
     Nicht genannte Einzelheiten stehen als [aus Quelle offen]. -->

## Werkzeugliste
| Nr. | Name | Zweck in einem Satz | ändert etwas? |
|---|---|---|---|
| 1 | `finanzen_muss_wissen_abrufen` („Muss-Wissen abrufen“) | Muss-Wissen Finanzen gültig zum Belegdatum abrufen; erster Aufruf jedes Laufs (B-14.1) | nein |
| 2 | `beleg_lesen` | Daten eines Belegs lesen | nein |
| 3 | `finanzen_kontierungsregel_suchen` | passende Kontierungsregel zum Belegdatum suchen | nein |
| 4 | `vorschlag_uebergeben` | Buchungsvorschlag in der Ablage Vorschläge ablegen | legt ab |
| 5 | `finanzen_aenderung_vorschlagen` | Änderung am Muss-Wissen vorschlagen, die ein Mensch prüft | legt einen Vorschlag ab, ändert nicht den Server |
| 6 | [WERKZEUG KONTOUMSÄTZE] | Kontoumsätze aus dem Buchhaltungsprogramm lesend abrufen | nein [aus Quelle offen: Name] |
| 7 | [WERKZEUG BUCHUNGSSTAPEL] | Buchungsstapel nach B-14.7 bereitstellen | legt ab [aus Quelle offen: Name, siehe DL-113] |

## 1. `finanzen_muss_wissen_abrufen` („Muss-Wissen abrufen“)
| Feld | Inhalt |
|---|---|
| Name | `finanzen_muss_wissen_abrufen` |
| Anzeigename | Muss-Wissen abrufen (Kapitel 1 und 9.4) |
| Zweck | Liefert die Wissensstücke des Muss-Wissens Finanzen, die zum Belegdatum gelten, etwa Kontenrahmen und Wertgrenzen. Nutze es als ersten Aufruf jedes Laufs und für jedes neue Belegdatum. Es ändert nichts. |
| Angaben | `belegdatum` · `themen` (etwa „Kontenrahmen“, „Wertgrenzen“) |
| Rückgabe | gültige Wissensstücke mit Version, gültig ab, gültig bis, Prüfsumme |
| Fehlerfälle | kein gültiges Wissensstück zum Belegdatum → [TEXT DER RÜCKGABE] [aus Quelle offen]. Verhalten des Agenten: kein Vorschlag, Ausnahme (B-09.4, B-14.5) |
| Rechte | Server Finanzen lesen |

## 2. `beleg_lesen`
| Feld | Inhalt |
|---|---|
| Name | `beleg_lesen` |
| Zweck | Liest die Daten einer Rechnung, bei einer E-Rechnung aus dem XML-Teil. [ERGÄNZUNG: wann nutzen, was es nicht tut] |
| Angaben | `belegnummer` |
| Rückgabe | Daten der Rechnung [aus Quelle offen: Feldliste] |
| Fehlerfälle | [aus Quelle offen] |
| Rechte | Belegeingang und Ablage Buchhaltung lesen; nicht löschen, nicht verschieben (B-14.4) |

## 3. `finanzen_kontierungsregel_suchen`
| Feld | Inhalt |
|---|---|
| Name | `finanzen_kontierungsregel_suchen` (statt `get_data`) |
| Zweck | „Sucht im Muss-Wissen Finanzen die Kontierungsregel, die zum Belegdatum für diesen Lieferanten und diese Leistung gilt. Nutze es vor jedem Buchungsvorschlag. Es ändert nichts.“ |
| Angaben | `belegdatum`, `lieferant_name`, `leistungsbeschreibung` (statt `id`) |
| Rückgabe | Regel, Konto, gültig ab und bis, Fundstelle, Version (statt interner Kennung) |
| Fehlerfälle | kein Treffer → „Keine Regel gefunden. Bitte Ausnahme an die Buchhaltung melden; nicht schätzen.“ (statt `404`) |
| Rechte | Server Finanzen lesen |

## 4. `vorschlag_uebergeben`
| Feld | Inhalt |
|---|---|
| Name | `vorschlag_uebergeben` |
| Zweck | Legt einen Buchungsvorschlag im Ausgabeformat B-13.3 in der Ablage Vorschläge ab. [ERGÄNZUNG: was es nicht tut, etwa nicht festschreiben] |
| Angaben | [aus Quelle offen: Felder des Vorschlags nach B-13.3] |
| Rückgabe | Bestätigung mit Kennung. Ohne Bestätigung gilt der Aufruf als nicht ausgeführt (B-02.5, B-14.1). |
| Fehlerfälle | [aus Quelle offen]. Verhalten des Agenten: höchstens ein weiterer Aufruf mit geprüften Angaben, dann Ausnahme mit Werkzeug, Angaben und Fehlermeldung (B-14.1) |
| Rechte | Vorschläge in einen eigenen Ordner schreiben; nichts überschreiben oder löschen (B-14.3) |

## 5. `finanzen_aenderung_vorschlagen`
| Feld | Inhalt |
|---|---|
| Name | `finanzen_aenderung_vorschlagen` |
| Zweck | Legt einen Vorschlag zur Änderung eines Wissensstücks ab, den ein Mensch prüft. Es ändert nichts am Server; neues Wissen speichert der Agent nicht selbst (B-13.7). |
| Angaben | Wissensstück, Vorschlag, Begründung, Beispielbelege [aus Quelle offen: Namen der Angaben] |
| Rückgabe | Kennung des Vorschlags; keine Änderung am Server |
| Fehlerfälle | [aus Quelle offen] |
| Rechte | Server Finanzen: Änderungsvorschläge ablegen |

## Rechte des Dienstkontos (Kapitel 14.6)
| Zugang | Recht |
|---|---|
| Server Finanzen | lesen; Änderungsvorschläge ablegen |
| Unternehmensserver | lesen |
| Belegeingang, Ablage Buchhaltung | lesen; Vorschläge in einen eigenen Ordner schreiben |
| Kontoumsätze aus dem Buchhaltungsprogramm | lesen |
| Lohnbuchungsliste | lesen, nur summarische Liste |
| Protokollablage | anhängen, nicht ändern, nicht löschen |
| DATEV | nur der eingerichtete Weg; kein Recht zum Festschreiben |
| alles andere | kein Zugang |

## Prüfliste der fünf Regeln (Kapitel 14.5)
| ✓ | Regel | Am KI-Buchhalter |
|---|---|---|
| [x] | Wenige, durchdachte Werkzeuge | ein Suchwerkzeug für die passende Regel statt „Liste alle Regeln“ und „Lies Regel“; zwei bis drei Werkzeuge für den Server Finanzen |
| [x] | Sprechende Namen mit Bereich | Präfix `finanzen_`, Angaben `belegdatum` statt `datum` |
| [ ] | Beschreibung wie für eine neue Kollegin | für Werkzeug 2, 4 und 5 ergänzen |
| [x] | Aussagekräftige Rückgaben | Regel, Konto, Gültigkeit, Fundstelle, Version; bei keinem Treffer Anweisung „nicht schätzen“ |
| [ ] | Sparsam mit Umfang | [aus Quelle offen: Grenze für Seiten oder Treffer festlegen] |

## Versionsvermerk
| Version | Datum | Änderung | Regressionstest bestanden am |
|---|---|---|---|
| 1.0 | 19.10.2026 | Erstfassung nach Band 1, Kapitel 14.5 | [DATUM] |
