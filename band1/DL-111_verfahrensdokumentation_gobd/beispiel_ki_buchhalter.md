# Verfahrensdokumentation: Einsatz des KI-Buchhalters in der Buchführung von [FIRMA]

Version 1.2 · Stand 19.10.2026 · verantwortlich: [NAME, ROLLE] · Aufbewahrung: 10 Jahre (§ 147 Abs. 3 AO)

<!-- Muster-Verfahrensdokumentation nach GoBD (DL-111). Gliederung nach Kapitel 16.3, ergänzt nach Kapitel 21.2 und 23. Baustein-IDs verweisen auf die Agentendatei DL-101 (Version 1.21). -->

## 1. Aufgabe
- **Unternehmen:** [FIRMA], Deutschland, Industrie / Großhandel / Einzelhandel; USt-Status und Kontenrahmen laut bestätigtem Einrichtungsprotokoll (B-05.1).
- **Zweck:** Der KI-Buchhalter (KI-System) prüft Belege, schlägt Buchungssätze vor, rechnet Abschreibungen und UStVA-Kennzahlen vor, erfasst die Lohnbuchungsliste als Vorschlag, gleicht Zahlungen mit offenen Posten ab und stellt DATEV-Buchungsstapel bereit (acht Aufgaben nach B-06.2). Er bearbeitet nur sieben freigegebene Vorgangsarten, darunter den Abgleich von Zahlungen anhand von Kontoauszügen oder Kontoumsätzen, die ihm nur lesend vorliegen (B-03.1).
- **Rollen:** Vorgesetzter [NAME VORGESETZTER]; Buchhalter [NAME BUCHHALTER] (Freigabestufe 2, Festschreibung); Leitung Rechnungswesen [NAME] (Freigabestufe 3); Vertretung [NAME VERTRETUNG]; Lohn [VERANTWORTLICH LOHN]; Aufbewahrung [VERANTWORTLICH AUFBEWAHRUNG]; verantwortliche Person für Sicherheitsvorfälle [NAME VERANTWORTLICH, ROLLE] (B-16.4).
- **Abgrenzung:** Der Agent schreibt nie fest, übermittelt keine Voranmeldung, übt keine Wahlrechte aus, löst keine Zahlungen aus, ändert keine Stammdaten, rechnet keinen Lohn und bucht nicht für Dritte (B-08.1, B-08.5).
- **Personenbezogene Daten und ausgeschlossene Zwecke:** Daten auf Belegen nur für den jeweiligen Vorschlag, keine Entscheidung über Personen, Auskunftsersuchen an [NAME DATENSCHUTZ, ROLLE] (B-23.1); keine Bewertung von Kreditwürdigkeit, Leistung oder Verhalten von Menschen (B-23.2). Prüfliste Rechtsrahmen: DL-132.
- **Keine Steuerberatung:** Hinweissatz für Berichte und Verfahrensdokumentation (B-23.5): „Das sind Vorschläge, keine Steuer- oder Rechtsberatung. Verantwortlich für Buchführung, Voranmeldung und Aufbewahrung bleibt [FIRMA].“
- **Ablauf je Lauf:**
  1. **Auslöser und Auftrag:** Zeitplan, Ereignis oder Auftrag einer freigabeberechtigten Person; Startprompt mit vier Angaben (B-15.1, B-09.3).
  2. **Arbeitsbeginn:** Abruf der Direktive und des Muss-Wissens Finanzen, gültig zum Belegdatum; ohne bestätigtes Einrichtungsprotokoll kein Vorschlag (B-09.1, B-09.4).
  3. **Beleg prüfen:** Vorgangsart freigegeben (B-03.1); Dublettenprüfung, jeder Beleg endet in genau einem Ergebnis (B-03.2); Pflichtangaben, Prüfschema Umsatzsteuer (B-D2); Arbeitsschleife mit höchstens einem neuen Anlauf, sonst Ausnahme (B-01.3).
  4. **Vorschlag:** Buchungssatz im festen Format mit Regel, Kontenrahmen-Version und Wissensstand (B-13.3), Selbstprüfung vor der Ausgabe (B-17.3).
  5. **Übergabe:** EXTF-Buchungsstapel, Festschreibung 0, keine Doppelübertragung (B-14.7). Weg: [DATEV-WEG].

## 2. Systeme
- **Plattform / Ausbaustufe:** [aus Quelle offen – je Unternehmen festlegen]
- **Anweisungen:** Direktive Version [X.Y] (DL-104); Agentendatei KI-Buchhalter, Version [X.Y], Änderungsprotokoll B-11.3.
- **Modell und Einstellungen:** [MODELL, VERSION] (Kapitel 13.1 und 13.2)
- **Wissen:** Wissensserver Finanzen (Muss-Wissen; jedes Wissensstück mit Version, gültig ab, gültig bis und Prüfsumme; Änderungen nur nach menschlicher Freigabe) und Unternehmensserver (Kann-Wissen, nur lesend) (B-08.3, B-13.7, DL-901).
- **Werkzeuge und Schnittstellen:** Werkzeugliste nach DL-128; DATEV-Export laut B-14.7; Beraternummer [BERATERNUMMER], Mandantennummer [MANDANTENNUMMER], Sachkontenlänge [SACHKONTENLÄNGE].
- **Dienstkonto und Zugriffsrechte:** eigenes Dienstkonto mit minimalen Rechten nach Kapitel 14.6, kein Bankzugang (Kontoumsätze nur lesend aus dem Buchhaltungsprogramm), keine Lohn- und Personaldaten Einzelner; Zugriffsmatrix DL-112. Schlüssel im Tresor, nie im Prompt (B-14.6).
- **Verschlüsselung:** auf dem Übertragungsweg zwischen Agent, Wissensservern, Ablage und DATEV und in Ablage, Protokoll und Status (Art. 32 DSGVO, Kapitel 16.4).

## 3. Freigaben
- **Staffel (Bezugsgröße Rechnungsbetrag (brutto)):** bis einschließlich 2.500 € Stapel ohne Einzelfreigabe · über 2.500 € bis einschließlich 10.000 € Buchhalter · über 10.000 € Buchhalter und Leitung · Probezeit über 500 € Einzelfreigabe, zusätzlich prüft ein Mensch jeden Vorschlag · UStVA immer · Lohn immer einzeln, mindestens Freigabestufe 2 (B-08.2, B-08.5). Der Grenzbetrag gehört zur unteren Freigabestufe.
- **Reifegrad je Vorgangsart (B-21.2):** Vorschläge aus Vorgangsarten „in Erprobung“ oder ohne Eintrag gehen einzeln zur Freigabe, unabhängig von der Staffel, mit dem Vermerk „Vorgangsart in Erprobung“. Über 10.000 € gilt weiter das Vieraugenprinzip. Den Reifegrad trägt nur ein Mensch ein, im Betriebsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“ (DL-131).
- **Freigabeschritt:** Die Freigabestufe berechnet der Ablauf aus dem Rechnungsbetrag (brutto) und der Summengrenze je Lieferant; bei Abweichung gilt die höhere. Freigabe zählt nur in [FREIGABEKANAL] mit Name und Zeitpunkt; Freigabestufe 3 braucht zwei verschiedene Personen (B-16.2, Kapitel 16.2).
- **Festschreibung und Übermittlung:** ausschließlich durch den Buchhalter oder den Steuerberater.
- **Ausnahmen:** Gründe und Form nach B-07.4; Sicherheitsvorfälle nach B-16.4.

## 4. Kontrollen
| Kontrolle | Wer | Wann | Nachweis |
|---|---|---|---|
| Sichtung Buchungsstapel, Festschreibung | Buchhalter | je Stapel | Protokoll, Festschreibung in der Buchhaltungssoftware |
| Einzelfreigabe Freigabestufe 2 | Buchhalter | je Beleg | Name und Zeitpunkt im Protokoll |
| Vieraugenfreigabe Freigabestufe 3 | Buchhalter und Leitung Rechnungswesen | je Beleg | beide Namen und Zeitpunkte |
| UStVA-Entwurf prüfen und übermitteln | [NAME] | je Voranmeldungszeitraum | Freigabe, Übermittlungsbeleg |
| Summengrenze je Lieferant (7 Kalendertage) | Ablauf berechnet, Mensch prüft | laufend | Bericht |
| Abnahmetest | Buchhalter | nach Einrichtung und jeder Änderung | Abnahmeprotokoll DL-110 |
| Regressionstest, drei Durchläufe (anpassbarer Startwert) | Buchhalter | nach jeder Änderung an einem der sechs Versionsgegenstände (Kapitel 17.4) | Ergebnisbericht je Fall und Durchlauf (B-17.4) |
| Stichprobe freigegebener Vorschläge, Eichen des Modellbewerters | Buchhalter | monatlich, 20 Vorschläge (Startwert, anpassbar) | Monatsauswertung DL-110 |
| Auswertung des Protokolls, Sofort-Signale | [NAME] | [RHYTHMUS] | Regelverstoß, Anstieg der Ausnahmen oder Korrekturen, Verbrauch ohne mehr Belege (Kapitel 16.3) |
| Beurteilung anhand der Kennzahlen | Vorgesetzter | vierteljährlich | Beurteilungsbogen DL-126 |
| Reifegrad je Vorgangsart (Korrektur-, Rückfrage-, Ausnahmequote) | Vorgesetzter | [RHYTHMUS] | Reifegrad- und Grenzen-Check DL-131, Eintrag im Betriebsprotokoll mit Datum und Namen |

- **Probezeit:** Vermerk „Probezeit“ je Vorschlag; Korrekturen mit Fehlerklasse kritisch / wesentlich / formal und Grund; Wochenbericht; Ende nur durch schriftliche Entscheidung (B-05.2, DL-120).
- **Änderungen:** nur in der Agentendatei mit Eintrag im Änderungsprotokoll (B-11.3); Ausweitung nur per neuer Version (B-05.3, DL-121). Pflegerhythmus: DL-122.
- **Leitplanken:** Grenzen je Lauf, Freigabeschritt, Schutzmaßnahmen nach DL-129.
- **Notabschaltung und Außerbetriebnahme:** Notschalter; auslösen dürfen die Freigabeberechtigten und die verantwortliche Person (B-11.4); Offboarding nach DL-127.

## 5. Protokoll
- **Je Lauf und je Vorschlag:** Lauf-Nummer, Zeitstempel und Auslöser; Versionen von Agentendatei, Einrichtungsprotokoll, Muss-Wissen und Modell; Beleg mit Fundort und geprüftem OCR- oder XML-Ergebnis; Vorgangsart (B-03.1); Vorschlag mit Regel, Fundstelle und Kontenrahmen-Version; Freigabestufe und Freigabe mit Name und Zeitpunkt; Ausnahmen, abgelehnte Bitten und Wissenslücken; bei Export Datei, Prüfsumme und Übertragungsergebnis (B-16.3, Kapitel 16.3).
- **Unveränderbarkeit:** Einträge werden nie geändert; Korrekturen als neuer Eintrag (§ 146 Abs. 4 AO).
- **Keine Einzeldaten:** keine personenbezogenen Einzeldaten aus der Lohnabrechnung (B-08.5).
- **Ablageort:** [aus Quelle offen]
- **Berichte und Kennzahlen:** Laufbericht mit Belegen, Vorschlägen je Freigabestufe, Ausnahme-, Übernahme- und Korrekturquote, Regelverstößen, Laufzeit und Verbrauch sowie den verwendeten Versionen (B-03.3, B-05.4); monatliche Kostenübersicht (B-10.6).

## 6. Aufbewahrung
- **Fristen (§ 147 Abs. 3 AO):** Buchungsbelege 8 Jahre (seit 01.01.2025); Bücher, Jahresabschlüsse, Arbeitsanweisungen und Organisationsunterlagen 10 Jahre; sonstige steuerlich relevante Unterlagen 6 Jahre. Laufprotokolle des Agenten als Teil der Verfahrensdokumentation 10 Jahre (B-08.3). Beispiel. Stimmen Sie die Einordnung für Ihr Unternehmen mit Ihrem Steuerberater ab.
- **E-Rechnungen und OCR:** Bei einer E-Rechnung genügt die Aufbewahrung des strukturierten Teils; Ergebnisse einer Texterkennung sind nach ihrer Prüfung aufzubewahren (BMF-Schreiben vom 14.07.2025, Rz. 118, 119, 131).
- **Außerbetriebnahme:** Protokolle bleiben aufbewahrungspflichtig und werden nicht mit dem Agenten gelöscht (Kapitel 11.4).
- **Agent und Unternehmen:** Der Agent protokolliert, das Unternehmen bewahrt auf. Ein Chatverlauf in einer Plattform ist kein Archiv; unveränderbare Ablage, vollständige Aufbewahrung und lesbare Ausgabe bei einer Betriebsprüfung stellt das Unternehmen sicher (Kapitel 23.4, DL-132 Teil 4).
- **Datensicherung:** [aus Quelle offen]

## Änderungshistorie
| Version | Datum | Änderung | Verantwortlich |
|---|---|---|---|
| 1.0 | [DATUM] | Erstfassung nach Muster aus Band 1 | [NAME, ROLLE] |
