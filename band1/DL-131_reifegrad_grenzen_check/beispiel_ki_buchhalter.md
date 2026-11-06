# Reifegrad- und Grenzen-Check: KI-Buchhalter

[FIRMA] (Testmandant: Muster Technik GmbH) · Version der Agentendatei: 1.21 · geprüft von: [NAME VORGESETZTER] · Datum: [DATUM]

<!-- Grundlage: Kapitel 21.2, Bausteine B-03.1, B-03.3, B-21.2 und B-22.1. Testfälle zu den Grenzen aus Kapitel 22 stehen in DL-110. -->

## Begriffe: Reifegrad und Grad der Eigenständigkeit

Die beiden Begriffe sind nicht dasselbe (Kapitel 1.4 und 21.2, Glossar).

| Begriff | Bedeutung | gehört zu | wer legt fest |
|---|---|---|---|
| **Reifegrad** (Kapitel 21.2, B-21.2) | Einstufung einer Vorgangsart als „erprobt“ oder „in Erprobung“, geführt im Betriebsprotokoll. Beim Start steht jede Vorgangsart auf „in Erprobung“. Vorgangsarten in Erprobung gehen immer einzeln zur Freigabe. Über 10.000 € gilt weiter das Vieraugenprinzip. Der Reifegrad hält fest, wie verlässlich eine Vorgangsart im eigenen Haus schon läuft. | der Vorgangsart | ein Mensch im Betriebsprotokoll, anhand der Kennzahlen aus dem Laufbericht; der Agent ändert ihn nie |
| **Grad der Eigenständigkeit** (Kapitel 1.4, B-01.4) | einer von fünf Graden von „lenkt“ bis „beobachtet“. Der Grad legt je Handlung fest, was der Agent selbst tun darf. Der KI-Buchhalter arbeitet höchstens im Grad 4 „genehmigt“; Grad 5 ist ausgeschlossen. | der Handlung des Agenten | die Agentendatei; Änderung nur durch eine neue Version mit Eintrag in B-11.3 |

Dieser Prüfbogen führt nur den Reifegrad. Der Reifegrad entscheidet nur, ob die Vorschläge einer Vorgangsart einzeln zur Freigabe gehen; am Grad der Eigenständigkeit ändert ein Eintrag „erprobt“ nichts (Kapitel 21.2).

## Reifegrad je Vorgangsart (Kapitel 21.2, B-21.2)

Den Reifegrad führt ein Mensch im Betriebsprotokoll des Agenten ([ABLAGE BETRIEBSPROTOKOLL]), nicht im Einrichtungsprotokoll; im Einrichtungsgespräch (B-05.1) wird er nicht abgefragt. Beim Start steht jede Vorgangsart auf „in Erprobung“; erst ein Mensch trägt sie als „erprobt“ ein.

Schwelle für „erprobt“: [EIGENER WERT], etwa drei Monate und eine Korrekturquote unter 5 % (Beispielwert); dazu Abnahmetest in allen Durchläufen bestanden (B-17.4).

Je Vorgangsart eine Zeile im Betriebsprotokoll. Die Quoten sind Ihre eigenen Werte: Korrektur- und Ausnahmequote je Vorgangsart aus dem Laufbericht (B-03.3), die Rückfragequote je Vorgangsart aus Ihrer eigenen Zählung. Für die Rückfragequote zählen Sie die Ausnahmen mit Rückfrage nach B-22.1 („Angabe fehlt auf dem Beleg, Rückfrage.“ oder „Konto unklar, Rückfrage.“) und teilen sie durch die Zahl der Vorgänge.

Grundlage ist das Feld „Vorgangsart (B-03.1)“ im Protokolleintrag (B-16.3): Jeder Eintrag nennt die Vorgangsart, danach werten Sie die Quoten je Vorgangsart aus (Kapitel 21.2).

| Vorgangsart | Korrekturquote (Laufbericht, B-03.3) | Rückfragequote (eigene Zählung, B-22.1) | Ausnahmequote (Laufbericht, B-03.3) | Zeitraum | Reifegrad | Abnahmetest alle Durchläufe bestanden | eingetragen von, am |
|---|---|---|---|---|---|---|---|
| Eingangsrechnungen und sonstige Kostenbelege | [EIGENER WERT] | [EIGENER WERT] | [EIGENER WERT] | [EIGENER WERT] | in Erprobung (Start) | [ ] | [NAME VORGESETZTER], [DATUM] |
| Ausgangsrechnungen | [EIGENER WERT] | [EIGENER WERT] | [EIGENER WERT] | [EIGENER WERT] | in Erprobung (Start) | [ ] | [NAME VORGESETZTER], [DATUM] |
| Anlagenzugänge | [EIGENER WERT] | [EIGENER WERT] | [EIGENER WERT] | [EIGENER WERT] | in Erprobung (Start) | [ ] | [NAME VORGESETZTER], [DATUM] |
| je weitere freigegebene Vorgangsart (B-03.1) eine Zeile | | | | | in Erprobung (Start) | [ ] | |

Folge am Beispiel (Praxisbeispiel 21.2): Ein Hersteller startet mit allen Vorgangsarten „in Erprobung“. Nach drei Monaten trägt der Vorgesetzte im Betriebsprotokoll ein: Eingangsrechnungen und sonstige Kostenbelege erprobt, Anlagenzugänge und Ausgangsrechnungen weiter in Erprobung. Eine Rechnung über eine Prüfmaschine für 1.900 € läge in Freigabestufe 1. Weil Anlagenzugänge in Erprobung sind, legt der KI-Buchhalter sie trotzdem einzeln vor, mit Rechenweg zur Abschreibung und dem Vermerk „Vorgangsart in Erprobung“ (Testfall E-09 in DL-110).

- [ ] Jede Vorgangsart beginnt bei „in Erprobung“; eine Vorgangsart ohne Eintrag gilt als „in Erprobung“ (B-21.2).
- [ ] Vorschläge aus Vorgangsarten in Erprobung gehen einzeln zur Freigabe, auch bis 2.500 € (Freigabestufe 1). Über 10.000 € gilt weiter das Vieraugenprinzip.
- [ ] Den Reifegrad ändert nur ein Mensch; der Agent schreibt Hinweise mit den Zahlen aus dem Laufbericht an [NAME VORGESETZTER].
- [ ] Korrekturquote: wie oft ein Mensch einen Vorschlag ändert. Rückfragequote: wie oft der Agent eine Lücke meldet, statt einen Vorschlag zu machen; sie steht nicht im Laufbericht, Sie zählen die Ausnahmen mit Rückfrage nach B-22.1 („Angabe fehlt auf dem Beleg, Rückfrage.“ oder „Konto unklar, Rückfrage.“) und teilen sie durch die Zahl der Vorgänge. Ausnahmequote: wie oft Belege einer Vorgangsart gar nicht bearbeitet werden können.
- [ ] Eine niedrige Rückfragequote ist nur gut, wenn auch die Korrekturquote niedrig ist; sonst rät der Agent, statt zu fragen (22.1).
- [ ] Fallen die Rückfragen über Wochen auf null, genauer hinsehen (22.1).
- [ ] Steigt die Ausnahmequote nach einer Änderung, ist die Vorgangsart wieder in Erprobung, bis der Regressionstest bestanden ist (B-17.4).
- [ ] Stichprobe: Buchhalter prüft Vorschläge vollständig gegen den Beleg, etwa jeden zwanzigsten, ein anpassbarer Startwert.

**Zur Einordnung: vier Reifegrade nach Aufgabentyp** (redaktionelle Einschätzung, Stand Oktober 2026, kein Messergebnis, ersetzt nicht den Abnahmetest)

| Aufgabentyp | Reifegrad Oktober 2026 | Was das für den KI-Buchhalter heißt |
|---|---|---|
| Angaben aus Belegen auslesen, einordnen, zusammenfassen | weitgehend zuverlässig, mit Stichprobe | Pflichtangaben prüfen, Vorgangsart erkennen |
| Regel aus vorgegebenem Wissen anwenden | zuverlässig bei Standardfällen, eingeschränkt bei Sonderfällen | Kontierung mit Fundstelle, Sonderfälle ausführlich begründen (B-13.2) |
| Mehrstufige Abläufe über mehrere Systeme | eingeschränkt | kurze Abläufe, Prüfschritt, Freigabe (Kapitel 22.2) |
| Finanz- und Verwaltungsaufgaben ohne Aufsicht | nicht zuverlässig | keine eigenständige Buchung, keine Übermittlung |
| Entscheidungen über Menschen | nicht automatisieren | Mahnsperre, Kreditlimit, Lohn bleiben beim Menschen (Kapitel 23.1) |

## Ergebnis
[ ] Reifegrade im Betriebsprotokoll eingetragen (Datum, Name) [ ] offen: [PUNKTE, bis DATUM, verantwortlich]

Unterschrift: [NAME VORGESETZTER] ________
