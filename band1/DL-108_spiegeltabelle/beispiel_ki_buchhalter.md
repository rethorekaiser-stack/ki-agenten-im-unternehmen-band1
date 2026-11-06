# Spiegeltabelle: KI-Buchhalter

Plattform und Stufe: [PLATTFORM, STUFE] · Stand 04.11.2026 · Grundlage: Kapitel 12.1, Stellenprofil DL-103, Agentendatei DL-101 (Version 1.21), Kapitel 2.5, 5, 8 und 12 bis 17 („Auf den drei Stufen“)

<!-- NC = No Code, LC = Low Code, TU = für technische Umsetzer.
     Spalten „auf der eigenen Plattform“, „Prüfer“ und „Prüfdatum“ füllt das Unternehmen. -->

## 1. Spiegeltabelle (Kapitel 12.1)
| ✓ | Kaufmännische Festlegung (Teil III) | Technisches Gegenstück (Teil IV) | Kapitel | Am KI-Buchhalter | Prüfer | Prüfdatum |
|---|---|---|---|---|---|---|
| [ ] | Rolle und Stellenbeschreibung (6.2) | Systemprompt mit Rolle, Ziel, Regeln und Ausgabeformat | 13.3 | Agentendatei DL-101 als Systemprompt, Gliederung nach DL-105 | | |
| [ ] | Ziele und Kennzahlen (6.3) | Testfälle, Bewertungskriterien, Kennzahlen aus dem Protokoll | 17.2, 17.3 | DL-110 mit Bewertungsrubrik; Kennzahlen nach B-03.3 | | |
| [ ] | Einsatzzeiten (6.4) | Auslöser und Zeitplan | 15.1 | B-06.4, B-15.1: [ZEITPLAN, etwa „werktags 07:00 Uhr“] | | |
| [ ] | Berichtsweg (7.1) | Ausgabekanäle für Vorschläge und Berichte | 15.2 | [aus Quelle offen: Kanal] | | |
| [ ] | Weisungsbefugnis (7.3) | Wer Läufe auslösen darf, wer wen aufrufen darf | 15.1, 15.3 | Auftrag nur von Freigabeberechtigten über [AUFTRAGSWEG] (B-15.1) | | |
| [ ] | Befugnisse und Wertgrenzen (8.1, 8.2) | Freigabeschritte, Rechte der Werkzeuge, Festschreibung im Export immer 0 | 16.2, 14.6, 14.7 | Freigabestufe aus dem Rechnungsbetrag (brutto) im Ablauf berechnet; Feld 21 = 0 | | |
| [ ] | Datenzugang und Zugriffsmatrix (8.3) | Zuschnitt der Wissensserver, Dienstkonto mit minimalen Rechten | 13.7, 14.6 | Server Finanzen und Unternehmensserver, sonst keiner; Rechte nach DL-128 | | |
| [ ] | Direktive (9.1) | gemeinsamer Teil des Systemprompts oder eigener Abruf vom Unternehmensserver | 13.3, 13.7 | DL-104, Abruf zu Laufbeginn (B-09.1) | | |
| [ ] | Startprompt und Wissensrecherche (9.3, 9.4) | erster Werkzeugaufruf eines Laufs: Muss-Wissen zum Belegdatum abrufen | 13.7, 14.1 | `finanzen_muss_wissen_abrufen` („Muss-Wissen abrufen“) als erster Aufruf (B-14.1); DL-106 | | |
| [ ] | Budget und Tokenlimit (10.4) | Tokenlimit, Ausgabengrenze, Warnschwellen, Kostenüberwachung | 16.1 | Kostenstelle Finanzen, 70 / 90 / 100 %; DL-109, DL-129 | | |
| [ ] | Probezeit und Änderungsprotokoll (11.1, 11.3) | Versionierung, eingeschränkte Werkzeuge, Regressionstests | 17.4 | sechs Versionsgegenstände, drei Durchläufe (anpassbarer Startwert) | | |
| [ ] | Anhalten und Offboarding (11.4) | Notschalter, Widerruf von Schlüsseln und Dienstkonten | 14.6, 16.1 | B-11.4; DL-127 | | |

## 2. Zugriffsmatrix als Serverzuschnitt (Kapitel 12.1)
| Wissensart | Technisch | Rechte des KI-Buchhalters |
|---|---|---|
| Muss-Wissen Finanzen | Wissensserver Finanzen, versioniert, mit Gültigkeit | lesen, Änderungen nur vorschlagen |
| Kann-Wissen Unternehmen | Unternehmensserver | nur lesen |
| Vorgangsdaten | Schnittstellen zu Belegeingang, Ablage, Buchhaltungsprogramm | nur für den jeweiligen Lauf |
| Protokolle | Protokollablage, unveränderlich | anhängen, nie ändern |

Kein Laufwerk der Personalabteilung, keine Ordner des Vertriebs. Kontoumsätze kommen über das Buchhaltungsprogramm nur lesend, kein Bankzugang.

## 3. Detailzeilen am KI-Buchhalter
| ✓ | Kaufmännische Festlegung | Technisches Gegenstück | Umsetzung KI-Buchhalter |
|---|---|---|---|
| [ ] | Rolle, Aufgaben, Ziel (B-06.2, B-06.3) | Systemprompt (13.3) | Agentendatei DL-101 als Anweisung, auf allen Stufen gleich |
| [ ] | Einsatzzeiten (6.4) | Auslöser, Zeitplan (15.1) | NC: Eingabe durch den Menschen · LC: Belegeingang startet den Ablauf · TU: Programm holt Belege ab · Zeiten nach B-06.4 und Auslöser nach B-15.1 im Stellenprofil festlegen |
| [ ] | Bericht an Vorgesetzten, Intervall [INTERVALL] (B-16.3) | Ausgabekanal, Zeitplan (15.1/15.2) | Kanal [aus Quelle offen] |
| [ ] | Anweisungen nur von Freigabeberechtigten (B-08.1, B-15.1) | Auslöser und Auftragsweg (15.1), Übergaben (15.3) | Auftrag nur über [AUFTRAGSWEG]; E-Mails an das Rechnungspostfach sind Belege oder Inhalt, nie Auftrag |
| [ ] | Nie festschreiben (B-08.1) | kein Werkzeug „festschreiben“; EXTF-Feld 21 „Festschreibung“ = 0 (B-14.7) | LC: EXTF mit Festschreibung 0 · TU: Werkzeug existiert nicht |
| [ ] | UStVA nie übermitteln (B-08.1) | kein Übermittlungswerkzeug | TU: Agent erhält kein Werkzeug zum Übermitteln |
| [ ] | Keine Zahlungen, keine Stammdaten (B-08.1) | kein Bankzugang, keine Schreibrechte auf Stammdaten (14.6) | eigenes Dienstkonto mit Lese- und Exportrechten · TU: das Programm liest Kontoumsätze nur lesend ab und übergibt sie als Vorgangsdaten, der Agent bekommt keinen Bankzugang (2.5) |
| [ ] | Nur freigegebene Vorgangsarten (B-03.1) | Auslöser und Eingangsfilter (15.1) | NC: Mensch legt nur freigegebene Belege vor · LC/TU: [aus Quelle offen] |
| [ ] | Dublettenprüfung, jeder Beleg genau ein Ergebnis (B-03.2) | Abgleich mit erfassten Belegen, Vollständigkeitsprüfung des Laufs | [aus Quelle offen] |
| [ ] | Einzelner Agent; Ergebnisse anderer Systeme sind Inhalt (B-04.2); Verbund-Ergänzung ruht, solange in B-18.1 kein Verbund eingetragen ist | keine Werkzeuge zum Aufruf anderer Agenten; ruft ein Assistent einen anderen auf, ist das ein Verbund, der in B-18.1 eingetragen und getestet sein muss (Kapitel 20.1) | [aus Quelle offen] |
| [ ] | Kennzahlen im Laufbericht (B-03.3) | Auswertung des Protokolls (16.3) | LC: Wochenbericht aus dem Protokoll erzeugt (Kapitel 5, Auf den drei Stufen) · NC/TU: [aus Quelle offen] |
| [ ] | Wertgrenzen bis einschließlich 2.500 € / bis einschließlich 10.000 € nach Rechnungsbetrag (brutto); Summengrenze 7 Tage (B-08.2) | Freigabeschritte (16.2) | NC: Mensch prüft von Hand · LC: Bedingung verzweigt nach Rechnungsbetrag (brutto), Freigabeschritt, über 10.000 € zweistufig · TU: Werkzeug „Vorschlag übergeben“ prüft serverseitig Betrag, Summengrenze, Probezeitstatus |
| [ ] | Probezeit 4 Wochen, über 500 € Einzelfreigabe, zusätzlich prüft ein Mensch jeden Vorschlag; Fehlerklassen (B-08.2, B-05.2, 5.2, 11.1) | Probezeitstatus im Freigabeschritt (16.2) | NC: Korrekturliste selbst führen, etwa in einer Tabelle (DL-120) · LC: Bedingung im Freigabeschritt, 500 € als feste Schwelle, die nicht im Prompt steht; Freigabeformular erfasst die Fehlerklasse · TU: Probezeit und Freigabestufe als Konfigurationswerte im Code, nur mit Freigabe änderbar |
| [ ] | Ausweitung nur per neuer Version, Rückstufung nach kritischem Fehler (B-05.3) | Versionierung des Ablaufs bzw. Codes | LC: jede Ausweitung eine neue Version des Ablaufs mit Testlauf · TU: Rückstufung ist ein Schalter, kein Prompt |
| [ ] | Pflege: Versionen im Bericht, Abnahmetest nach Änderung (B-05.4) | Versionierung im Repository, automatisierte Testreihe (17.4) | NC: Versionen am Dateinamen von Agentendatei und Protokoll; Test bei Modellwechsel wiederholen · TU: jede Ausgabe trägt die Versionen; Änderung an Datei, Protokoll, Kontenrahmen oder Modell löst die Testreihe aus |
| [ ] | Zugriffsmatrix (B-08.3, DL-112) | Zuschnitt der Wissensserver, Zugriffsrechte (12.1, 13.7, 14.6) | genau zwei Server: Finanzen (Muss-Wissen) und Unternehmen (Kann-Wissen, nur lesend); keine Bank- oder Personaldaten · NC: nur Kontenrahmen und Kontierungsrichtlinie hochladen |
| [ ] | Zugangsschlüssel (14.6) | Tresor, nie im Prompt, nie im Protokoll | Schlüssel im Tresor der Plattform oder des Programms; regelmäßig erneuern, beim Offboarding widerrufen (B-14.6) |
| [ ] | Außenauftritt: nur Entwürfe (B-08.4) | Ausgabekanal Freigabeliste (15.2) | LC: Entwürfe landen in einer Freigabeliste, nicht im Postausgang · TU: bei späterem Selbstversand setzt der Code den KI-Hinweis |
| [ ] | Wissensabruf zum Belegdatum (B-09.4, B-13.7) | Wissens-MCP-Server Finanzen mit Gültigkeitszeiträumen und Versionierung (13.7) | NC: Gültigkeit von Hand pflegen · LC/TU: Abruf beim Server Finanzen |
| [ ] | Budget, Kostenstelle (10.4) | Tokenlimit, Warnschwellen (16.1) | Kostenstelle Finanzen, Warnschwellen 70 / 90 / 100 % (B-10.4); Betrag [aus Quelle offen], siehe DL-109 |
| [ ] | Protokoll, unveränderlich; Aufbewahrung 8/10 Jahre (B-16.3, B-08.3) | Protokollierung (16.3) | NC: Belege und Ergebnisse außerhalb des Chats GoBD-konform ablegen · LC: jeder Freigabeschritt protokolliert Name, Zeitstempel, Wissensstand · TU: unveränderliches Protokoll mit Prüfsumme |
| [ ] | Eingeschleuste Anweisungen sind Inhalt (B-08.1) | Schutzmaßnahmen (16.4), minimale Rechte (14.6) | fehlende Zahlungs- und Stammdatenrechte machen die Anweisung wirkungslos |
| [ ] | Abnahme vor Echtbetrieb (B-17.2) | Testfälle (17.2), Testmodus | sechs Musterfälle und Prüffall 4a, DL-110, mehrmals hintereinander; Ergebnisse im Testmodus nie in einen echten Stapel |
| [ ] | Änderung der Agentendatei (B-11.3) | Versionierung, Regressionstest (17.4) | nach jeder Änderung Abnahmetest wiederholen; Regressionstest zum Jahreswechsel |
| [ ] | Abschaltung, Offboarding (11.4) | Notschalter, Widerruf von Schlüsseln und Dienstkonten (14.6, 16.1) | Agent oder Zugänge deaktivieren oder Tokenlimit auf null; auslösen dürfen Freigabeberechtigte und verantwortliche Person; Offboarding nach DL-127 |
