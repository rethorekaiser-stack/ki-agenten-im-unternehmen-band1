# Stufenwahl: KI-Buchhalter

Stand 19.10.2026 · Grundlage: Kapitel 2.4, 2.5 und 26.1

<!-- Der KI-Buchhalter wird in jedem Plattformband auf allen drei Stufen gebaut; die Agentendatei bleibt dieselbe.
     Die Tabelle zeigt, wie die drei Fragen jede Ausbauform einordnen. -->

| Frage (2.4) | No Code: Kontierungsassistent | Low Code: automatischer Belegeingang | Für technische Umsetzer: volle Anbindung |
|---|---|---|---|
| 1 Startet ohne Ihr Zutun? | nein – Sie laden jeden Beleg hoch | ja – ein neuer Beleg im Eingangsordner oder E-Rechnungs-Eingang startet den Ablauf | ja – ein eigenes Programm holt Belege ab und liest Kontoumsätze nur lesend ab |
| 2 Schreibt in andere Systeme? | nein – Sie übertragen den Vorschlag selbst oder sammeln ihn in einer EXTF-Datei für Ihren Steuerberater | ja – EXTF-Buchungsstapel mit Festschreibung 0 über Partner-Software und Buchungsdatenservice an den Steuerberater | ja – Übergabe über die DATEV Online-APIs |
| 3 Freigaben nicht umgehbar? | nein – die Grenze ziehen nur die Anweisungen, Sie prüfen jeden Vorschlag | ja – eine Bedingung verzweigt nach der Wertgrenzen-Staffel in Freigabeschritte | ja – serverseitige Prüfung von Betrag, Summengrenze und Probezeit |
| Ergebnis | passt, wenn Belegmenge klein und Prüfung von Hand verlässlich | nächste Stufe, sobald Wertgrenzen von Hand übersehen werden | für volle Kontrolle im Code |

**Auf jeder Stufe gleich:** Ein Mensch schreibt fest. Der Agent erhält keinen Bankzugang und löst keine Zahlungen aus (B-08.1, B-08.3). Auf der Stufe „Für technische Umsetzer“ liest das Programm Kontoumsätze nur lesend ab; sie dienen dem Agenten als Vorgangsdaten für den Abgleich von Zahlungen (Kapitel 2.5, B-03.1 Nr. 7). Geschäftstarif mit AVV, Datenhaltung und Ausschluss vom Training.

**Signal für den Wechsel (Praxisbeispiel 2.4):** Ein Großhändler startet mit No Code; nach einigen Wochen werden jeden Morgen rund vierzig Rechnungen hochgeladen und die Wertgrenze mehrfach übersehen. Low Code übernimmt mit einem Auslöser das Hochladen und erzwingt die Staffel mit einem Freigabeschritt. Anweisungen und Wissen bleiben unverändert.

**Kosten außerhalb der KI-Plattform:** No Code keine zusätzlichen DATEV-Kosten; Low Code Buchungsdatenservice laut DATEV-Preisliste 08/2026 ab 1,36 € im Monat zzgl. USt, je nach Zahl der Buchungssätze; technische Umsetzer: Onboarding für den Produktivbetrieb laut DATEV-Preisliste 1.500 € zzgl. USt einmalig (Art.-Nr. 46051); getestet wird vorher in einer Testumgebung von DATEV. Den Ablauf der Registrierung beschreibt DATEV im Developer Portal; er kann sich ändern.

**Selbsttest mit fünf Fragen (Praxisbeispiel 26.1):** Ein Großhändler für Sanitärbedarf mit rund 300 Eingangsrechnungen im Monat macht den Selbsttest.

| Frage (26.1) | Antwort |
|---|---|
| 1 Ohne Ihr Zutun starten? | nein, der Buchhalter will die Belege morgens selbst übergeben |
| 2 In andere Systeme übergeben? | ja, die Vorschläge sollen als Buchungsstapel zum Steuerberater |
| 3 Freigabeschritte, die sich nicht umgehen lassen? | ja, die Geschäftsführung will die Wertgrenzen technisch gesichert sehen |
| 4 Code pflegen? | nein, eine eigene IT gibt es nicht |
| 5 Kosten je Vorgang und Qualität laufend messen? | nein |
| Ergebnis | Zwei „Ja“ ergeben Low Code. Nach der Probezeit prüft er, ob Frage 1 inzwischen „ja“ lautet. |

Auswertung (26.1): 0 bis 1 „Ja“ No Code, 2 bis 3 „Ja“ Low Code, 4 bis 5 „Ja“ „Für technische Umsetzer“. Eine Ausnahme: Ohne „Ja“ bei Frage 4 empfiehlt der Test höchstens Low Code.
