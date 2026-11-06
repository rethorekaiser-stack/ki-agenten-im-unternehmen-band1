# DL-113 Anleitung: DATEV-Anbindung auf drei Stufen

Version 1.1 · Stand 19.10.2026 · Wortlaut aus Kapitel 14.7 des Buchs. DATEV ist eine eingetragene Marke der DATEV eG. Dieses Beispiel ist nicht von DATEV geprüft oder freigegeben.

## Stufe No Code: Vorschlagsliste und Datei für Ihren Steuerberater

1. Klären Sie mit dem Steuerberater, ob er EXTF-Dateien annimmt und welche Angaben er braucht: Kontenrahmen, Sachkontenlänge, Berater- und Mandantennummer, Bereiche der Personenkonten.
2. Tragen Sie diese Angaben im Einrichtungsgespräch ein (Fragen 5 und 6). Sie stehen damit im Muss-Wissen.
3. Der Assistent erstellt je Monat eine Vorschlagsliste im Ausgabeformat und daraus einen Buchungsstapel als CSV-Datei mit Festschreibung 0.
4. Der Buchhalter prüft, korrigiert und gibt nach der Wertgrenzen-Staffel frei.
5. Der Steuerberater importiert die Datei, prüft und schreibt fest. Die Belege gehen auf dem bisherigen Weg an den Steuerberater.

Risiko auf dieser Stufe sind Formatfehler. Testen Sie den Import deshalb vorab mit den Musterfällen.

## Stufe Low Code: Buchungsstapel über Partnerprogramm und Buchungsdatenservice

1. Der Steuerberater bestellt den Buchungsdatenservice und schaltet ihn frei.
2. Das Unternehmen nutzt ein Programm, das bereits am Buchungsdatenservice angebunden ist, etwa eine Belegerfassung oder ein Rechnungsprogramm aus dem DATEV-Marktplatz.
3. Der Ablauf übergibt die freigegebenen Vorschläge des Agenten als EXTF-Buchungsstapel mit Verwaltungssatz an dieses Programm, über dessen Schnittstelle oder Import. Feld 21 „Festschreibung“ ist immer 0.
4. Das Partnerprogramm überträgt Buchungen und Belegbilder an DATEV, der Steuerberater übernimmt sie.
5. Die Rückmeldung, Erfolg oder Fehler, geht ins Protokoll des Agenten.

Der Vorteil dieser Stufe: Sie brauchen keine eigene Zulassung bei DATEV.

## Für technische Umsetzer: DATEV-Online-APIs

1. Registrierung im DATEV Developer Portal, Organisation und Anwendung anlegen, die Produkte für Mandantenliste, EXTF-Upload und Belegbilder abonnieren. Das schaltet die Testumgebung (Sandbox) frei.
2. Anmeldung über OAuth 2.0 gegen den DATEV-Login. Das Anmeldetoken liegt im Tresor, nicht im Prompt (Kapitel 14.6).
3. Die EXTF-Datei erzeugt ein **festes Programm**, nicht das Modell: Das Modell füllt ein Schema, das Programm prüft Konto, Gegenkonto, Datum und Betrag und setzt Feld 21 fest auf 0.
4. Tests in der Sandbox mit allen Musterfällen. Als übertragen gilt eine Datei erst, wenn die Abfrage des Auftrags das Ergebnis „success“ meldet; die Annahme der Datei allein ist keine Bestätigung. Die Schritte folgen der Beschreibung im DATEV Developer Portal, Stand Oktober 2026; maßgeblich ist die aktuelle Fassung dort.
5. Onboarding bei DATEV buchen (Paket „Consulting Onboarding DATEV Online-APIs“, Art.-Nr. 46051, 1.500 € zzgl. USt einmalig, mit vier Stunden Schnittstellenberatung; Ablauf in drei bis vier Terminen) und die technische Prüfung bestehen.
6. Der Steuerberater schaltet den Buchungsdatenservice für den Mandanten frei.
7. Im Betrieb: Doppelversand-Sperre über Prüfsumme und Auftragskennung, Protokoll nach GoBD mit Datei, Prüfsumme, Auftragskennung, Ergebnis und Freigebendem (Kapitel 16.3), Regressionstest bei jeder neuen Formatversion und jedem neuen Kontenrahmen (Kapitel 17.4).
