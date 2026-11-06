# DL-133 Laufzeit-Messbogen

| | |
|---|---|
| Kennung | DL-133 |
| Version | 1.11 |
| Stand | 04.11.2026 |
| Autor | Charlie Moore |
| Kapitelbezug | 24.1 Wo die Zeit verloren geht (auch 24.2 bis 24.6); Bausteine B-24.1, B-24.3, B-24.5, B-24.6, B-13.1, B-19.4 der Agentendatei Version 1.21 (DL-101) |
| Fundstellen im Buch | 24.1 (Anhang B.3) |

## Zweck
Ein Messbogen in drei Teilen. Er trennt Laufzeit (wie lange der Agent an einem Beleg oder Lauf rechnet) von Durchlaufzeit (vom Eingang des Belegs bis zum freigegebenen Buchungsstapel) und zeigt, wo die Zeit tatsächlich verloren geht: beim Lesen, beim Schreiben, in Werkzeugrunden, beim Warten auf Systeme oder beim Warten auf Menschen. Erst messen, dann ändern, und jede Änderung mit dem Regressionstest absichern (B-17.4).

## Dateien
- `leervorlage_belege.csv` / `beispiel_ki_buchhalter_belege.csv` – Teilzeiten je Beleg, getrennt nach Standard und Sonderfall.
- `leervorlage_laeufe.csv` / `beispiel_ki_buchhalter_laeufe.csv` – Laufzeit je Lauf mit Zielzeiten und den fünf langsamsten Belegen (B-24.1).
- `leervorlage_massnahmen.csv` / `beispiel_ki_buchhalter_massnahmen.csv` – Vorher/Nachher je Maßnahme aus 24.2 bis 24.6 und dem Regressionstest.

Alle CSV: UTF-8 mit BOM, Semikolon als Trenner, öffnen direkt in einer Tabellenkalkulation.

## So gehen Sie vor
1. Zwei bis drei Läufe messen, ohne etwas zu ändern. Was das Werkzeug nicht anzeigt, als „nicht gemessen“ eintragen (B-24.1).
2. Zielzeiten je Lauf und je Beleg festlegen und in B-24.1 eintragen.
3. Den größten Zeitblock zuerst angehen. Liegt er bei der Wartezeit auf Menschen, hilft keine Technik, sondern ein anderer Ablauf (Laufbeginn, Zwischenstände).
4. Je Maßnahme vorher und nachher messen und den Regressionstest eintragen. Eine Maßnahme, die eine Prüfung, einen Wissensabruf oder eine Freigabe auslässt, ist ausgeschlossen (B-24.1, B-10.3).

## Anpassungshinweis
Die Beispielwerte je Beleg sind Orientierungswerte aus Kapitel 24.1, keine Messung; das Buch empfiehlt, sie durch eigene Zahlen zu ersetzen. Die Beispiele je Lauf und je Maßnahme stammen aus den Praxisbeispielen in Kapitel 24 (verschiedene Unternehmen) und zeigen nur die Größenordnung. Zielzeiten wie „60 Minuten“ je Lauf oder „3 Minuten“ je Beleg sind Platzhalter-Beispiele aus B-24.1. Ersparnisse durch Zwischenspeicher und Preise hängen vom Anbieter ab und sind deshalb nicht Teil dieses Bogens. [EIGENER WERT] markiert Werte, die Sie selbst aus Ihrem Betrieb eintragen, hier die Durchlaufzeit je Beleg, die Durchlaufzeit vorher ohne Agent, die Vorher-Werte der Maßnahmen und die offenen Felder der Läufe (Kapitel 24.1). Messen Sie den Vorher-Wert, bevor der Agent startet; später lässt er sich nicht mehr erheben. Einziger Beispielwert im Teil Belege ist „drei Arbeitstage“ vorher bei der Standard-Eingangsrechnung (Kapitel 24.1); die erste Zeile der Läufe ist als Beispielwert aus dem Praxisbeispiel 24.1 gekennzeichnet.

## Änderungen in Version 1.1
- Durchlaufzeit je Beleg und Vorher-Werte M-1 und M-6: [EIGENER WERT] statt „aus Quelle offen“, ohne Beispielwert. Erklärung der Markierung im Anpassungshinweis.

## Änderungen in Version 1.2
- Nach Kapitel 24.1: neue Spalte „Durchlaufzeit vorher ohne Agent“ in Teil Belege ([EIGENER WERT], Beispielwert „drei Arbeitstage“). Teil Läufe: alle neun offenen Felder [EIGENER WERT], erste Zeile als Beispielwert aus dem Praxisbeispiel gekennzeichnet.
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.3
- Belege: Prüfmarken durch „Ersetzen Sie die Werte durch Ihre eigenen Zahlen (24.1)“ nach Kapitel 24.1 ersetzt (Abgleich mit dem Manuskript, Stand 19.10.2026 11:17).

## Änderungen in Version 1.4
- Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.5
- README: Beispielwerte aus Kapitel 24.1 mit der Empfehlung des Buches, sie durch eigene Zahlen zu ersetzen (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.6
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Kapitelbezug) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.7
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.8
- Beispiel Belege, Spalte Vorgangsart: „Eingangsrechnungen und sonstige Kostenbelege“ und „Anlagenzugänge“ wie in B-03.1 und DL-131; Spalte Beleg unverändert (Kapitel 24.1) (Dreißigster Auftrag, 19.10.2026 22:55).
- Vollständige Fassung: Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.9
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.10
- Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.11
- Kapitelbezug: Bezug auf die Agentendatei auf Version 1.21 gehoben (DL-101, freigegeben am 04.11.2026 um 20:02 MEZ). (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
