#!/usr/bin/env python3
# NUR BEISPIELCODE, NICHT PRODUKTIV. Download DL-113 DATEV-Beispielschnittstelle zu Kapitel 14.7, Version 1.3, Stand 05.11.2026.
# DATEV ist eine eingetragene Marke der DATEV eG. Dieses Beispiel ist nicht von DATEV geprüft oder freigegeben.
# Fachliche Regeln, vorbehaltlich der Prüfung durch Ihren Steuerberater:
#   Belegdatum im EXTF-Buchungsstapel = TTMM; das Jahr ergibt sich aus dem Verwaltungssatz (Header:
#       WJ-Beginn, Datum von/bis).
#   Automatikkonten (AV/AM, z. B. 3400, 8400) bekommen KEINEN BU-Schlüssel (sonst doppelte Steuer);
#       BU-Schlüssel nur für Konten ohne Automatik [PRÜFEN gegen DATEV-Steuerschlüsseltabelle 2026, Dok.-Nr. 0907055].
#   Betrag mit Dezimalkomma, ohne Vorzeichen (Richtung über Soll/Haben-Kennzeichen).
#   Festschreibung im Header immer 0 (Regel des KI-Buchhalters, Kap. 8).
#   Übertragung (Schritt 7 in Kapitel 14.7) nur als Skelett: standardmäßig AUS, ohne Zugang und ohne Freigabe
#       nur Probelauf ohne Versand; keine Netzwerkverbindung im Programm.
#   Geheimnisse (Kapitel 14.6): Das Programm liest den Zugang nur aus der Umgebungsvariablen DATEV_CLIENT_SECRET
#       (Name in .env.example, Wert im Tresor), meldet einen fehlenden Wert mit seinem Namen und gibt den Wert nie aus.
# Feldauswahl gekürzt; vollständiger Satzaufbau (v13, 125 Spalten) laut DATEV-Developer-Portal [PRÜFEN Portal].
"""DATEV-EXTF-Buchungsstapel – vereinfachtes Beispiel für den KI-Buchhalter"""

import hashlib
import json
import os
import sys
import tempfile
from datetime import datetime, date
from typing import Callable, Dict, List, Optional, Tuple

# Automatikkonten laut DATEV-Kontenrahmen 2026 (Auszug, Funktionen AV/AM; Quelle: SKR 03 Art.-Nr. 11174, SKR 04 Art.-Nr. 11175)
AUTOMATIKKONTEN = {
    "SKR03": {"3400", "8400", "3736", "8736", "3760", "3030"},
    "SKR04": {"5400", "4400", "5736", "4736", "5760", "5130"},
}
SPALTEN = ("Umsatz (ohne Soll/Haben-Kz);Soll/Haben-Kennzeichen;WKZ Umsatz;Kurs;Basis-Umsatz;WKZ Basis-Umsatz;"
           "Konto;Gegenkonto (ohne BU-Schlüssel);BU-Schlüssel;Belegdatum;Belegfeld 1;Belegfeld 2;Skonto;Buchungstext")


class DatevSchnittstelle:
    def __init__(self, kontenrahmen: str = "SKR03", wj_beginn: date = date(2026, 1, 1),
                 berater: int = 1001, mandant: int = 10001, sachkontenlaenge: int = 4):
        self.kontenrahmen = kontenrahmen
        self.wj_beginn = wj_beginn
        self.berater, self.mandant, self.sachkontenlaenge = berater, mandant, sachkontenlaenge

    def pruefe_buchung(self, b: Dict) -> List[str]:
        """Plausibilitätsprüfung; liefert Liste von Fehlern (leer = ok)."""
        fehler = [f"Pflichtfeld fehlt: {k}" for k in ("datum", "belegnummer", "konto", "gegenkonto", "betrag")
                  if k not in b]
        if fehler:
            return fehler
        try:
            datetime.strptime(b["datum"], "%Y-%m-%d")
        except ValueError:
            fehler.append("datum muss JJJJ-MM-TT sein (intern); exportiert wird TTMM")
        if float(b["betrag"]) <= 0:
            fehler.append("betrag muss positiv sein; Richtung über soll_haben")
        auto = AUTOMATIKKONTEN.get(self.kontenrahmen, set())
        if b.get("bu_schluessel") and (str(b["konto"]) in auto or str(b["gegenkonto"]) in auto):
            fehler.append("BU-Schlüssel auf Automatikkonto – doppelte Steuer; BU leer lassen")
        return fehler

    @staticmethod
    def _betrag(x) -> str:
        return f"{float(x):.2f}".replace(".", ",")

    @staticmethod
    def _ttmm(iso: str) -> str:
        return datetime.strptime(iso, "%Y-%m-%d").strftime("%d%m")  # TTMM

    def header(self, von: date, bis: date, bezeichnung: str, erzeugt_am: Optional[datetime] = None) -> str:
        """Verwaltungssatz (Zeile 1), Felder wie im Beispiel in Kapitel 14.7; Feld 21 Festschreibung = 0."""
        erzeugt = (erzeugt_am or datetime.now()).strftime("%Y%m%d%H%M%S") + "000"
        f = ['"EXTF"', "700", "21", '"Buchungsstapel"', "13", erzeugt, "", '"RE"', '"KI-Buchhalter"', '""',
             str(self.berater), str(self.mandant), self.wj_beginn.strftime("%Y%m%d"), str(self.sachkontenlaenge),
             von.strftime("%Y%m%d"), bis.strftime("%Y%m%d"), f'"{bezeichnung}"', '"KI"', "1", "0",
             "0",  # Feld 21 Festschreibung: immer 0
             '"EUR"', "", '""', "", "", '"03"' if self.kontenrahmen == "SKR03" else '"04"', "", "", '""',
             '"KI-Buchhalter [VERSION]"']  # letztes Feld: Version Ihrer Agentendatei (Kapitel 14.7)
        return ";".join(f)

    def formatiere_extf(self, buchungen: List[Dict], von: date, bis: date, bezeichnung: str,
                        erzeugt_am: Optional[datetime] = None) -> str:
        zeilen = [self.header(von, bis, bezeichnung, erzeugt_am), SPALTEN]
        for b in buchungen:
            d = datetime.strptime(b["datum"], "%Y-%m-%d").date()
            if not (von <= d <= bis):
                raise ValueError(f"Belegdatum {b['datum']} liegt außerhalb Datum von/bis des Stapels")
            zeilen.append(";".join([
                self._betrag(b["betrag"]),
                '"S"' if b.get("soll_haben", "S") == "S" else '"H"',
                '"EUR"', "", "", "",
                str(b["konto"]), str(b["gegenkonto"]),
                f'"{b.get("bu_schluessel", "")}"',
                self._ttmm(b["datum"]),
                f'"{b["belegnummer"]}"', '""', "",
                f'"{b.get("buchungstext", "")[:60]}"',
            ]))
        return "\r\n".join(zeilen)

    def erzeuge_vorschlag(self, buchung: Dict, von: date, bis: date) -> Dict:
        """Erzeugt nur eine Vorschlagsdatei (keine Übermittlung, keine Festschreibung)."""
        fehler = self.pruefe_buchung(buchung)
        if fehler:
            return {"status": "fehler", "meldung": fehler}
        return {"status": "ok", "meldung": "EXTF-Vorschlag erzeugt – Prüfung und Import durch Mensch/Steuerberater",
                "csv": self.formatiere_extf([buchung], von, bis, "Buchungsvorschlaege")}

    def erzeuge_stapel(self, buchungen: List[Dict], von: date, bis: date, bezeichnung: str,
                       erzeugt_am: Optional[datetime] = None) -> Dict:
        """Wie erzeuge_vorschlag, aber für mehrere freigegebene Buchungen in einem Stapel."""
        fehler = [f"{b.get('belegnummer', '?')}: {f}" for b in buchungen for f in self.pruefe_buchung(b)]
        if fehler:
            return {"status": "fehler", "meldung": fehler}
        return {"status": "ok", "meldung": "EXTF-Vorschlag erzeugt – Prüfung und Import durch Mensch/Steuerberater",
                "csv": self.formatiere_extf(buchungen, von, bis, bezeichnung, erzeugt_am)}


# ---------------------------------------------------------------------------------------------------------
# Skelett für Schritt 7 in Kapitel 14.7: Doppelversand-Sperre, Übertragung, Rückmeldung „success“, Protokoll.
# Standardmäßig AUS. Es gibt hier keine Netzwerkverbindung und keine Zugangsdaten; [ZUGANG] bleibt Platzhalter.
# ---------------------------------------------------------------------------------------------------------
ZUGANG = "[ZUGANG]"              # Platzhalter: Anmeldung über OAuth 2.0, Token im Tresor, nie im Programm (Kapitel 14.6)
ZUGANG_NAME = "DATEV_CLIENT_SECRET"  # nur der Name des Geheimnisses; der Wert liegt im Tresor (Kapitel 14.6)
UEBERTRAGUNG_AN = False          # erst nach Onboarding, Sandbox-Tests und Freigabe durch einen Menschen umstellen
NICHT_UEBERTRAGEN = "Nicht übertragen. Bitte übernehmen Sie den Vorschlag selbst."  # Wortlaut B-02.5


class FreigabeFehlt(Exception):
    """Ohne Freigabe durch einen Menschen wird nichts übertragen."""


class GeheimnisFehlt(RuntimeError):
    """Ein benötigtes Geheimnis ist nicht als Umgebungsvariable gesetzt. Die Meldung nennt nur den Namen."""


def lies_geheimnis(name: str) -> str:
    """Liest ein Geheimnis aus der Umgebungsvariablen `name` (Kapitel 14.6, Verweis statt Wert).
    Entwicklung: eine lokale Datei .env setzt die Variable; .env steht in .gitignore und wird nie eingecheckt,
    die Namen stehen in .env.example. Betrieb: der Tresor (etwa Azure Key Vault, AWS Secrets Manager,
    Google Secret Manager oder HashiCorp Vault) stellt die Variable bereit. Der Wert wird nie ausgegeben."""
    wert = os.environ.get(name, "").strip()
    if not wert:
        raise GeheimnisFehlt(f"Geheimnis {name} fehlt: Umgebungsvariable nicht gesetzt oder leer. Wert im Tresor "
                             f"hinterlegen und als Umgebungsvariable bereitstellen (Kapitel 14.6); "
                             f"in der Entwicklung über eine lokale .env nach dem Muster .env.example.")
    return wert


def schwaerze(text: str, *geheimnisse: str) -> str:
    """Ersetzt jeden Geheimniswert im Text durch *** (Schwärzen vor Protokoll und Ausgabe, Kapitel 14.6)."""
    for g in geheimnisse:
        if g and g != ZUGANG:
            text = text.replace(g, "***")
    return text


def pruefsumme(csv: str) -> str:
    """Fingerabdruck des Stapels für Sperre und Protokoll."""
    return hashlib.sha256(csv.encode("utf-8")).hexdigest()


def protokolliere(protokoll_pfad: str, eintrag: Dict) -> None:
    """Protokoll nach GoBD, nur anhängen: Datei, Prüfsumme, Auftragskennung, Ergebnis, Freigebender (Kapitel 16.3).
    [PRÜFEN Protokoll: Ablageort, Aufbewahrung und Unveränderbarkeit mit Verfahrensdokumentation DL-111 abstimmen]"""
    eintrag = dict(eintrag, zeitpunkt=datetime.now().isoformat(timespec="seconds"))
    with open(protokoll_pfad, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(eintrag, ensure_ascii=False) + "\n")


def lies_protokoll(protokoll_pfad: str) -> List[Dict]:
    if not os.path.exists(protokoll_pfad):
        return []
    with open(protokoll_pfad, encoding="utf-8") as f:
        return [json.loads(z) for z in f if z.strip()]


def schon_uebertragen(protokoll_pfad: str, summe: str) -> bool:
    """Doppelversand-Sperre: gesperrt ist ein Stapel, dessen Prüfsumme mit Ergebnis „success“ im Protokoll steht.
    [PRÜFEN Doppelversand-Sperre: zusätzlich Auftragskennung und Prüfregeln laut DATEV Developer Portal]"""
    return any(e.get("pruefsumme") == summe and e.get("ergebnis") == "success" for e in lies_protokoll(protokoll_pfad))


def sende_an_datev(csv: str, zugang: str) -> Tuple[Optional[str], Optional[str]]:
    """Übertragung über die DATEV-Online-APIs: Upload, dann Abfrage des Auftrags; liefert (Auftragskennung, Ergebnis).
    Leer: hier gibt es keine Netzwerkverbindung. Für Ihre Umgebung umsetzen.
    [PRÜFEN Übertragung: Ablauf und Endpunkte nach der aktuellen Beschreibung im DATEV Developer Portal]"""
    raise NotImplementedError("Übertragung nicht umgesetzt – nur Probelauf möglich")


def uebertrage_stapel(csv: str, dateiname: str, protokoll_pfad: str, freigegeben_von: Optional[str],
                      zugang: str = ZUGANG, uebertragung_an: bool = UEBERTRAGUNG_AN,
                      sender: Callable[[str, str], Tuple[Optional[str], Optional[str]]] = sende_an_datev) -> Dict:
    """Schritt 7: Freigabe Pflicht, Doppelversand-Sperre, Übertragung oder Probelauf, Rückmeldung, Protokoll.
    Als übertragen gilt der Stapel nur, wenn die Abfrage des Auftrags „success“ meldet (B-02.5, Kapitel 14.7).
    [PRÜFEN Rückmeldung „success“: Status-Werte nach der aktuellen Schnittstellenbeschreibung von DATEV]"""
    if not freigegeben_von:
        raise FreigabeFehlt("Keine Freigabe durch einen Menschen – Abbruch, nichts übertragen")
    summe = pruefsumme(csv)
    basis = {"datei": dateiname, "pruefsumme": summe, "freigegeben_von": freigegeben_von}
    if schon_uebertragen(protokoll_pfad, summe):
        protokolliere(protokoll_pfad, dict(basis, auftragskennung=None, ergebnis="gesperrt"))
        return {"status": "gesperrt", "meldung": "Stapel wurde bereits übertragen – kein zweiter Versand"}
    if not uebertragung_an:
        protokolliere(protokoll_pfad, dict(basis, auftragskennung=None, ergebnis="probelauf"))
        return {"status": "probelauf", "meldung": "Probelauf ohne Versand. " + NICHT_UEBERTRAGEN}
    if not zugang or zugang == ZUGANG:
        zugang = lies_geheimnis(ZUGANG_NAME)  # bricht mit GeheimnisFehlt ab, wenn der Wert fehlt; nichts gesendet
    try:
        kennung, ergebnis = sender(csv, zugang)
    except Exception as fehler:  # Fehlertexte können den Zugang enthalten: erst schwärzen, dann protokollieren
        meldung = schwaerze(f"{type(fehler).__name__}: {fehler}", zugang)
        protokolliere(protokoll_pfad, dict(basis, auftragskennung=None, ergebnis="fehler", meldung=meldung))
        return {"status": "nicht_uebertragen", "meldung": NICHT_UEBERTRAGEN + " " + meldung}
    protokolliere(protokoll_pfad, dict(basis, auftragskennung=kennung, ergebnis=ergebnis or "keine Rückmeldung"))
    if ergebnis == "success":
        return {"status": "uebertragen", "meldung": f"Übertragen, Auftragskennung {kennung}"}
    return {"status": "nicht_uebertragen", "meldung": NICHT_UEBERTRAGEN}


# Beispiel: Musterfälle 1 und 2 aus Kapitel 17.2, wie in Kapitel 14.7 (SKR 03, gekürzt)
MUSTERFAELLE = [
    {"datum": "2026-10-06", "belegnummer": "ER-2026-0815", "konto": "3400", "gegenkonto": "1600",
     "betrag": 5950.00, "bu_schluessel": "", "buchungstext": "Wareneingang Handelsware"},
    {"datum": "2026-10-14", "belegnummer": "ER-2026-0815", "konto": "1600", "gegenkonto": "3736",
     "betrag": 119.00, "bu_schluessel": "", "buchungstext": "Skonto 2 % ER-2026-0815"},
    {"datum": "2026-10-15", "belegnummer": "AR-2026-047", "konto": "1400", "gegenkonto": "8400",
     "betrag": 29750.00, "bu_schluessel": "", "buchungstext": "Lieferung Baumarkt"},
]
VON, BIS, BEZEICHNUNG = date(2026, 10, 1), date(2026, 10, 31), "Buchungsvorschlaege Oktober 2026"
BUCH_14_7 = [  # die Zeilen aus Kapitel 14.7
    '"EXTF";700;21;"Buchungsstapel";13;20261031120000000;;"RE";"KI-Buchhalter";"";1001;10001;20260101;4;20261001;'
    '20261031;"Buchungsvorschlaege Oktober 2026";"KI";1;0;0;"EUR";;"";;;"03";;;"";"KI-Buchhalter [VERSION]"',
    SPALTEN,
    '5950,00;"S";"EUR";;;;3400;1600;"";0610;"ER-2026-0815";"";;"Wareneingang Handelsware"',
    '119,00;"S";"EUR";;;;1600;3736;"";1410;"ER-2026-0815";"";;"Skonto 2 % ER-2026-0815"',
    '29750,00;"S";"EUR";;;;1400;8400;"";1510;"AR-2026-047";"";;"Lieferung Baumarkt"',
]


def selbsttest() -> bool:
    datev = DatevSchnittstelle("SKR03")
    stapel = datev.erzeuge_stapel(MUSTERFAELLE, VON, BIS, BEZEICHNUNG, datetime(2026, 10, 31, 12, 0, 0))
    ok = {"Beispiel gleich 14.7": stapel["status"] == "ok" and stapel["csv"].split("\r\n") == BUCH_14_7}
    csv = stapel["csv"]
    with tempfile.TemporaryDirectory() as tmp:
        prot = os.path.join(tmp, "protokoll.jsonl")
        r = uebertrage_stapel(csv, "EXTF_Buchungsvorschlaege_2026-10.csv", prot, "[NAME FREIGEBENDER]")
        ok["Probelauf ohne Versand"] = r["status"] == "probelauf" and lies_protokoll(prot)[-1]["ergebnis"] == "probelauf"
        try:
            uebertrage_stapel(csv, "EXTF_test.csv", prot, None)
            ok["fehlende Freigabe bricht ab"] = False
        except FreigabeFehlt:
            ok["fehlende Freigabe bricht ab"] = True
        aufrufe = []

        def sender_ohne(c, z):  # Platzhalter-Sender: keine Bestätigung
            aufrufe.append(1)
            return "TEST-1", None
        r = uebertrage_stapel(csv, "EXTF_test.csv", prot, "[NAME FREIGEBENDER]", "[TESTZUGANG]", True, sender_ohne)
        ok["fehlende Bestätigung = nicht übertragen"] = (r["status"] == "nicht_uebertragen"
                                                       and r["meldung"] == NICHT_UEBERTRAGEN
                                                       and not schon_uebertragen(prot, pruefsumme(csv)))

        def sender_ok(c, z):  # Platzhalter-Sender: meldet „success“
            aufrufe.append(1)
            return "TEST-2", "success"
        r1 = uebertrage_stapel(csv, "EXTF_test.csv", prot, "[NAME FREIGEBENDER]", "[TESTZUGANG]", True, sender_ok)
        n = len(aufrufe)
        r2 = uebertrage_stapel(csv, "EXTF_test.csv", prot, "[NAME FREIGEBENDER]", "[TESTZUGANG]", True, sender_ok)
        ok["Doppelversand gesperrt"] = (r1["status"] == "uebertragen" and r2["status"] == "gesperrt"
                                        and len(aufrufe) == n)
        # Geheimnisse (Kapitel 14.6): Name statt Wert, klare Meldung, Wert nie in Ausgabe oder Protokoll
        alt = os.environ.pop(ZUGANG_NAME, None)
        try:
            n = len(aufrufe)
            try:
                uebertrage_stapel(csv + " ", "EXTF_test2.csv", prot, "[NAME FREIGEBENDER]", ZUGANG, True, sender_ok)
                ok["fehlendes Geheimnis bricht ab"] = False
            except GeheimnisFehlt as e:
                ok["fehlendes Geheimnis bricht ab"] = ZUGANG_NAME in str(e) and len(aufrufe) == n
            r = uebertrage_stapel(csv + " ", "EXTF_test2.csv", prot, "[NAME FREIGEBENDER]")
            ok["Übertragung AUS liest kein Geheimnis"] = r["status"] == "probelauf"
            testwert = "TESTWERT-nicht-echt-4711"
            os.environ[ZUGANG_NAME] = testwert

            def sender_fehler(c, z):  # Platzhalter-Sender: Fehlermeldung enthält den Zugang
                raise ConnectionError(f"Anmeldung mit {z} abgelehnt")
            r = uebertrage_stapel(csv + "  ", "EXTF_test3.csv", prot, "[NAME FREIGEBENDER]", ZUGANG, True, sender_fehler)
            with open(prot, encoding="utf-8") as f:
                inhalt = f.read()
            ok["Geheimnis geschwärzt, nie im Protokoll"] = (r["status"] == "nicht_uebertragen" and "***" in r["meldung"]
                                                          and testwert not in r["meldung"] and testwert not in inhalt)
        finally:
            os.environ.pop(ZUGANG_NAME, None)
            if alt is not None:
                os.environ[ZUGANG_NAME] = alt
    for name, wert in ok.items():
        print(("OK    " if wert else "FEHLER") + " " + name)
    return all(ok.values())


if __name__ == "__main__":
    if "--selbsttest" in sys.argv:
        sys.exit(0 if selbsttest() else 1)
    datev = DatevSchnittstelle("SKR03")
    print(datev.erzeuge_stapel(MUSTERFAELLE, VON, BIS, BEZEICHNUNG)["csv"])
    falsch = dict(MUSTERFAELLE[0], bu_schluessel="9")
    print(datev.erzeuge_vorschlag(falsch, VON, BIS)["meldung"])
