# DL-117 Ablaufzerlegung: Eingabe, Tätigkeit, Ergebnis, Prüfkriterium, Wer und Baustein je Schritt, Übergabepunkte

| | |
|---|---|
| Kennung | DL-117 |
| Version | 1.4 |
| Stand | 19.10.2026 |
| Kapitelbezug | 3.2 Die Aufgabe zerlegen (Tabelle 3.2) |
| Fundstellen im Buch | 3.2, 3.3 (Anhang B.3) |

## Zweck
Eine Aufgabe in Einzelschritte zerlegen, **bevor** der Agent gebaut wird. Jeder Schritt bekommt fünf Angaben: **Eingabe** (was liegt vor), **Tätigkeit** (was wird getan), **Ergebnis** (was entsteht), **Prüfkriterium** (woran erkennt man, dass der Schritt richtig erledigt ist) und **Wer** (Agent, Mensch oder anderes Programm). Dazu kommt als sechste Spalte der **Baustein** der Agentendatei, der den Schritt regelt. Die Spalte „Wer“ zeigt die Übergabepunkte. Davon gibt es drei Arten: **Freigabe** (Mensch bestätigt oder ändert), **Ausnahme** (Agent kommt nicht weiter und meldet, was er braucht) und **Entscheidung** (Wahlrecht oder Ermessen, das der Agent nur vorbereitet).

Faustregel: so viele Schritte, wie es Stellen gibt, an denen etwas schiefgehen kann oder ein Mensch übernimmt. Was sich nicht zerlegen lässt, kann der Agent nicht zuverlässig erledigen. Grundlage sind vorhandene Arbeitsanweisungen, etwa die Verfahrensdokumentation (DL-111).

## Dateien
- `leervorlage.csv` – Spalten wie Tabelle 3.2: Nr., Eingabe, Tätigkeit, Ergebnis, Prüfkriterium, Wer, Baustein.
- `beispiel_ki_buchhalter.csv` – die Eingangsrechnung der Muster Technik GmbH in elf Schritten, wörtlich nach Tabelle 3.2 (Kapitel 3.2).

Format: UTF-8 mit BOM, Semikolon.

## Anpassungshinweis
Das Beispiel übernimmt Tabelle 3.2 aus Kapitel 3.2 unverändert. Die Übergabepunkte lesen Sie an der Spalte „Wer“ ab: Wechselt die Arbeit vom Agenten zum Menschen, liegt eine Freigabe vor (Schritt 8); Ausnahmen meldet der Agent bei Dublette, fehlenden Angaben oder fehlendem Konto (Abbildung 3.2). Lässt sich in Ihrem Unternehmen ein Fall nicht zerlegen (Beispiel aus 3.2: Anzahlungsrechnungen), nehmen Sie ihn vorerst nicht in die Vorgangsarten auf; der Agent meldet ihn als Ausnahme.

## Änderungen in Version 1.1
- Titel nach Anhang B.3 (vorher: „Ablaufzerlegung“).

## Änderungen in Version 1.2
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.3
- Schritt 9: an Steuerberater / beim Steuerberater (Kapitel 3) (Spiegelung Manuskript 15:56 / Festlegung Buch-Autor 16:09).

## Änderungen in Version 1.4
- Spalten wie Tabelle 3.2: Nr., Eingabe, Tätigkeit, Ergebnis, Prüfkriterium, Wer, Baustein (Spalte Übergabepunkt entfällt); Beispiel wörtlich aus Tabelle 3.2; Titel nach Anhang B.3 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
