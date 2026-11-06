# Ablaufbeschreibung für den Baukasten: [NAME DES ABLAUFS]

Muster: [ ] Kette (B-19.1) [ ] Weiche (B-19.2) [ ] Orchestrator und Arbeitsagenten (B-19.3) [ ] Parallele Teilläufe (B-19.4) [ ] Prüfschleife (B-19.5) [ ] Menschen im Verbund (B-19.6)
Version des Ablaufs: [X.Y] · Stand: [DATUM] · eingetragen in B-18.1 am: [DATUM] · verantwortlich: [NAME]

| Element | Beschreibung |
|---|---|
| Auslöser | [ZEITPLAN / EREIGNIS / AUFTRAG] (B-15.1) |
| Bedingungen (Weiche) | [BEDINGUNG → ZIEL] |
| Schritte | [SCHRITT: AGENT oder PROGRAMM, TEILAUFGABE] |
| Übergaben | Übergabevermerk (B-20.1) über [ÜBERGABEWEG] |
| Tore | [PRÜFUNG PER PROGRAMM, etwa Vermerk vollständig, Beträge gehen auf] |
| Freigabeschritte | [STUFE → WER GIBT FREI] (B-08.2, B-16.2) · Kein Vorschlag, der eine Freigabe braucht, geht ohne Freigabeschritt in den Stapel. Probezeit: [ja / nein]; In der Probezeit geht jeder Vorschlag über 500 € zur Einzelfreigabe, auch bei Freigabestufe 1; über 10.000 € bleibt es beim Vieraugenprinzip. |
| Fehlerpfad | [SCHRITT SCHEITERT → AUSNAHME AN WEN] |
| Grenzen | Höchstzahl Durchläufe je Schleife: [ANZAHL] · Grenzen je Lauf: [GRENZEN] (B-16.1) |
| Zusammenführen | [nur bei parallelen Zweigen: Dubletten und Summengrenze über alle Zweige] |

Änderungen am Ablauf: neue Version und Regressionstest (DL-110), Eintrag hier: [DATUM, ÄNDERUNG]
