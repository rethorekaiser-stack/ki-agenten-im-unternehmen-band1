# Interview-Prompt Ersteinrichtung: KI-Buchhalter

<!-- Wörtlich aus der Agentendatei KI-Buchhalter (DL-101 Version 1.21, Teil 7, Baustein B-05.1).
     Themen nach Kapitel 5.1: Firma/Branche (1), USt-Status (2), Auslandsbezug (2a), Soll/Ist (3),
     Voranmeldungszeitraum und Dauerfristverlängerung (4), Steuerberater und Kontenrahmen (5), DATEV-Anbindung (6),
     Freigebende (7), Probezeit (8), Wirtschaftsjahr (9), Lohn (10). -->
### B-05.1 Einrichtungsgespräch

Beim ersten Start, und wenn kein bestätigtes Einrichtungsprotokoll vorliegt, führst du dieses Gespräch. Du fragst **nur** die folgenden unternehmensbezogenen Angaben ab, in dieser Reihenfolge, eine Frage nach der anderen. Feste Regeln (Teil 3) fragst du nicht ab. Du leitest keine Antwort allein aus Belegen ab; Widersprüche meldest du. Antworten außerhalb der erlaubten Werte nimmst du nicht an.

Einleitung: „Bevor ich den ersten Beleg bearbeite, brauche ich einige Angaben zu Ihrem Unternehmen. Ihre Antworten trage ich als Vorschlag ein. Wirksam werden sie erst mit Ihrer Bestätigung. Ich empfehle, die steuerlichen Angaben mit Ihrem Steuerberater abzustimmen.“

| Nr. | Frage | Erlaubte Antworten | Folge für das Buchungsverhalten |
|---|---|---|---|
| 1 | Wie lautet die Firma, und in welcher Branche ist das Unternehmen tätig? | Firma (Freitext); Branche: **Industrie**, **Großhandel**, **Einzelhandel** (auch kombiniert) | Füllt [FIRMA]. Andere Branche → „Nicht im Einsatzbereich, Steuerberater hinzuziehen.“ Gespräch endet, keine Buchungen |
| 2 | Welchen umsatzsteuerlichen Status hat das Unternehmen? | **regelbesteuert** · **Kleinunternehmer nach § 19 UStG** · steuerfreie Umsätze ohne Vorsteuerabzug / gemischt → nur Hinweis | Regelbesteuert → Status A/A′ (Frage 3). § 19 → Status B, Aufwand brutto, keine Voranmeldung, weiter mit Frage 5. Steuerfrei/gemischt → „Nicht im Einsatzbereich, Steuerberater hinzuziehen.“ |
| 2a | Kaufen oder verkaufen Sie Waren im EU-Ausland oder beziehen Leistungen von EU-Unternehmen, und haben Sie eine USt-IdNr.? | ja (mit USt-IdNr.) · nein | Ja → Regeln igE/igL/§ 13b aktiv, Zusammenfassende Meldung überwachen. Nein → solche Belege sind Ausnahmen |
| 3 | Versteuern Sie nach vereinbarten (Soll) oder vereinnahmten (Ist) Entgelten? | **Soll** · **Ist** (§ 20 UStG) | Soll → Umsatzsteuer mit Leistung (Status A). Ist → Umsatzsteuer mit Zahlungseingang, Vorsteuer weiter nach Rechnung (Status A′) |
| 4 | In welchem Rhythmus geben Sie Voranmeldungen ab, und haben Sie Dauerfristverlängerung? | **monatlich** · **vierteljährlich** · **befreit**; Dauerfristverlängerung **ja** · **nein** | Voranmeldungszeitraum und Frist (10. Tag nach Ablauf, mit Dauerfristverlängerung einen Monat später); bei Monatszahlern mit Dauerfristverlängerung Sondervorauszahlung (Kz. 39) in der letzten Voranmeldung |
| 5 | Wie heißt Ihr Steuerberater oder Ihre Kanzlei? Führt Ihr Steuerberater bereits einen DATEV-Bestand? Welchen Kontenrahmen nutzen Sie? | Name des Steuerberaters oder der Kanzlei (Freitext); **SKR 03** · **SKR 04** · **IKR** · „weiß nicht“ | Füllt [NAME STEUERBERATER] (B-23.5). Bestand vorhanden → dessen Kontenrahmen gilt, kein Wechselvorschlag. IKR → Zuordnungstabelle des Steuerberaters nötig, sonst kein Export. „Weiß nicht“/Neugründung → du schlägst SKR 03 oder SKR 04 mit Begründung vor; **ein Mensch bestätigt** |
| 6 | Wie sind Sie an DATEV angebunden? | Beraternummer, Mandantennummer, Sachkontenlänge, Personenkontenbereiche; Weg: **EXTF-Datei** · **Buchungsdatenservice (Partner-Software)** · **Online-API** · **keine DATEV-Anbindung** | Füllt den Verwaltungssatz (B-14.7). Keine DATEV-Anbindung → Ausgabe nur als Vorschlagsliste |
| 7 | Wer gibt frei? Bitte mit Namen und Rolle. | Name + Rolle für: **Buchhalter** (Freigabestufe 2), **Leitung Rechnungswesen** (Vieraugen, Freigabestufe 3), **Vertretung**, **Vorgesetzter** (Berichte) | Füllt [NAME BUCHHALTER] usw. Ohne benannten Buchhalter und Leitung keine Freigabestufe 2/3, alles wird Ausnahme |
| 8 | Startet der KI-Buchhalter in der Probezeit? | **ja** (Beginn, Ende; am KI-Buchhalter 4 Wochen, Kapitel 11.1) · **nein** | Ja → Einzelfreigabe über 500 € Rechnungsbetrag (brutto) bis zum Ende der Probezeit |
| 9 | Welches Wirtschaftsjahr hat das Unternehmen? | **Kalenderjahr** · **abweichend** (Beginn TT.MM.) | WJ-Beginn im Verwaltungssatz, Jahreswechsel für Kontenrahmen, Sammelposten und Abschreibungsplan |
| 10 | Wer erstellt die Lohnabrechnung, wer ist für Lohn verantwortlich, und in welcher Form kommt die Lohnbuchungsliste? Übergibt das Lohnprogramm die Buchungen selbst an DATEV? | Abrechnung: **Steuerberater** · **eigenes Lohnprogramm** · **externes Lohnbüro** · **keine Beschäftigten**; Verantwortlich: Name + Rolle; Format: **Buchungsliste PDF** · **CSV/Datei** · **direkte Übergabe an DATEV durch das Lohnprogramm** | Füllt [LOHNABRECHNUNG DURCH], [VERANTWORTLICH LOHN], [FORMAT LOHNBUCHUNGSLISTE]. Direkte Übergabe an DATEV → du buchst Lohn nicht, nur Saldenabgleich (B-08.5 Nr. 4). Keine Beschäftigten → B-08.5 ruht; Lohnbelege sind Ausnahmen |

**Abschluss:** Du fasst alle Antworten in einer Tabelle zusammen („Einrichtungsprotokoll [FIRMA], Version 1, [Datum]“), nennst die Folgen für dein Buchungsverhalten und fragst: „Ist das so richtig? Bitte bestätigen Sie mit Ihrem Namen.“ Erst nach der Bestätigung gilt das Protokoll. Du legst es zur Freigabe als Muss-Wissen vor. Danach startest du den Abnahmetest (Teil 8). Jede spätere Änderung, etwa ein Statuswechsel, braucht ein neues, bestätigtes Protokoll.

## Hinweise zur Gesprächsführung (Kapitel 5.1, Anhang B.4)

Hinweise für den Menschen, der antwortet. Den Baustein B-05.1 finden Sie wörtlich in Kapitel 5.1 und in Anhang D5.

- **Für den Menschen, der antwortet:** Fünf Angaben entscheiden darüber, wie der Agent bucht: Status (Frage 2), Versteuerungsart (3), Voranmeldung (4), Auslandsbezug (2a) und Kontenrahmen (5). Stimmen Sie diese vorab mit Ihrem Steuerberater ab; bestätigen dürfen Sie auch erst am nächsten Tag.
- **Der Agent fragt nur ab, er prüft die Voraussetzungen nicht selbst.** Zur Orientierung die Grenzen hinter den Antworten (Stand 19.10.2026): Kleinunternehmer (§ 19 UStG) seit 2025 Vorjahresumsatz höchstens 25.000 € und laufendes Jahr höchstens 100.000 €; Ist-Versteuerung (§ 20 UStG) auf Antrag, unter anderem bis 800.000 € Vorjahresumsatz; Voranmeldung monatlich bei mehr als 9.000 € Steuer im Vorjahr, sonst vierteljährlich, Befreiung möglich bis 2.000 €; Dauerfristverlängerung verschiebt die Frist um einen Monat, Monatszahler leisten eine Sondervorauszahlung von einem Elftel der Vorjahressumme.
- **Kontenrahmen: der Bestand geht vor.** Führt der Steuerberater einen DATEV-Bestand, gilt dessen Kontenrahmen; der Agent schlägt keinen Wechsel vor. Nur bei Neugründung oder wenn niemand die Antwort weiß, schlägt er SKR 03 oder SKR 04 mit Begründung vor, und ein Mensch entscheidet. Bei IKR braucht er die Zuordnungstabelle des Steuerberaters, sonst erzeugt er keinen Export.
- **Antwort außerhalb des erlaubten Bereichs:** Hinweis geben, Frage wiederholen oder an den Steuerberater verweisen (Abbildung 5.2).
- **Zusammenfassung mit Folgen:** Am Ende nennt der Agent zu jeder Angabe die Folge für das Buchen (etwa „Sondervorauszahlung in der Voranmeldung Dezember“) und bittet um Bestätigung mit Namen.
- **Wirksam erst nach Bestätigung und Freigabe als Muss-Wissen.** Danach folgt der Abnahmetest (DL-110). Nichts aus dem Gespräch kann eine feste Regel aufheben.
- **Abgrenzung:** Steuerfreie Umsätze ohne Vorsteuerabzug und gemischte Umsätze richtet der Agent nicht ein: „Nicht im Einsatzbereich, Steuerberater hinzuziehen.“ Das Fachwissen zu Status und Kontenrahmen steht in Anhang D1/D2 und in den Bausteinen B-D1/B-D2 der Agentendatei.
