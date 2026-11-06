# Offboarding-Checkliste: KI-Buchhalter

Anlass: [x] Wechsel der Plattform, weil das bisherige Werkzeug abgekündigt wird · letzte Version der Agentendatei: 1.5 · verantwortlich: [NAME VERANTWORTLICH, ROLLE] · geplanter Stopp: [DATUM]

<!-- Beispiel nach Kapitel 11.4 (Praxisbeispiel Umzug). Zuständigkeiten ohne Quelle sind als Platzhalter gesetzt. -->

## A. Notabschaltung vorbereiten (vor dem Echtbetrieb)
| ✓ | Punkt | Eintrag |
|---|---|---|
| [x] | Wer darf den Stopp auslösen | die Freigabeberechtigten und die verantwortliche Person (Kapitel 7.2, B-11.4) |
| [x] | Wie wird gestoppt | [x] Agent deaktivieren [x] Dienstkonto sperren [x] Tokenlimit auf null (Kapitel 10.4, 14.6) |
| [ ] | Notschalter getestet am | [DATUM] (Kapitel 16.1) |

Nach einem Stopp macht der Agent keinen Vorschlag und keinen Werkzeugaufruf mehr und legt nur die Liste der offenen Belege und Ausnahmen vor (B-11.4).

## B. Geordnetes Offboarding in fünf Schritten
| ✓ | Schritt | Inhalt | zuständig | erledigt am | Nachweis |
|---|---|---|---|---|---|
| [ ] | 1 Offene Arbeit übergeben | Übergabebericht des Agenten nach B-11.4: offene Belege und Ausnahmen (im Praxisbeispiel 14 offene Belege), wiederkehrende Fälle, Versionen von Agentendatei, Einrichtungsprotokoll und Muss-Wissen | Buchhalter oder Nachfolger übernimmt | [DATUM] | Übergabebericht |
| [ ] | 2 Zugänge entziehen | Belegablage, Wissensserver Finanzen und Unternehmensserver, Buchungsprogramm, Kontoumsätze; Schlüssel für Schnittstellen im Tresor widerrufen; Dienstkonto sperren; Konten bei der Plattform | IT [NAME] | am Tag des Stopps | [NACHWEIS] |
| [ ] | 3 Archivieren | Protokolle, Agentendatei mit allen Versionen, Einrichtungsprotokoll, Wissensstand (Versionen und Prüfsummen des Muss-Wissens) | [NAME] | [DATUM] | Archiv der Buchhaltung |
| [ ] | 4 Aufbewahren | Protokolle so lange wie die Buchungen, die auf den Vorschlägen beruhen; nicht mit dem Agenten löschen. Fristen nach § 147 Abs. 3 AO (Kapitel 16.3); Laufprotokolle 10 Jahre. Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrem Steuerberater ab. | [VERANTWORTLICH AUFBEWAHRUNG] | [DATUM] | |
| [ ] | 5 Abmelden | Lizenzen kündigen, Kostenstelle Finanzen schließen, Verfahrensdokumentation fortschreiben (DL-111), Eintrag in B-11.3 „außer Betrieb seit [DATUM]“ | [NAME VORGESETZTER] | [DATUM] | |

## C. Nachfolge
| ✓ | Punkt | Eintrag |
|---|---|---|
| [ ] | Nachfolger übernimmt offene Belege | neuer KI-Buchhalter auf der neuen Plattform, offene Belege zunächst beim Buchhalter |
| [ ] | Nachfolge-Agent mit derselben Agentendatei als neuer Version, eigenem Einrichtungsgespräch, Abnahmetest (DL-110) und verkürzter Probezeit | [DATUM] |

Das Protokoll des alten Agenten bleibt unverändert (B-16.3).

Abschluss: [NAME VERANTWORTLICH, ROLLE], Datum: [DATUM], Unterschrift: ________
