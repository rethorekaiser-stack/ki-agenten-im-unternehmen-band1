# DL-124 Übergabevermerk und Ablaufmuster

| | |
|---|---|
| Kennung | DL-124 |
| Version | 1.13 |
| Stand | 04.11.2026 |
| Autor | Charlie Moore |
| Kapitelbezug | 20.1 No Code (Übergabevermerk); 20.2 Low Code (Abläufe mit Auslösern, Bedingungen und Übergaben); Kapitel 19.1 bis 19.6 (die sechs Muster); Bausteine B-20.1, B-15.1, B-19.1 bis B-19.6 der Agentendatei Version 1.21 (DL-101) |
| Fundstellen im Buch | 20.2 (Anhang B.3) |

## Zweck
Zwei Hilfen für einen Verbund ohne eigenes Programm:
1. **Übergabevermerk** (B-20.1): festes Format für jede Übergabe zwischen Agenten. Fehlt eine Angabe, nimmt der empfangende Agent das Ergebnis nicht an. Wer von Hand kopiert, kopiert den Vermerk vollständig.
2. **Ablaufmuster** für die Stufe Low Code: je Muster Auslöser, Bedingungen, Schritte, Tore, Freigabeschritte und Fehlerpfad für einen Ablauf im visuellen Baukasten.

Gilt nur, wenn der Verbund in B-18.1 eingetragen ist (Verbundplan DL-123). Steht dort „keiner“, ruhen B-20.1 und die Muster-Bausteine.

## Dateien
- `leervorlage_uebergabevermerk.md` / `beispiel_ki_buchhalter_uebergabevermerk.md` – Vorlage und ausgefülltes Beispiel (Agent für die vorbereitende Buchhaltung an KI-Buchhalter).
- `leervorlage_ablaufmuster.md` / `beispiel_ki_buchhalter_ablaufmuster.md` – Ablaufbeschreibung je Muster zum Ausfüllen und die sechs Muster am KI-Buchhalter.

## Anpassungshinweis
Wie die Bausteine Ihres Baukastens heißen und welche Funktionen er hat, unterscheidet sich je Plattform und ändert sich oft; die Plattformbände 2 bis 5 beschreiben sie. Ein Ablauf erzwingt die Reihenfolge, nicht den Inhalt: Die Regeln der Agentendatei gelten zusätzlich. Jede Änderung am Ablauf ist eine Änderung am Verbund mit Version und Regressionstest (Kapitel 17.4, DL-110). Ruft ein Assistent einen anderen selbst auf, ist das ein Verbund, der in B-18.1 eingetragen und getestet sein muss (Kapitel 20.1).

## Änderungen in Version 1.1
- Version der Agentendatei 1.8.

## Änderungen in Version 1.2
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.3
- Funktionsumfang je Plattform nach Kapitel 20.1 („ändert sich oft; die Plattformbände 2 bis 5 beschreiben sie“) statt Prüfmarke (Abgleich mit dem Manuskript, Stand 19.10.2026 11:17).

## Änderungen in Version 1.4
- Ablaufmuster: Freigabestufe; Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.5
- Beispiel Übergabevermerk: Bezug auf das Buch vereinheitlicht (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.6
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Kapitelbezug) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.7
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.8
- Musternamen nach den Abschnittstiteln von Kapitel 19: „Orchestrator und Arbeitsagenten“ (B-19.3), „Menschen im Verbund“ (B-19.6) in Beispiel und Leervorlage; „die Übergabe an Menschen“ als Beschreibung wie in Kapitel 20.1 unverändert (Lektorat Runde 15, Kapitel 19, 19.10.2026 22:25).

## Änderungen in Version 1.9
- Ablaufmuster nach Kapitel 20.2: Freigaberegel „Kein Vorschlag, der eine Freigabe braucht, geht ohne Freigabeschritt in den Stapel.“ und Probezeit-Satz „In der Probezeit geht jeder Vorschlag über 500 € zur Einzelfreigabe, auch bei Freigabestufe 1; über 10.000 € bleibt es beim Vieraugenprinzip.“ in Beispiel (gemeinsame Regeln, Abschnitte 1 und 2) und Leervorlage; Weiche, Tor und Fehlerpfad im Wortlaut des Buchs; Zahlen wie B-08.2 und B-05.2 der Agentendatei 1.14. Rolle im Beispiel Übergabevermerk: „Agent für die vorbereitende Buchhaltung“ (Lektorat Runde 16, Kapitel 20, 19.10.2026 22:40).

## Änderungen in Version 1.10
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.11
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.12
- Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.13
- Kapitelbezug: Bezug auf die Agentendatei auf Version 1.21 gehoben (DL-101, freigegeben am 04.11.2026 um 20:02 MEZ). (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)
