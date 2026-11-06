# DL-901 Skelett eines Wissens-MCP-Servers, bandübergreifend

| | |
|---|---|
| Kennung | DL-901 (vormals DL-010) |
| Version | 1.9 |
| Stand | 03.11.2026 |
| Kapitelbezug | Band 1: 13.7 Wissens-MCP-Server je Abteilung (Gültigkeit zum Belegdatum, Versionierung, Prüfsumme, Freigabeweg, Werkzeuge des Servers); 13.5; 13.6; 14.2 MCP; 14.5 Werkzeuge gut beschreiben; 14.6 Zugangsdaten und Tresor; bandübergreifend |
| Fundstellen im Buch | Einleitung, 13.7, 13.8, 14.6 (Anhang B.3) |

## Zweck
Ausgangspunkt für einen Abteilungsserver mit Muss-Wissen, am Beispiel des Servers Finanzen des KI-Buchhalters. Das Skelett zeigt die Kernfrage aus Kapitel 13.7: Was galt an diesem Tag? Jedes Wissensstück trägt Version, gültig ab, gültig bis und Prüfsumme. Der Server liefert nur freigegebene Wissensstücke, die zum Belegdatum gelten, und bietet die drei Werkzeuge aus 13.7 an:

| Werkzeug | Eingabe | Rückgabe |
|---|---|---|
| `finanzen_muss_wissen_abrufen` („Muss-Wissen abrufen“) | Belegdatum, Themen | gültige Wissensstücke mit Version, gültig ab/bis, Prüfsumme; bei fehlendem Wissen der Hinweis, eine Ausnahme zu melden |
| `finanzen_kontierungsregel_suchen` | Belegdatum, Lieferant, Beschreibung | Regel, Konto, Gültigkeit, Fundstelle, Version; bei keinem Treffer die Aufforderung, eine Ausnahme zu melden |
| `finanzen_aenderung_vorschlagen` | Wissensstück, Vorschlag, Begründung, Beispielbelege | Kennung des Vorschlags; keine Änderung am Server |

## Dateien
| Datei | Inhalt |
|---|---|
| `mcp_wissensserver_skelett.py` | Skelett in Python (nur Standardbibliothek; MCP-Anbindung optional über ein MCP-SDK). Selbsttest: `python mcp_wissensserver_skelett.py --selbsttest` |
| `leervorlage_wissensstuecke.csv` | leere Tabelle der Wissensstücke (Spalten wie im Skelett) |
| `beispiel_ki_buchhalter_wissensstuecke.csv` | Muss-Wissen Finanzen mit den Beispielen aus Kapitel 13.7; der Kontenrahmen 2027 ist noch nicht freigegeben und wird deshalb nicht ausgeliefert |

CSV: UTF-8 mit BOM, Semikolon. Datumsangaben TT.MM.JJJJ. Wissensstücke mit Platzhalter im Datum werden nicht ausgeliefert.

## Stand und Lücken
Das Skelett ist ein Lehrbeispiel, kein Produktivsystem. Nicht enthalten: Anmeldung und Rechteprüfung je Dienstkonto (vorbereitet ist nur der Schalter `ANMELDUNG_AN`, standardmäßig aus, und das Lesen des Zugangs `WISSENSSERVER_ZUGANG` über `lies_geheimnis` aus einer Umgebungsvariablen, die Ihr Tresor befüllt; Kapitel 14.6), Verschlüsselung, dauerhafte Ablage der Änderungsvorschläge, Volltext- oder Vektorsuche. Die Anbindung an ein MCP-SDK ist nicht gegen eine bestimmte SDK-Version getestet [PRÜFEN]. Der Selbsttest läuft ohne SDK. Inhalte der Wissensstücke (Kontenrahmen, Einrichtungsprotokoll, Abschnitt der Kontierungsrichtlinie) sind Platzhalter [aus Quelle offen].

## Anpassungshinweis
Zugangsschlüssel nie im Code oder Prompt ablegen, sondern im Tresor (Kapitel 14.6). Jeder Agent bekommt nur den Server seiner Abteilung und den Unternehmensserver. Neue Versionen gehen erst nach Freigabe durch einen Menschen online, alte Versionen bleiben für ältere Belege erhalten. Werkzeugbeschreibungen sind Anweisungen: nach jeder Änderung Regressionstest (Kapitel 17.4, DL-128).

Änderung gegenüber Version 1.0: lauffähiges Skelett mit Gültigkeitsfilter, Versionierung, Prüfsumme, Freigabevermerk und den drei Werkzeugen aus Kapitel 13.7; Leervorlage und Beispiel der Wissensstücke ergänzt. Der bisherige Inhalt steht als Kommentar im Dateikopf.

## Änderungen in Version 1.2
- Titel nach Anhang B.3 (vorher: „Minimaler Wissens-MCP-Server (Skelett)“).

## Änderungen in Version 1.3
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.4
- Lizenzzeile mit Namensnennung im Programmkopf ergänzt, Programmkopf auf Version 1.2 (Entscheidungen Thore 19.10.2026, 11:06). Programmlogik unverändert, Selbsttest bestanden.

## Änderungen in Version 1.5
- Programmkopf (Version 1.3): Lizenzzeile auf die eigene Lizenz umgestellt, mit Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ (Umentscheidung Lizenz 11:21). Programmlogik unverändert, Selbsttest bestanden.

## Änderungen in Version 1.6
- Beispiel-Wissensstück W08 (E-Rechnung, § 27 Abs. 38 UStG): Prüfmarke zum Beginn der Gültigkeit entfernt, gültig ab 01.01.2025 bestätigt (Kapitel 3.1, Entscheidung des Buch-Autors 11:39); Inhalt im Wortlaut an Agentendatei B-D2 angeglichen. Programm unverändert, Selbsttest auf der Box bestanden.

## Änderungen in Version 1.7
- Beispiel-Wissensstück W08 (§ 27 Abs. 38 UStG): gültig bis 31.12.2027 statt 31.12.2026, weiter ein einziges Stück; der Inhalt nennt bereits beide Stufen nach Agentendatei B-D2 und Kapitel 3.1 (Entscheidung des Buch-Autors 11:40). Programm unverändert, Selbsttest auf der Box bestanden.

## Änderungen in Version 1.8
- Anzeigename „Muss-Wissen abrufen“ in README, Kommentar und Werkzeugbeschreibung (Docstring); Werkzeugname finanzen_muss_wissen_abrufen unverändert. Wissensstück W05: Freigabestufe. Selbsttest bestanden, Ausgabe unverändert (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.9
- Programm (Programmkopf Version 1.4): Schalter `ANMELDUNG_AN` (standardmäßig aus) und Name `WISSENSSERVER_ZUGANG`; Lesefunktion `lies_geheimnis` mit `GeheimnisFehlt`, der Wert wird nie ausgegeben; Selbsttest prüft das Lesen ohne echtes Geheimnis und ist bestanden. README: Kapitelbezug und Fundstelle 14.6 (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).
