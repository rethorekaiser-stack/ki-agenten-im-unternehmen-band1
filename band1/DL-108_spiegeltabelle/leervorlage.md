# Spiegeltabelle: [NAME DES AGENTEN]

Plattform und Stufe: [PLATTFORM, STUFE] · Stand [DATUM] · geprüft von [NAME]

<!-- Kapitel 12.1: Jede kaufmännische Festlegung aus Teil III hat ein technisches Gegenstück aus Teil IV.
     Zeile für Zeile durchgehen: Wie sieht das Gegenstück auf Ihrer Plattform aus, wer setzt es durch (Mensch, Plattform, Code), wer hat es geprüft?
     Bleibt eine Zeile leer, ist die Festlegung nur eine Bitte. Bei Wertgrenzen, Festschreibung, Bankzugang und Datenzugang ist das nicht vertretbar. -->

## 1. Spiegeltabelle
| ✓ | Kaufmännische Festlegung (Teil III) | Technisches Gegenstück (Teil IV) | Kapitel | auf der eigenen Plattform | durchgesetzt von | Prüfer | Prüfdatum |
|---|---|---|---|---|---|---|---|
| [ ] | Rolle und Stellenbeschreibung (6.2) | Systemprompt mit Rolle, Ziel, Regeln und Ausgabeformat | 13.3 | | | | |
| [ ] | Ziele und Kennzahlen (6.3) | Testfälle, Bewertungskriterien, Kennzahlen aus dem Protokoll | 17.2, 17.3 | | | | |
| [ ] | Einsatzzeiten (6.4) | Auslöser und Zeitplan | 15.1 | | | | |
| [ ] | Berichtsweg (7.1) | Ausgabekanäle für Vorschläge und Berichte | 15.2 | | | | |
| [ ] | Weisungsbefugnis (7.3) | Wer Läufe auslösen darf, wer wen aufrufen darf | 15.1, 15.3 | | | | |
| [ ] | Befugnisse und Wertgrenzen (8.1, 8.2) | Freigabeschritte, Rechte der Werkzeuge, Festschreibung im Export immer 0 | 16.2, 14.6, 14.7 | | | | |
| [ ] | Datenzugang und Zugriffsmatrix (8.3) | Zuschnitt der Wissensserver, Dienstkonto mit minimalen Rechten | 13.7, 14.6 | | | | |
| [ ] | Direktive (9.1) | gemeinsamer Teil des Systemprompts oder eigener Abruf vom Unternehmensserver | 13.3, 13.7 | | | | |
| [ ] | Startprompt und Wissensrecherche (9.3, 9.4) | erster Werkzeugaufruf eines Laufs: Muss-Wissen zum Stichtag abrufen | 13.7, 14.1 | | | | |
| [ ] | Budget und Tokenlimit (10.4) | Tokenlimit, Ausgabengrenze, Warnschwellen, Kostenüberwachung | 16.1 | | | | |
| [ ] | Probezeit und Änderungsprotokoll (11.1, 11.3) | Versionierung, eingeschränkte Werkzeuge, Regressionstests | 17.4 | | | | |
| [ ] | Anhalten und Offboarding (11.4) | Notschalter, Widerruf von Schlüsseln und Dienstkonten | 14.6, 16.1 | | | | |
| [ ] | [WEITERE FESTLEGUNG] | | | | | | |

## 2. Zugriffsmatrix als Serverzuschnitt (12.1)
| Wissensart | Technisch | Rechte des Agenten | auf der eigenen Plattform | geprüft |
|---|---|---|---|---|
| Muss-Wissen [ABTEILUNG] | Wissensserver der Abteilung, versioniert, mit Gültigkeit | lesen, Änderungen nur vorschlagen | | [ ] |
| Kann-Wissen Unternehmen | Unternehmensserver | nur lesen | | [ ] |
| Vorgangsdaten | Schnittstellen zu [SYSTEME] | nur für den jeweiligen Lauf | | [ ] |
| Protokolle | Protokollablage, unveränderlich | anhängen, nie ändern | | [ ] |
| alles andere | – | kein Zugang | | [ ] |

## 3. Weitere Zeilen
| ✓ | Festlegung | Gegenstück | Kapitel | auf der eigenen Plattform | durchgesetzt von | Prüfer | Prüfdatum |
|---|---|---|---|---|---|---|---|
| [ ] | Außenauftritt, KI-Kennzeichnung | Ausgabekanäle, Freigabeliste | 15.2 | | | | |
| [ ] | Nachvollziehbarkeit | Protokollierung und Überwachung | 16.3 | | | | |
| [ ] | Schutz vor eingeschleusten Anweisungen | Schutzmaßnahmen | 16.4 | | | | |
| [ ] | Zugangsschlüssel | Tresor, nie im Prompt | 14.6 | | | | |
