# Ablaufmuster am KI-Buchhalter (Stufe Low Code)

<!-- Nach Kapitel 19 und 20.2. Gemeinsam für alle Muster:
     - Auslöser (20.2, B-15.1): Zeitplan werktags 07:00 Uhr oder neue E-Rechnung mit Skontofrist in den nächsten zwei Arbeitstagen; ist ein Orchestrator eingetragen, auch sein Auftrag nach B-19.3.
     - Fehlerpfad (20.2): Scheitert ein Schritt, endet der Ablauf für diesen Beleg mit einer Ausnahme, nicht mit einem zweiten Versuch auf anderem Weg.
     - Freigabe (20.2): Kein Vorschlag, der eine Freigabe braucht, geht ohne Freigabeschritt in den Stapel. In der Probezeit geht jeder Vorschlag über 500 € zur Einzelfreigabe, auch bei Freigabestufe 1; über 10.000 € bleibt es beim Vieraugenprinzip.
     - Schleifen immer mit fester Höchstzahl an Durchläufen. Parallele Zweige nur mit einem Schritt zum Zusammenführen.
     - Der Ablauf erzwingt die Reihenfolge; die Agentendatei sichert den Inhalt. -->

## 1. Orchestrator und Arbeitsagenten (B-19.3) – Ablauf aus Kapitel 20.2
| Element | Beschreibung |
|---|---|
| Auslöser | Zeitplan werktags 07:00 Uhr oder neue E-Rechnung mit Skontofrist in den nächsten zwei Arbeitstagen |
| Bedingung als Weiche | Ist der Eingang eine Rechnung, Gutschrift oder E-Rechnung? Wenn nein, Ablage oder Weiterleitung an einen Menschen. |
| Schritt 1 | Agent für die vorbereitende Buchhaltung liest aus und erzeugt je Beleg einen Übergabevermerk |
| Bedingung als Tor | Ist der Vermerk vollständig und gehen die Beträge auf? Wenn nein, Ausnahme an den Buchhalter. |
| Schritt 2 | KI-Buchhalter kontiert, ermittelt die Freigabestufe und schreibt die Begründung |
| Bedingung nach Freigabestufe | Freigabestufe 1 in den Buchungsstapel, Freigabestufe 2 in den Freigabeschritt beim Buchhalter, Freigabestufe 3 in den zweistufigen Freigabeschritt. |
| Probezeit | In der Probezeit geht jeder Vorschlag über 500 € zur Einzelfreigabe, auch bei Freigabestufe 1; über 10.000 € bleibt es beim Vieraugenprinzip. |
| Fehlerpfad | Scheitert ein Schritt, endet der Ablauf für diesen Beleg mit einer Ausnahme, nicht mit einem zweiten Versuch auf anderem Weg. |

Was der Ablauf sicherstellt (20.2): Der KI-Buchhalter bekommt nur Vermerke, die das Tor bestanden haben, und kein Vorschlag, der eine Freigabe braucht, geht ohne Freigabeschritt in den Stapel. Ob der Vermerk stimmt, prüft weiter der KI-Buchhalter am Beleg.

Praxisbeispiel 20.2: Ohne Tor startet der KI-Buchhalter auch bei leerem Vermerk und meldet je Beleg eine Ausnahme. Mit Tor endet der Ablauf vorher, und der Buchhalter bekommt eine einzige Meldung mit allen betroffenen Belegen.

## 2. Kette (B-19.1) – Kapitel 19.1
| Element | Beschreibung |
|---|---|
| Auslöser | wie oben |
| Schritt 1 | Agent Belegerfassung liest aus: Aussteller, Rechnungsnummer, Datum, Beträge, Steuersätze, bei E-Rechnungen aus dem XML-Teil |
| Tor 1 (Programm) | Angaben vollständig? Netto, Steuer und Brutto passen zusammen? Wenn nein: Ausnahme an den Buchhalter |
| Schritt 2 | KI-Buchhalter kontiert, ermittelt die Freigabestufe nach B-08.2, schreibt die Begründung; prüft die Daten am Originalbeleg |
| Tor 2 (Programm) | Ausgabeformat (B-13.3) und Soll gleich Haben? Wenn nein: Ausnahme |
| Freigabeschritte | danach Freigabeschritt oder Buchungsstapel nach Freigabestufe; Kein Vorschlag, der eine Freigabe braucht, geht ohne Freigabeschritt in den Stapel. In der Probezeit geht jeder Vorschlag über 500 € zur Einzelfreigabe, auch bei Freigabestufe 1; über 10.000 € bleibt es beim Vieraugenprinzip. |
| Fehlerpfad | Was ein Tor nicht besteht oder dem Beleg widerspricht, geht an einen Menschen, nicht zurück an den Vorgänger |

## 3. Weiche (B-19.2) – Kapitel 19.2
| Eingang | Weiche leitet an |
|---|---|
| Eingangsrechnung, Gutschrift, E-Rechnung | KI-Buchhalter |
| Mahnung eines Lieferanten | Kreditorenbuchhaltung (Mensch) |
| Lieferavis, Auftragsbestätigung | Einkauf |
| Preisliste, Werbung | Ablage ohne Bearbeitung |
| nicht einzuordnen | Buchhalter |

Zweite Art von Weiche nach Aufwand: Routinebelege eines Stammlieferanten an eine Einstellung mit günstigem Modell, Sonderfälle (Anzahlungen, innergemeinschaftliche Erwerbe, Investitionen) an ein stärkeres Modell; dieselbe Agentendatei, jeder Wechsel im Protokoll. Fehlerpfad: Der KI-Buchhalter gibt fehlgeleitete Vorgänge mit einem Satz Begründung an [RÜCKGABEWEG] zurück und leitet nie selbst weiter.

## 4. Parallele Teilläufe (B-19.4) – Kapitel 19.4
| Element | Beschreibung |
|---|---|
| Auslöser | Monatsende, Zeitplan [ZEITPLAN] |
| Aufteilung | am einfachsten nach Lieferanten (wegen der Summengrenze); sonst nach Filialen, Lieferantengruppen oder Paketen |
| Schritte | mehrere Teilläufe gleichzeitig |
| Zusammenführen | Dublettenprüfung (B-03.2) und Summengrenze je Lieferant (B-08.2) über alle Teilläufe des Zeitraums |
| Tor | Entwurf der Voranmeldung erst, wenn alle Teilläufe abgeschlossen sind oder ihre offenen Belege gemeldet haben |
| Grenzen | Grenzen je Lauf (B-16.1) je Teillauf und [GESAMTGRENZE] für alle zusammen; nie aufteilen, um Grenzen zu umgehen |
| doppelte Bearbeitung | nur für festgelegte Fallarten, etwa Investitionen der Freigabestufe 3 oder Belege mit Wahlrecht; weichen die Ergebnisse ab, Vorschlag als unsicher mit beiden Ergebnissen vorlegen |

## 5. Prüfschleife (B-19.5) – Kapitel 19.5
| Element | Beschreibung |
|---|---|
| Schritt 1 | KI-Buchhalter erstellt den Vorschlag |
| Schritt 2 | Programm prüft Konto gegen Kontierungsrichtlinie, Steuerschlüssel, Freigabestufe, Soll gleich Haben; Prüfagent (anderes Modell) prüft die Begründung nach Rubrik R1 bis R5 (DL-110) |
| Schleife | höchstens 2 Runden; Beanstandung nur übernommen, wenn am Beleg und im Muss-Wissen mit Fundstelle bestätigt |
| Fehlerpfad | keine Einigkeit nach 2 Runden: Vorgang mit beiden Fassungen an [NAME BUCHHALTER] |
| Freigabeschritt | Prüfung ist keine Freigabe; ermittelt der Prüfagent eine höhere Freigabestufe, gilt die höhere |
| Rechte Prüfagent | Beleg, Vorschlag, Prüfkriterien, genannte Wissensstücke; kein Zugang zu Freigabekanal, Buchungsstapel oder Postfach |

## 6. Menschen im Verbund (B-19.6) – Kapitel 19.6
| Element | Beschreibung |
|---|---|
| gilt | in jedem Ablauf, auch wenn kein anderes Muster genutzt wird |
| Freigabeschritte | Freigabeanfragen, Ausnahmen, Regelverstöße und Sicherheitsvorfälle direkt an die Menschen nach B-07.4 und B-16.2, mit dem vollständigen Vorgang, nicht über einen anderen Agenten |
| Inhalt der Freigabeanfrage | welche Agenten den Vorgang bearbeitet haben; Widersprüche an erster Stelle |
| Halt | wird der Agent nach B-11.4 angehalten, nimmt er auch von Agenten des Verbunds nichts mehr an |

Auf der Stufe No Code ist der Mensch die Orchestrierung: Kette mit dem Menschen als Tor, Prüfschleife mit einem zweiten Assistenten und die Übergabe an Menschen passen dort; Weiche und Aufteilung übernimmt der Buchhalter selbst (Kapitel 20.1).
