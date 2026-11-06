# Repository-Skelett – KI-Agenten-Reihe
Stand: 06.11.2026

Öffentliches Repository zur Buchreihe „KI-Agenten im Unternehmen“: [https://github.com/rethorekaiser-stack/ki-agenten-im-unternehmen-band1](https://github.com/rethorekaiser-stack/ki-agenten-im-unternehmen-band1). Jeder praktische Schritt hat eine Downloadkennung (DL-xxx). Jeder Band hat sein eigenes Skelett; das Skelett von Band 1 ist plattformneutral.

## Kennungsschema
| Bereich | Kennungen | Ordner |
|---|---|---|
| Band 1 Fundament | DL-100 bis DL-199 (DL-1xx) | `band1/` |
| Band 2 | DL-200 bis DL-299 (DL-2xx) | noch nicht angelegt |
| Band 3 | DL-3xx | noch nicht angelegt |
| Band 4 | DL-4xx | noch nicht angelegt |
| Band 5 | DL-5xx | noch nicht angelegt |
| Band 6 | DL-6xx | noch nicht angelegt |
| bandübergreifend | DL-900 bis DL-999 (DL-9xx) | `uebergreifend/` |

**Regel:** Eine Kennung bleibt für immer dieselbe. Neue Fassungen ändern nur die Version im README des Downloads und den Eintrag im `CHANGELOG.md`, nie die Kennung. Eine vergebene Kennung wird nicht neu belegt.

## Struktur
- `band1/` – plattformneutrale Vorlagen und Skelette von Band 1 (derzeit DL-100 bis DL-133, Grundlage Agentendatei KI-Buchhalter Version 1.21 mit 92 Bausteinen; nächste freie Kennung DL-134, weiter bis DL-199; DL-111 Muster-Verfahrensdokumentation nach GoBD; DL-130 Programmskelett Orchestrierung; DL-131 Reifegrad- und Grenzen-Check); Einstiegsseite und Übersicht aller Kennungen: [`band1/DL-100_repository_aufbau/README.md`](band1/DL-100_repository_aufbau/README.md)
- Ordner für die Bände 2 bis 6 sind noch nicht angelegt; sie entstehen mit dem jeweiligen Band.
- `uebergreifend/` – bandübergreifende Downloads, z. B. DL-901 Skelett eines Wissens-MCP-Servers
- `vorlagen/`, `code/` – frühere Ordner; Inhalte in DL-103 und DL-901 aufgegangen, die Altdateien DL-001 und DL-010 am 04.11.2026 gelöscht (Kopie außerhalb des Repositorys im Archiv `_archiv_geloescht_2026-11-04/`)

- `.gitignore` – hält Zugangsdaten (`.env`), Protokolle, echte Belege und erzeugte Buchungsstapel aus dem Repository heraus (Kapitel 14.6, Anhang B.7)
- `.env.example` – Vorlage mit den Namen der Geheimnisse ohne Werte (`DATEV_CLIENT_SECRET`, `MODELL_API_SCHLUESSEL`, `WISSENSSERVER_ZUGANG`); die Werte liegen im Tresor

Aufbau je Download: `README.md` (Zweck, Kapitelbezug, Version, Stand, Anpassungshinweis), `leervorlage.*`, `beispiel_ki_buchhalter.*` (bei mehrteiligen Downloads mit Namenszusatz). Texte als Markdown, Tabellen als CSV (UTF-8 mit BOM, Semikolon).

## Zugangsdaten und Tresor
Kein Download enthält echte Zugangsdaten. Die Programmskelette DL-113, DL-130 und DL-901 nennen nur den Namen eines Geheimnisses und lesen den Wert erst zur Laufzeit aus einer Umgebungsvariablen, die Ihr Tresor befüllt (Kapitel 14.6). Übertragung und Anmeldung sind standardmäßig aus; die Selbsttests laufen ohne Geheimnis. Für Versuche auf dem eigenen Rechner kopieren Sie `.env.example` nach `.env`; `.env` kommt nie ins Repository.

## Vollständige Kontenrahmen: offizieller Bezugsweg
Das Buch und dieser Download nennen nur die Konten, die in den Beispielen vorkommen. Die vollständigen Kontenpläne gibt DATEV heraus und stellt sie kostenlos als PDF bereit [PRÜFEN bis Drucklegung: Adressen und Dokumentnummern, weil DATEV sie jährlich ändern kann]:
- SKR 03 (Art.-Nr. 11174) und SKR 04 (Art.-Nr. 11175): DATEV-Hilfe-Dokument Nr. 0907817 „DATEV-Kontenrahmen 2026“, https://apps.datev.de/help-center/documents/0907817
- Steuerschlüssel-Tabellen 2026: Dok.-Nr. 0907055, https://apps.datev.de/help-center/documents/0907055
- Übersichtsseite zum Jahreswechsel: https://www.datev.de/web/de/berufsgruppenuebergreifend/service-und-support/wichtige-informationen-zum-jahreswechsel/jahreswechsel-rechnungswesen/anpassungen-in-den-programmen/DATEV-Kontenrahmen

Holen Sie jedes Jahr die Fassung des Belegjahres. Die Änderungen gegenüber dem Vorjahr stehen im Dok.-Nr. 0907108. DATEV kennzeichnet die PDFs als Eigenformular und untersagt den Nachdruck, auch auszugsweise; deshalb liegen sie diesem Repository nicht bei (Anhang D1).

## Lizenz
Namensnennung: Charlie Moore, KI-Agenten im Unternehmen, Band 1

Die Downloads dürfen Sie nutzen und anpassen, auch im eigenen Unternehmen. Weiterverkauf und Weitergabe gegen Entgelt sind nicht erlaubt. Eine Gewähr für Richtigkeit und Eignung wird nicht übernommen.

Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele. Vorlagen zwingend an eigene Bedürfnisse anpassen. Wortlaut: `LICENSE.md`.

## Änderungen
Siehe `CHANGELOG.md`.
