# DL-113 DATEV-Beispielschnittstelle

| | |
|---|---|
| Kennung | DL-113 |
| Version | 1.11 |
| Stand | 05.11.2026 |
| Autor | Charlie Moore |
| Kapitelbezug | 14.4 Die Schnittstellen des KI-Buchhalters; 14.6 Zugangsdaten und Tresor; 14.7 DATEV-Anbindung auf drei Stufen; Bausteine B-14.6 und B-14.7 der Agentendatei Version 1.21 (DL-101) |
| Fundstellen im Buch | 14.6, 14.7 (Anhang B.3) |

DATEV ist eine eingetragene Marke der DATEV eG. Dieses Beispiel ist nicht von DATEV geprüft oder freigegeben.

## Zweck
Die Schritt-für-Schritt-Anleitung für alle drei Stufen der DATEV-Anbindung, eine Vorlage für den Verwaltungssatz, das EXTF-Beispiel aus Kapitel 14.7 als Datei und ein Programm, das den Stapel als CSV-Datei erzeugt (Programmskelett, Buchungsstapel als Vorschlag). Das Beispiel enthält Platzhalter; vor dem Einsatz passen Sie es an die aktuelle Formatbeschreibung von DATEV an. Es zeigt den Aufbau; es ist keine geprüfte Importdatei.

## Dateien
- `anleitung_drei_stufen.md` – die Schritte für No Code, Low Code und technische Umsetzer, Wortlaut aus Kapitel 14.7.
- `leervorlage_verwaltungssatz.md` – Vorlage für Verwaltungssatz, Spaltenüberschriften und eine Buchungszeile mit Platzhaltern nach B-14.7.
- `beispiel_ki_buchhalter.md` – das EXTF-Beispiel aus den Musterfällen 1 und 2 (SKR 03, gekürzt) aus Kapitel 14.7 mit Erläuterung; letztes Feld „KI-Buchhalter [VERSION]“, im Muster Agentendatei Version 1.21.
- `datev_schnittstelle_beispiel.py` – Programm, das den Stapel als CSV-Datei erzeugt (Programmskelett, nur Python-Standardbibliothek), Programmkopf Version 1.3. Es prüft Pflichtfelder, Datum, Betrag und BU-Schlüssel auf Automatikkonten und erzeugt einen Buchungsstapel als Vorschlag mit Feld 21 „Festschreibung“ 0, ohne Festschreibung. `python datev_schnittstelle_beispiel.py` gibt den Stapel aus den Musterfällen 1 und 2 aus (dieselben Zeilen wie in Kapitel 14.7) und die Fehlermeldung für einen BU-Schlüssel auf einem Automatikkonto.
- Skelett für Schritt 7 aus Kapitel 14.7 im selben Programm: Doppelversand-Sperre über die Prüfsumme, Übertragung, Rückmeldung „success“ und Protokoll (nur anhängen; Datei, Prüfsumme, Auftragskennung, Ergebnis, Freigebender). Die Übertragung ist standardmäßig aus (`UEBERTRAGUNG_AN = False`); dann läuft nur ein Probelauf ohne Versand, und das Programm baut keine Netzwerkverbindung auf. Schalten Sie die Übertragung ein, liest das Programm den Zugang erst zur Laufzeit mit `lies_geheimnis("DATEV_CLIENT_SECRET")` aus einer Umgebungsvariablen, die Ihr Tresor befüllt (Kapitel 14.6). Fehlt der Wert, bricht es ab, ohne etwas zu senden. Fehlermeldungen schwärzt es, bevor sie ins Protokoll gehen. Ohne Freigabe durch einen Menschen bricht es ab. Ohne „success“ gilt der Stapel als nicht übertragen (B-02.5). `python datev_schnittstelle_beispiel.py --selbsttest` prüft Beispielstapel, Probelauf, fehlende Freigabe, fehlende Bestätigung, Doppelversand, fehlendes Geheimnis und das Schwärzen in einem temporären Ordner; er setzt kein echtes Geheimnis voraus.

Die EXTF-Datei liegt nicht fertig bei, das Programm erzeugt sie: Ihre Zeilen haben unterschiedlich viele Felder und passen nicht zum Format der übrigen CSV-Vorlagen, und die Datei soll aus Ihren eigenen Daten entstehen.

## Zugang und Tresor (B-14.6)
- Im Programm steht nur der Name des Geheimnisses: `DATEV_CLIENT_SECRET`. Den Wert legen Sie im Tresor ab (No Code: Konnektor der Plattform; Low Code: Credentials bzw. Verbindungen; technisch: Key Vault, Secrets Manager, Secret Manager oder Vault) und geben ihn erst zur Laufzeit als Umgebungsvariable an das Programm.
- Für Versuche auf dem eigenen Rechner kopieren Sie `.env.example` aus dem Hauptordner nach `.env` und tragen dort Testwerte ein. `.env` steht in `.gitignore` und kommt nie ins Repository.
- Lag ein Schlüssel offen, widerrufen Sie ihn sofort, hinterlegen einen neuen und prüfen das Protokoll (Kapitel 14.6 „Wenn ein Schlüssel offen lag“).

## Feste Regeln (B-14.7)
- Feld 21 „Festschreibung“ ist immer 0; festgeschrieben wird von einem Menschen.
- Bei Automatikkonten (AV/AM) bleibt das Feld BU-Schlüssel leer.
- Die EXTF-Datei erzeugt ein festes Programm, nicht das Modell.
- Keine Doppelübertragung; bei API-Übertragung gilt nur das Ergebnis „success“ als übertragen.
- DATEV prüft nicht die fachliche Richtigkeit. Das bleibt beim Menschen und beim Steuerberater.

## Vollständige Kontenrahmen: offizieller Bezugsweg
Das Buch und dieser Download nennen nur die Konten, die in den Beispielen vorkommen. Die vollständigen Kontenpläne gibt DATEV heraus und stellt sie kostenlos als PDF bereit [PRÜFEN bis Drucklegung: Adressen und Dokumentnummern, weil DATEV sie jährlich ändern kann]:
- SKR 03 (Art.-Nr. 11174) und SKR 04 (Art.-Nr. 11175): DATEV-Hilfe-Dokument Nr. 0907817 „DATEV-Kontenrahmen 2026“, https://apps.datev.de/help-center/documents/0907817
- Steuerschlüssel-Tabellen 2026: Dok.-Nr. 0907055, https://apps.datev.de/help-center/documents/0907055
- Übersichtsseite zum Jahreswechsel: https://www.datev.de/web/de/berufsgruppenuebergreifend/service-und-support/wichtige-informationen-zum-jahreswechsel/jahreswechsel-rechnungswesen/anpassungen-in-den-programmen/DATEV-Kontenrahmen

Holen Sie jedes Jahr die Fassung des Belegjahres. Die Änderungen gegenüber dem Vorjahr stehen im Dok.-Nr. 0907108. DATEV kennzeichnet die PDFs als Eigenformular und untersagt den Nachdruck, auch auszugsweise; deshalb liegen sie diesem Repository nicht bei (Anhang D1).

Der Programmkopf verweist für die Steuerschlüssel auf die Dok.-Nr. 0907055 (Steuerschlüssel-Tabellen 2026, so im DATEV-Kontenrahmen 2026 genannt). [PRÜFEN bis Drucklegung]

## Anpassungshinweis
Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele. Eine Schnittstelle zu DATEV betreiben Sie erst, wenn Sie die aktuelle Formatbeschreibung geprüft, die Übertragung in der Testumgebung erprobt und die Einrichtung mit Ihrem Steuerberater abgestimmt haben (Kapitel 14.7, Anhang B.3). Formatversion, Spaltenüberschriften, Steuerschlüssel und die Behandlung des Skontos richten sich nach der aktuellen Formatbeschreibung bzw. Steuerschlüsseltabelle von DATEV. Sechs Prüfmarken im Programm sind offen: Steuerschlüsseltabelle und vollständiger Satzaufbau im Kopf, dazu Protokoll, Doppelversand-Sperre, Übertragung und Rückmeldung „success“ im Skelett für Schritt 7. Die Übertragung setzen Sie erst nach Onboarding, Tests in der Sandbox und Freigabe für Ihre Umgebung um.

## Version 1.0
- Platzhalter, gesperrt bis Freigabe, ohne Code und Beispieldateien (19.10.2026).

Anhang D4 zeigt dieselbe Belegnummer ER-2026-0815 mit dem Personenkonto 70001; Kap. 14.7 und DL-113 nutzen vereinfacht das Sammelkonto 1600.

## Änderungen in Version 1.1
- Sperre aufgehoben (Buch-Autor, 19.10.2026). Programmskelett aus der Vorlage des Buch-Autors übernommen (Quelle MD5 8B1245E4C58AC6DA5C08AFCBA5FC16D9) und an Kapitel 14.7 angeglichen: letztes Feld im Verwaltungssatz „KI-Buchhalter [VERSION]“ statt „KI-Buchhalter Beispiel“; Programmkopf mit Kennung, Version und Markenhinweis statt Herkunfts- und Bearbeitungsvermerken; Meldung „Prüfung und Import durch Mensch/Steuerberater“ statt „Mensch/Kanzlei“. Werkzeugnamen und Themenfeld zum Muss-Wissen enthält das Programm nicht. Anleitung, Leervorlage Verwaltungssatz und Beispiel neu. Programmlogik unverändert; py_compile und Beispiellauf bestanden (MD5 7D779412F45B7C481908561BDB6D9C41) (Zweiundzwanzigster Auftrag, 19.10.2026 22:02).

## Änderungen in Version 1.2
- Beispiellauf mit den Musterfällen 1 und 2 aus Kapitel 14.7 (ER-2026-0815 mit 5.950,00 € und Skonto 119,00 €, AR-2026-047 mit 29.750,00 €, Stapel „Buchungsvorschlaege Oktober 2026“); die Ausgabe stimmt Zeile für Zeile mit dem Buch überein, nur Feld 6 ist der Zeitpunkt des Laufs. Neu: Skelett für Schritt 7 (Doppelversand-Sperre, Übertragung standardmäßig aus, Rückmeldung „success“, Protokoll nach B-02.5), vier Prüfmarken, Selbsttest. Satz zur EXTF-Datei, die das Programm erzeugt. Beispiel auf Version 1.2. py_compile und Selbsttest auf der Box bestanden, PC und Box gleich (MD5 CACFF3A21E0E706053A27043647993D8) (Nachtrag zum Dreiundzwanzigsten Auftrag, Freigabe Buch-Autor, 19.10.2026 22:11).

## Änderungen in Version 1.3
- README nach Anhang B: „Programm, das den Stapel als CSV-Datei erzeugt“ in Zweck und Dateiliste; Markenhinweis mit „Dieses Beispiel“ unverändert. Programm unverändert (MD5 CACFF3A21E0E706053A27043647993D8) (Lektorat Runde 16, Kapitel 20, 19.10.2026 22:40).

## Änderungen in Version 1.4
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.5
- README: Hinweis auf Personenkonto 70001 in Anhang D4 und Sammelkonto 1600 in Kapitel 14.7 und DL-113 (in Anhang D4 und Kapitel 14.7 geprüft); Programm unverändert; Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.6
- Programm (Programmkopf Version 1.3): Zugang nur über den Namen `DATEV_CLIENT_SECRET`, Lesefunktion `lies_geheimnis` für Umgebungsvariablen aus dem Tresor, Abbruch ohne Versand bei fehlendem Wert, Schwärzen von Fehlermeldungen im Protokoll; Übertragung bleibt standardmäßig aus; Selbsttest um drei Prüfungen erweitert und bestanden. README: Abschnitte „Zugang und Tresor (B-14.6)“ und „Vollständige Kontenrahmen: offizieller Bezugsweg“ (DATEV-Dok.-Nr. 0907817, 0907055, 0907108, Übersichtsseite, je [PRÜFEN bis Drucklegung]); Hinweis zu Dok.-Nr. 0907055 (siehe CHANGELOG); Fundstelle 14.6; Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.7
- README, Beispiel und Leervorlage Verwaltungssatz: Bezug auf die Agentendatei auf Version 1.21 gehoben (DL-101, freigegeben am 04.11.2026 um 20:02 MEZ). Im Muster steht im letzten Feld damit Version 1.21. (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)

## Änderungen in Version 1.8
- README: Überblick Steuerschlüssel-Tabellen (N77; siehe CHANGELOG). (Neununddreißigster Auftrag, Lektorat Runde 30, 05.11.2026)

## Änderungen in Version 1.9
- Programmkopf und README: Steuerschlüssel siehe CHANGELOG (Runde 31/32; aktuell Dok.-Nr. 0907055). (Vierzigster Auftrag, Lektorat Runde 31, 05.11.2026)

## Änderungen in Version 1.11
- README-Historie bereinigt, Verweis auf CHANGELOG (N101) (Zweiundvierzigster Auftrag, Lektorat Runde 33, 05.11.2026)

## Änderungen in Version 1.10
- Steuerschlüssel-Tabellen 2026 = Dok.-Nr. 0907055; Prüfmarke am Programmkopf-Hinweis wiederhergestellt (N94). (Einundvierzigster Auftrag, Lektorat Runde 32, 05.11.2026)
