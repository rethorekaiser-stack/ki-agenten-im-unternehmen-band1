# Checkliste Tarif und Vertrag: KI-Buchhalter

Unternehmen: [FIRMA] · Anbieter und Tarif: [ANBIETER], Business-Tarif für zwei Nutzer · Stufe: No Code (Einstieg) · geprüft von: [NAME, ROLLE] · Datum: [DATUM]

<!-- Beispiel nach Kapitel 10.5. Anbieterbezogene Angaben trägt das Unternehmen ein; sie ändern sich häufig. -->

## 1. Tarif passt zur Stufe
| ✓ | Stufe | Tarif | Worauf achten | Ergebnis |
|---|---|---|---|---|
| [x] | No Code | Business-Tarif für zwei Nutzer, der übliche Einstieg für ein KMU | AVV, Trainingsausschluss, Projekte mit Anweisungen und Wissensdateien | [ERGEBNIS] |
| [x] | alle | kein Privattarif | Ein Test mit dem privaten Abo eines Mitarbeiters ist nicht zulässig: kein AVV, Training nicht ausgeschlossen. | [ERGEBNIS] |
| [ ] | alle | Anbindung eigener Wissensserver im Tarif enthalten | nötig für den Server Finanzen ab Low Code (Kapitel 13.7) | [ERGEBNIS] |

## 2. Vier Punkte im Vertrag
| ✓ | Punkt | Prüffrage | Nachweis | Ergebnis |
|---|---|---|---|---|
| [ ] | AVV nach Art. 28 DSGVO | Liegt ein AVV vor? Belege enthalten personenbezogene Daten, etwa Namen auf Rechnungen und Reisekostenabrechnungen. | [DOKUMENT, DATUM] | |
| [ ] | Datenhaltung und Verarbeitung | Speicherort und Verarbeitungsort in der EU? Einstellung, die eine Verarbeitung außerhalb der EU erlaubt, deaktiviert? | [EINSTELLUNG] | |
| [ ] | Drittlandtransfer | Anbieter im Verzeichnis des EU-US Data Privacy Framework; Datenhaltung in der EU gewählt, wo möglich; Stand C-703/25 P geprüft | [VERZEICHNIS, DATUM] | |
| [ ] | Ausschluss vom Modelltraining | vertraglich bestätigt | [DOKUMENT] | |

## 3. Zwei Punkte außerhalb des Vertrags
| ✓ | Punkt | Prüffrage | Ergebnis |
|---|---|---|---|
| [ ] | Protokolle nach GoBD | Ablage der Vorschlagslisten mit Datum und Freigabevermerk außerhalb des Chatverlaufs (Kapitel 16, No Code) | |
| [ ] | Abkündigung | Agentendatei (DL-101) ist plattformneutral; Umzug geplant für den Fall einer Abschaltung | |

## 4. Ausgabengrenze und Budget
| Angabe | Eintrag |
|---|---|
| Ausgabengrenze mit dem Anbieter vereinbart | [JA/NEIN, BETRAG] |
| Wer darf die Ausgabengrenze erhöhen | [NAME, ROLLE] [aus Quelle offen] |
| Budget je Monat und Kostenstelle | [BETRAG] € · Kostenstelle Finanzen (DL-109, B-10.4) |
| Warnschwellen | 70 % Warnung an den Vorgesetzten · 90 % nur beauftragte Läufe · 100 % Stopp (B-10.4) |

## 5. Datenhaltung je Plattform und Dienst
<!-- Freigegebene Dienste nach B-10.5 im Beispiel: Wissensserver Finanzen, Belegablage, Buchungsprogramm. -->
| Dienst | Speicherort | Verarbeitungsort | Einstellung, die dafür nötig ist | AVV | Training ausgeschlossen | geprüft am |
|---|---|---|---|---|---|---|
| Plattform des Assistenten (Business-Tarif) | [aus Quelle offen] | [aus Quelle offen] | [aus Quelle offen] | [ ] | [ ] | [DATUM] |
| Wissensserver Finanzen | [ORT] | [ORT] | | [ ] | [ ] | [DATUM] |
| Belegablage | [ORT] | [ORT] | | [ ] | [ ] | [DATUM] |
| Buchungsprogramm | [ORT] | [ORT] | | [ ] | [ ] | [DATUM] |

Andere Dienste, etwa Websuchen, Übersetzungs- oder Umwandlungsdienste, sind für den KI-Buchhalter nicht freigegeben (B-10.5).

## 6. Fragen an den Anbieter
1. Schließen Sie einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO für den Business-Tarif ab?
2. Wo werden unsere Belege gespeichert und wo verarbeitet, und welche Einstellung legt das fest?
3. Auf welcher Grundlage werden Daten in ein Drittland übertragen?
4. Ist vertraglich ausgeschlossen, dass unsere Belege zum Training verwendet werden?
5. Mit welcher Vorlaufzeit kündigen Sie Modelle und Werkzeuge ab, und können wir eine Ausgabengrenze vereinbaren?

## 7. Freigabe der Beschaffung
[ ] Datenschutz geprüft: [NAME, DATUM] · [ ] IT geprüft: [NAME, DATUM] · [ ] Vertrag geschlossen: [DATUM] · [ ] Kostenstelle Finanzen eingerichtet

Erst nach dieser Freigabe verarbeitet der KI-Buchhalter echte Belege; vorher nur anonymisierte Musterbelege. Der Wechsel auf Low Code oder die Stufe „Für technische Umsetzer“ ist eine neue Beschaffungsentscheidung mit eigener Prüfung.
