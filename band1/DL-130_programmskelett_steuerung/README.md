# DL-130 Programmskelett Orchestrierung

| | |
|---|---|
| Kennung | DL-130 |
| Version | 1.16 |
| Stand | 05.11.2026 |
| Autor | Charlie Moore |
| Kapitelbezug | 20.3 Für technische Umsetzer; Bausteine B-18.1, B-19.3, B-20.1, B-20.3 und B-21.2 der Agentendatei Version 1.21 (DL-101); Kapitel 14.6 (Tresor), 19.1 (Tore), 20.2 (Fehlerpfad), 21.2 (Reifegrad je Vorgangsart) |
| Fundstellen im Buch | 14.6, 20.3 (Anhang B.3) |

## Zweck
Kommentiertes Programmskelett für einen Verbund mit programmierter Steuerung und festem Weg: Das Programm bestimmt, welche Agenten in welcher Reihenfolge arbeiten; die Agenten entscheiden nur innerhalb ihres Schritts. Es zeigt Zustände je Vorgang, Erlaubnisliste der Agenten und Teilaufgaben, Tore zwischen den Schritten, Wiederaufnahme am letzten bestätigten Zustand, keine doppelte Wirkung über die Kennung, begrenzte Wiederholungen, kein Ausweichen auf nicht eingetragene Agenten, die Version je Vorgang und die Einzelfreigabe für Vorgangsarten in Erprobung.

Das Skelett ist plattformneutral und enthält keinen Anbieter-Code. Es ruft kein Modell auf: Die Funktion `rufe_agent_auf` ist leer und muss für Ihre Plattform umgesetzt werden [PRÜFEN: Plattformbände 2 bis 5]. Braucht Ihr Aufruf einen Schlüssel für das Modell, lesen Sie ihn dort mit `lies_geheimnis(MODELL_ZUGANG_NAME)` aus einer Umgebungsvariablen, die Ihr Tresor befüllt (`MODELL_API_SCHLUESSEL`, Kapitel 14.6); fehlt der Wert, bricht das Programm mit `GeheimnisFehlt` ab, ohne den Wert zu nennen. Der Selbsttest braucht keinen Schlüssel. Freigabe und Festschreibung bleiben bei Menschen.

## Dateien
- `programmskelett_steuerung.py` – das Skelett (nur Python-Standardbibliothek). `python programmskelett_steuerung.py --selbsttest` spielt mit einem Platzhalter-Agenten das Praxisbeispiel aus 20.3 nach: Ausfall, Wiederholungen, Ausnahme, Wiederaufnahme, ein Vorschlag lag schon im Stapel und wird nicht erneut übergeben. Dazu prüft er die Einzelfreigabe nach B-21.2. Der Selbsttest legt Dateien in einem temporären Ordner des Betriebssystems an; führen Sie ihn in einer Testumgebung aus.
- `leervorlage_erlaubnisliste.csv` – Erlaubnisliste: Agent, Rolle, Version der Agentendatei, Teilaufgabe, erlaubt, Übergabeweg.
- `beispiel_ki_buchhalter_erlaubnisliste.csv` – KI-Buchhalter (Agentendatei 1.21) als Orchestrator mit dem Agenten für die vorbereitende Buchhaltung (Kapitel 19.3).

Der Ordnername `DL-130_programmskelett_steuerung` bleibt aus Gründen der Verlinkung unverändert.

## Zustände (Kapitel 20.3)
eingegangen → ausgelesen → vorgeschlagen → (geprüft) → freigegeben → im Stapel; jederzeit möglich: Ausnahme. Jeder Wechsel kommt mit Zeitpunkt, Agent und Version ins Protokoll (nur anhängen).

## Anpassungshinweis
Werte wie die Höchstzahl der Wiederholungen und die Wartezeit sind Platzhalter; legen Sie sie im Verbundplan (DL-123) fest. Die Staffel im Skelett folgt B-08.2 (bis einschließlich 2.500 € Freigabestufe 1, über 2.500 € bis einschließlich 10.000 € Freigabestufe 2, darüber Freigabestufe 3; Probezeit über 500 € Einzelfreigabe). Weicht die Freigabestufe des Agenten ab, gilt die höhere. Den Reifegrad je Vorgangsart (`REIFEGRAD`, B-21.2) übernehmen Sie aus dem Betriebsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“, eine Vorgangsart ohne Eintrag gilt als „in Erprobung“, ihre Vorschläge gehen einzeln zur Freigabe. Über 10.000 € gilt weiter das Vieraugenprinzip (die Freigabestufe 3 bleibt am Vorschlag stehen). Den Eintrag ändert nur ein Mensch. Die Pflichtfelder in Tor 2 an Ihr Ausgabeformat (B-13.3) anpassen. Bevor das Programm mit echten Belegen läuft: Abnahmetest des Verbunds (DL-123) und Regressionstest (DL-110). Jede Änderung am Programm ist eine Änderung am Verbund mit Version.

## Änderungen in Version 1.1
- Titel einheitlich „Programmskelett Orchestrierung“ (README, Kopf des Skeletts, DL-100, Wurzel-README).
- B-21.2: Vorschläge zu Vorgangsarten „in Erprobung“ oder ohne Eintrag gehen unabhängig von der Staffel zur Einzelfreigabe, mit Vermerk „Vorgangsart in Erprobung“; Selbsttest ergänzt.
- Beispiel-Erlaubnisliste und Selbsttest: KI-Buchhalter mit Agentendatei 1.8.

## Änderungen in Version 1.2
- Kommentare im Programm (Version 1.2) und Anpassungshinweis: Reifegrad im Betriebsprotokoll, nicht im Einrichtungsprotokoll; jede Vorgangsart beginnt bei „in Erprobung“ (Entscheidung des Buch-Autors, 19.10.2026). Programmlogik unverändert, Selbsttest bestanden.

## Änderungen in Version 1.3
- Fundstellen im Buch nach Anhang B.3 (Bereinigung 4, 19.10.2026) im Kopf ergänzt.

## Änderungen in Version 1.4
- Lizenzzeile mit Namensnennung im Programmkopf ergänzt, Programmkopf auf Version 1.3 (Entscheidungen Thore 19.10.2026, 11:06). Programmlogik unverändert, Selbsttest bestanden.

## Änderungen in Version 1.5
- Programmkopf (Version 1.4): Lizenzzeile auf die eigene Lizenz umgestellt, mit Hinweis „Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.“ (Umentscheidung Lizenz 11:21). Programmlogik unverändert, Selbsttest bestanden.

## Änderungen in Version 1.6
- Skelett: Kommentare und Docstrings „Freigabestufe“, Start „in Erprobung“; Wert „Freigabestufe“ in der nicht ausgewerteten Menge NIE_ABGEBEN; Programmlogik und Feldname „Stufe“ unverändert, Selbsttest bestanden. Erlaubnisliste und README: Freigabestufe, Agentendatei 1.10 (Lektorat-Runde 1, Agentendatei v1.10, 19.10.2026 21:20).

## Änderungen in Version 1.7
- Selbsttest: Erlaubnisliste mit Version der Agentendatei 1.10 statt 1.8; Logik und Feldname „Stufe“ unverändert, Selbsttest bestanden (MD5 8F43424CAFBC707DA3EFB0445D1A41A6) (Siebzehnter Auftrag, 19.10.2026 21:30).

## Änderungen in Version 1.8
- Selbsttest und Beispiel-Erlaubnisliste mit Version der Agentendatei 1.12, README-Bezug 1.12; Logik unverändert, Selbsttest bestanden (MD5 905D20A4BCAA18EB85D3346581D29D88) (Zwanzigster Auftrag, Agentendatei v1.12, 19.10.2026 21:46).

## Änderungen in Version 1.9
- Selbsttest und Beispiel-Erlaubnisliste mit Version der Agentendatei 1.14, README-Bezug 1.14; Logik unverändert, Selbsttest bestanden (MD5 074EDADCCC2BCC9164FA630D104FC8E1) (Einundzwanzigster Auftrag, Agentendatei v1.14, 19.10.2026 21:50).

## Änderungen in Version 1.10
- Langform „Agent für die vorbereitende Buchhaltung“ in der Beispiel-Erlaubnisliste (Zeilen 2 und 4) und im Selbsttest (Testdaten, Spalte „Agent“ als Anzeigename); Leervorlage ohne Nennung. Programmlogik, Bezeichner und Programmkopf unverändert. py_compile und Selbsttest auf der Box bestanden („Selbsttest bestanden: 10 Protokollzeilen“), Beispiel-Erlaubnisliste vom Programm gelesen; PC und Box gleich (MD5 3DDD2176145C0F6A1B34A108932A6C63) (Siebenundzwanzigster Auftrag, Freigabe Buch-Autor, 19.10.2026 22:45).

## Änderungen in Version 1.11
- README, Anpassungshinweis: „Über 10.000 € gilt weiter das Vieraugenprinzip“ bei Vorgangsarten in Erprobung (Kapitel 21.2). Programm unverändert (MD5 3DDD2176145C0F6A1B34A108932A6C63) (Achtundzwanzigster Auftrag, Lektorat Runde 17, 19.10.2026 22:50).

## Änderungen in Version 1.12
- Selbsttest: Vorgangsarten „Eingangsrechnungen und sonstige Kostenbelege“ und „Anlagenzugänge“ wie in B-03.1 und DL-131 statt „Standard-Eingangsrechnung Inland“ und „Anlagenzugang“; Kommentar „Praxisbeispiel 21.2“. Nur Testdaten und sichtbarer Text, Logik und Erlaubnisliste unverändert (Dreißigster Auftrag, 19.10.2026 22:55).
- Vollständige Fassung: Selbsttest und Beispiel-Erlaubnisliste mit Version der Agentendatei 1.18, README-Bezug 1.18; Logik unverändert. py_compile und Selbsttest auf der Box bestanden („Selbsttest bestanden: 10 Protokollzeilen“), PC und Box gleich (MD5 56D30ABE946E4DEF7B29CCBD77125B17); der MD5-Wert im vorigen Punkt ist damit überholt; Bezug auf die Agentendatei von Version 1.14 auf 1.18 angepasst (Dreißigster Auftrag, vollständige Fassung mit Lektorat Runde 22, Agentendatei v1.18, 19.10.2026 23:02).

## Änderungen in Version 1.13
- Selbsttest und Beispiel-Erlaubnisliste mit Version der Agentendatei 1.19, README Z. 9 und 20 auf 1.19 (Z. 67 ist ein alter Vermerk und bleibt); Logik unverändert. py_compile und Selbsttest auf der Box bestanden („Selbsttest bestanden: 10 Protokollzeilen“), PC und Box gleich (MD5 siehe CHANGELOG); Bezug auf die Agentendatei von Version 1.18 auf 1.19 angepasst (Sechsunddreißigster Auftrag, Lektorat Runde 24, Agentendatei v1.19, 19.10.2026 23:24).

## Änderungen in Version 1.14
- Programm: Lesefunktion `lies_geheimnis` mit `GeheimnisFehlt` und Name `MODELL_API_SCHLUESSEL` (nur der Name, der Wert liegt im Tresor; Kapitel 14.6), Hinweis in `rufe_agent_auf`; Selbsttest um zwei Prüfungen erweitert; Selbsttest und Beispiel-Erlaubnisliste mit Version der Agentendatei 1.20; Logik der Steuerung unverändert. README: Kapitelbezug und Fundstelle 14.6; Bezug auf die Agentendatei von Version 1.19 auf 1.20 angepasst. py_compile und Selbsttest auf der Box bestanden („Selbsttest bestanden: 10 Protokollzeilen“) (Siebenunddreißigster Auftrag, Lektorat Runde 28, Agentendatei v1.20, 03.11.2026 23:30).

## Änderungen in Version 1.15
- README, Erlaubnisliste und Testwert im Selbsttest: Agentendatei Version 1.21. (Achtunddreißigster Auftrag, Lektorat Runde 29, Agentendatei v1.21, 04.11.2026)

## Änderungen in Version 1.16
- Programmkopf: Stand 04.11.2026 (N86). (Neununddreißigster Auftrag, Lektorat Runde 30, 05.11.2026)
