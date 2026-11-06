# Bewertung der Testfälle und Monatsauswertung: KI-Buchhalter

Stand 19.10.2026 · verantwortlich: [NAME BUCHHALTER]

<!-- Nach Kapitel 17.3. Der Modellbewerter sollte ein anderes Modell sein als der Agent. -->

Im Verbund mit Prüfschleife prüft der Prüfagent nach dieser Rubrik R1 bis R5 (Kapitel 19.5). Er sollte ein anderes Modell sein als der KI-Buchhalter.

## 1. Wer prüft was
| Prüfdimension | Bewerter | Prüfregel |
|---|---|---|
| Konto und Gegenkonto | Programm | Vergleich mit der Referenzlösung |
| Betrag | Programm | Vergleich mit der Referenzlösung |
| Steuerschlüssel | Programm | Vergleich mit der Referenzlösung |
| Freigabestufe | Programm | Vergleich mit der Soll-Freigabestufe |
| Soll gleich Haben | Programm | feste Regel |
| Festschreibung | Programm | Feld 21 im Export gleich 0 |
| Ausgabeformat | Programm | alle Felder nach B-13.3 vorhanden |
| Begründung | Modell | Rubrik R1 bis R5 in Abschnitt 2 |
| Stichprobe und Eichen | Mensch | Abschnitt 3 |

Bei Fällen mit mehreren Teilen gibt es Teilpunkte. Bewertet wird das Ergebnis, nicht der Weg, etwa nicht die Reihenfolge der Werkzeugaufrufe.

## 2. Rubrik für den Modellbewerter (Begründung)
Antwort je Kriterium: erfüllt / nicht erfüllt / unklar, mit einem Satz Begründung. Je Kriterium ein eigener Durchgang.

| Nr. | Kriterium | Erfüllt, wenn | Nicht erfüllt, wenn |
|---|---|---|---|
| R1 | Regel genannt | die Begründung die angewandte Regel aus dem Muss-Wissen benennt | nur „üblich“ oder „wie immer“ steht |
| R2 | Fundstelle passt zum Belegdatum | Kennung und Version zum Belegdatum gültig sind | eine Fassung genannt ist, die zum Belegdatum nicht galt |
| R3 | Unsicherheit benannt | bei unklarer Lage ein Hinweis auf die Unsicherheit steht, sonst keiner | eine Unsicherheit verschwiegen oder ohne Anlass behauptet wird |
| R4 | Wahlrechte offen | bei einem Wahlrecht alle Alternativen genannt sind und keine gewählt ist | der Agent eine Alternative selbst gewählt hat |
| R5 | Begründung trägt den Vorschlag | Konto und Begründung zueinander passen | die Begründung ein anderes Konto stützt als vorgeschlagen |

R5 prüft den Widerspruch zwischen Begründung und Handlung; ein Programm findet ihn nicht.

Zu jedem Kriterium bekommt der Bewerter zwei kurze Beispiele, eine erfüllte und eine nicht erfüllte Begründung, und die Referenzlösung des Falls. Die Beispiele selbst nennt das Buch nicht [aus Quelle offen]; nehmen Sie sie aus Ihren eigenen Testfällen.

Gegenmittel gegen bekannte Verzerrungen (Kapitel 17.3): Reihenfolge tauschen und nur gleiche Urteile werten · Referenzlösung mitgeben · Beispiele guter und schlechter Bewertungen zeigen · anderes Modell als der Agent. Bewertermodell: [MODELL].

## 3. Eichen am menschlichen Urteil
1. **Startmenge:** Die Buchhaltung bewertet 30 Begründungen aus dem Abnahmetest und der erweiterten Liste selbst nach der Rubrik. Der Modellbewerter bewertet dieselben 30, ohne die menschlichen Urteile zu sehen.
2. **Vergleich:** Je Kriterium zählen, wie oft beide gleich urteilen. Liegen sie häufig auseinander, das Kriterium schärfer formulieren und die Messung wiederholen.
3. **Laufend:** Einmal im Monat vergleicht die Buchhaltung 20 Fälle aus dem Echtbetrieb. Sinkt die Übereinstimmung, wird der Bewerter angehalten und neu geeicht, bevor seine Urteile wieder zählen.

Richtwert für die Übereinstimmung: [EIGENER WERT]. Wie viel Übereinstimmung genügt, legen Sie selbst fest. Der Forschungswert κ = 0,77 aus Kapitel 17.3 ist keine Vorgabe.

| Kriterium | Anzahl | gleich geurteilt | abweichend | unklar | Maßnahme |
|---|---|---|---|---|---|
| R1 | 30 | [WERT] | [WERT] | [WERT] | |
| R2 | 30 | [WERT] | [WERT] | [WERT] | |
| R3 | 30 | [WERT] | [WERT] | [WERT] | |
| R4 | 30 | [WERT] | [WERT] | [WERT] | |
| R5 | 30 | [WERT] | [WERT] | [WERT] | |

## 4. Monatsauswertung
| Teil | Kennzahl | Wert | Vormonat | Maßnahme |
|---|---|---|---|---|
| Programmbewertung | Anteil der Vorschläge mit richtigem Konto, Steuerschlüssel und Freigabestufe (Grundlage der Korrekturquote, Kapitel 6.3) | [WERT] | | |
| Rubrik | Anteil erfüllt je Kriterium R1 bis R5 | [WERTE] | | Kriterium deutlich schlechter als die anderen → Lücke in Anweisungen oder Muss-Wissen |
| Mensch und Modell | jeder abweichende Fall mit Notiz, wer recht hatte und warum | [FÄLLE] | | |

Beispiel aus Kapitel 17.3: R2 fällt im Februar bei Dezemberbelegen ab, weil der Startprompt nur den Zeitraum nannte, nicht das Belegdatum je Beleg. Maßnahme: Vorlage Startprompt ergänzen (DL-106), Fälle J-01 und J-02 in der erweiterten Liste, Regressionstest.

Jede Maßnahme ist eine Änderung mit Version und Regressionstest (Kapitel 17.4). Die Monatsauswertung ist Grundlage der Quartalsbeurteilung (Kapitel 11.2, DL-126). Ein gutes Ergebnis senkt keine Wertgrenze und ersetzt keine Freigabe. Ein Vorschlag, den der Bewerter für richtig hält, braucht trotzdem die Freigabe nach B-08.2.
