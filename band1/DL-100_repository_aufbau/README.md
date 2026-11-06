# DL-100 Aufbau des Repositorys, Übersicht aller Kennungen

| | |
|---|---|
| Kennung | DL-100 |
| Version | 1.20 |
| Stand | 06.11.2026 |
| Kapitelbezug | Anhang B (Repository, Skelett und Vorlagen zum Download); Einleitung „Downloads: Skelett, Prompts und Repository“ |
| Fundstellen im Buch | Einleitung, Anhang B.1 (Anhang B.3) |
| QR-Ziel | Der QR-Code in Anhang B.1 führt auf die Startseite des Repositorys; von dort ist diese Übersicht die Einstiegsseite. Repository-Adresse: [https://github.com/rethorekaiser-stack/ki-agenten-im-unternehmen-band1](https://github.com/rethorekaiser-stack/ki-agenten-im-unternehmen-band1). QR-Code-Bild: [`qr_code_repository.png`](qr_code_repository.png) (Anhang B.1) |

## Zweck
Übersicht aller Downloadkennungen von Band 1 „Fundament“ der Reihe „KI-Agenten im Unternehmen“. Jeder praktische Schritt im Buch ist mit seiner Kennung markiert. Das Skelett von Band 1 ist plattformneutral.

## Aufbau je Download
```
band1/DL-1xx_<kurzname>/
  README.md                    Zweck, Kapitelbezug, Version, Stand, Anpassungshinweis
  leervorlage.(md|csv)         zum Ausfüllen
  beispiel_ki_buchhalter.(md|csv)  ausgefülltes Beispiel des Referenzagenten KI-Buchhalter
```
Besteht ein Download aus mehreren Teilen (u. a. DL-109, DL-110, DL-112, DL-120, DL-122, DL-124, DL-130, DL-133), tragen die Dateien einen Zusatz, z. B. `leervorlage_wochenbericht.md`. Programmskelette (DL-130, DL-901) liegen zusätzlich als kommentierte Python-Datei bei. Im Wurzelverzeichnis liegen außerdem `.gitignore` (hält `.env`, Protokolle, echte Belege und erzeugte Buchungsstapel aus dem Repository heraus) und `.env.example` (nur die Namen der Geheimnisse, Werte im Tresor, Kapitel 14.6, Anhang B.7). Markdown für Texte, Prompts und Checklisten; CSV (UTF-8 mit BOM, Semikolon) für Tabellen, Rechenvorlage und Testfälle.

Grundlage aller Beispiele ist die Agentendatei KI-Buchhalter **Version 1.21 mit 92 Bausteinen** (Teil I bis VII, Kapitel 1 bis 25).

## Kennungen Band 1
| Kennung | Ordner | Inhalt | Fundstellen |
|---|---|---|---|
| DL-100 | `DL-100_repository_aufbau` | Aufbau des Repositorys, Übersicht aller Kennungen (diese Datei) | Einleitung, Anhang B.1 |
| DL-101 | `DL-101_agentendatei_ki_buchhalter` | Komplette Agentendatei KI-Buchhalter, Version 1.21 | Einleitung, 1, 2, 9, 13.3, Anhang D5; Kopf jedes Bausteinkastens |
| DL-102 | `DL-102_bausteine_checkliste` | Bausteine-Übersicht als Checkliste, fest oder abgefragt | 11.3, 25.2, Anhang D5 |
| DL-103 | `DL-103_stellenprofil` | Stellenprofil KI-Buchhalter, ausgefülltes Beispiel | 3.3, 4.3, 6.3, 6.4, 7.1, 9.1, 10.4, 25.1, 25.3 |
| DL-104 | `DL-104_direktive` | Vorlage Direktive | 4.1, 9.1, Anhang D5 |
| DL-105 | `DL-105_systemprompt` | Vorlage Systemprompt | 13.3 |
| DL-106 | `DL-106_startprompt_wissensrecherche` | Vorlage Startprompt mit stellenspezifischer Wissensrecherche | 9.3, 9.4, Anhang D5 |
| DL-107 | `DL-107_interview_ersteinrichtung` | Interview-Prompt Ersteinrichtung | 5.1, Anhang B.4 |
| DL-108 | `DL-108_spiegeltabelle` | Spiegeltabelle als Checkliste | 12.1 |
| DL-109 | `DL-109_rechenvorlage_budget_roi` | Rechenvorlage Wirtschaftlichkeit mit Token- und Kostenschätzer | Einleitung, 3.3, 10.2, 10.7, Anhang B.6 |
| DL-110 | `DL-110_testfaelle_abnahmetest` | Testfallliste und Abnahmetest: sechs Musterfälle mit Prüffall 4a, erweiterte Testliste mit den Prüffällen G-01 bis G-13, Bewertungsrubrik | 5.2, 5.4, 16.4, 17.2, 17.3, 19.5, 22.1, 22.3, 22.4, Anhang D4 |
| DL-111 | `DL-111_verfahrensdokumentation_gobd` | Muster-Verfahrensdokumentation nach GoBD | 16.3, 23.4 |
| DL-112 | `DL-112_wissensinventur` | Wissensinventur: Erhebungsbogen, Zugriffsmatrix, Interview-Prompt | 13.6, Anhang B.5 |
| DL-113 | `DL-113_datev_beispielschnittstelle` | DATEV-Beispielschnittstelle (aktiv): Anleitung für alle drei Stufen, Vorlage für den Verwaltungssatz, Beispiel, Programm für den Stapel als CSV-Datei | 14.6, 14.7 |
| DL-114 | `DL-114_kopiervorlage_skelett` | Kopiervorlage Skelett, leer und ausgefüllt | 25.3 |
| DL-115 | `DL-115_stufenvergleich_checkliste` | Checkliste Stufenvergleich No Code, Low Code, Für technische Umsetzer | 2.4 |
| DL-116 | `DL-116_eignungscheck` | Eignungscheck: vier Prüffragen, Skala, Entscheidungsweg | 3.1, 3.3 |
| DL-117 | `DL-117_ablaufzerlegung` | Ablaufzerlegung: Eingabe, Tätigkeit, Ergebnis, Prüfkriterium, Wer und Baustein je Schritt, Übergabepunkte | 3.2, 3.3 |
| DL-118 | `DL-118_kennzahlenblatt` | Kennzahlenblatt mit Ausgangswert, Zielwert, Messweg, Verantwortlichem | 3.3, 6.3 |
| DL-119 | `DL-119_stellenprofil_vorlage` | Stellenprofil-Vorlage (leer) mit Ausfüllhilfe | 4.3, 25.1, 25.3 |
| DL-120 | `DL-120_pilotplan_wochenbericht` | Pilotplan, Korrekturliste mit Fehlerklassen, Wochenbericht | 5.2 |
| DL-121 | `DL-121_checkliste_ausweitung` | Checkliste Ausweitung mit Testfällen T1 bis T5 | 5.3 |
| DL-122 | `DL-122_pflegekalender` | Pflegekalender und Versionsübersicht | 5.4 |
| DL-123 | `DL-123_verbundplan` | Verbundplan | 19.3, 19.4, 19.5 |
| DL-124 | `DL-124_uebergabevermerk_ablaufmuster` | Übergabevermerk und Ablaufmuster | 20.2 |
| DL-125 | `DL-125_checkliste_tarif_vertrag` | Checkliste Tarif und Vertrag | 10.5, 26.2 |
| DL-126 | `DL-126_beurteilungsbogen` | Beurteilungsbogen | 11.2 |
| DL-127 | `DL-127_offboarding_checkliste` | Offboarding-Checkliste | 11.4 |
| DL-128 | `DL-128_werkzeugbeschreibungen` | Vorlage Werkzeugbeschreibungen | 14.5, 14.7, Anhang D5 |
| DL-129 | `DL-129_leitplanken_checkliste` | Leitplanken-Checkliste | 16 |
| DL-130 | `DL-130_programmskelett_steuerung` | Programmskelett Orchestrierung | 14.6, 20.3 |
| DL-131 | `DL-131_reifegrad_grenzen_check` | Reifegrad- und Grenzen-Check | 21.2 |
| DL-132 | `DL-132_rechtsrahmen_ki_buchhalter` | Rechtsrahmen KI-Buchhalter | 23 |
| DL-133 | `DL-133_laufzeit_messbogen` | Laufzeit-Messbogen | 24.1 |

**Nummernvergabe:** DL-123 und DL-124 waren zeitweise reserviert und sind mit Teil V vergeben. DL-131 bis DL-133 sind mit Teil VI und VII vergeben. Für Band 1 wird mit **DL-134 bis DL-199** weitergezählt; nächste freie Kennung: DL-134.

Die Spalte „Fundstellen“ folgt Anhang B.3: Sie nennt jeden Abschnitt, in dem die Kennung im Text vorkommt; eine Zahl ohne Abschnitt steht für den Einstieg eines Kapitels. Der Kopf der Bausteinkästen, der überall auf DL-101 verweist, ist nicht einzeln aufgeführt. Anhang B ist nur genannt, wo der Download dort beschrieben ist.

## Bandübergreifend (DL-9xx)
| Kennung | Ordner | Inhalt | Fundstellen |
|---|---|---|---|
| DL-901 | `../uebergreifend/DL-901_mcp_wissensserver_skelett` | Skelett eines Wissens-MCP-Servers, bandübergreifend (vormals DL-010) | Einleitung, 13.7, 13.8, 14.6 |

## Lizenz und Hinweis
Kostenlose Zusatzleistung zum Buch. Namensnennung: Charlie Moore, KI-Agenten im Unternehmen, Band 1. Die Downloads dürfen Sie nutzen und anpassen, auch im eigenen Unternehmen. Weiterverkauf und Weitergabe gegen Entgelt sind nicht erlaubt. Eine Gewähr für Richtigkeit und Eignung wird nicht übernommen. Wortlaut: `LICENSE.md` im Wurzelverzeichnis. Jede Vorlage muss zwingend an die eigenen Bedürfnisse angepasst werden. Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.

## Änderungen in Version 1.3
- Grundlage Agentendatei Version 1.8 mit 92 Bausteinen; DL-131 bis DL-133 eingetragen, nächste freie Kennung DL-134.
- Inhalt und Kapitel aller Kennungen nach Anhang B.3; DL-130 Programmskelett Orchestrierung.
- Titel nach Anhang B.3 (vorher: „Aufbau des Repositorys: Band 1 Fundament“).

## Änderungen in Version 1.4
- Titel DL-111 „Muster-Verfahrensdokumentation nach GoBD“ und DL-131 „Reifegrad- und Grenzen-Check“ mit Bindestrich (Entscheidung des Buch-Autors, 19.10.2026).

## Änderungen in Version 1.5
- Spalte „Kapitel“ heißt „Fundstellen“ und folgt Anhang B.3 bzw. dl_kapitel_liste.md (20 Zeilen geändert, etwa DL-131 nur 21.2, DL-110 mit 16.4 und 22.1 bis 22.4); Erklärsatz aus Anhang B.3 ergänzt.
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.6
- Lizenzhinweis mit Namensnennung umgestellt (Entscheidungen Thore 19.10.2026, 11:06; um 11:21 durch die eigene Lizenz ersetzt, siehe Version 1.7).

## Änderungen in Version 1.7
- Lizenzhinweis auf die eigene Lizenz umgestellt (Wortlaut wie LICENSE.md), Namensnennung und Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ (Umentscheidung Lizenz 11:21).

## Änderungen in Version 1.8
- Grundlage Agentendatei Version 1.10 mit 92 Bausteinen; Titel DL-117 nach Anhang B.3 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).
- Zeile DL-103: Fundstellen nach Anhang B.3 (3.3, 4.3, 6.3, 6.4, 7.1, 9.1, 10.4, 25.1, 25.3); nächste freie Kennung bleibt DL-134 (Lektorat-Runde 1, Nachtrag v1.10, 19.10.2026).

## Änderungen in Version 1.9
- Bezug auf die Agentendatei von Version 1.10 auf 1.12 angepasst (Grundlage und Zeile DL-101) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.10
- Bezug auf die Agentendatei von Version 1.12 auf 1.14 angepasst (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.11
- DL-113 aktiv statt gesperrt (Sperre vom Buch-Autor aufgehoben); DL-101 mit Version 1.14 gleich der Agentendatei (Zweiundzwanzigster Auftrag, 19.10.2026 22:02).

## Änderungen in Version 1.12
- Fundstelle DL-123 „19.3 (auch 19.4, 19.5)“ (Lektorat Runde 14, 19.10.2026 22:17).

## Änderungen in Version 1.13
- Fundstellen DL-110 mit 19.5, DL-123 „19.3, 19.4, 19.5“ (Lektorat Runde 15, Kapitel 19, 19.10.2026 22:25).

## Änderungen in Version 1.14
- Zeile DL-113 nach Anhang B (Anleitung für alle drei Stufen, Vorlage für den Verwaltungssatz, Beispiel, Programm für den Stapel als CSV-Datei); DL-124 Fundstelle 20.2 geprüft (Lektorat Runde 16, Kapitel 20, 19.10.2026 22:40).

## Änderungen in Version 1.15
- Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.16
- Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.17
- `.gitignore` und `.env.example` im Wurzelverzeichnis beschrieben; Fundstellen DL-110 (Anhang D4, Prüffälle G-01 bis G-13), DL-113 und DL-130 (14.6), DL-901 (14.6) nach Anhang B.3; Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.18
- Grundlage und Zeile DL-101 auf Agentendatei Version 1.21. Kennungen und Fundstellen erneut mit Anhang B.3 abgeglichen, ohne Abweichung. DL-001 und DL-010 sind seit 04.11.2026 aus dem Repository gelöscht (Inhalte in DL-103 und DL-901), die Kennungen werden nicht neu vergeben. (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)

## Änderungen in Version 1.19
- Repo-Adresse und QR-Code gesetzt (Freigabe Thore 06.11.2026): `https://github.com/rethorekaiser-stack/ki-agenten-im-unternehmen-band1`, Bilddatei `qr_code_repository.png`. [PRÜFEN] zur Adresse geschlossen.

## Änderungen in Version 1.20
- Formulierung QR-Ziel: QR führt auf die Repo-Startseite; von dort ist diese Übersicht (DL-100) die Einstiegsseite. Root-README-Link auf DL-100 als Einstiegsseite (N111, Lektorat Runde 34, 06.11.2026).
