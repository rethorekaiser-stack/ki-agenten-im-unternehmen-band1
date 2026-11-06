# -*- coding: utf-8 -*-
"""
DL-130 Programmskelett Orchestrierung
Buch: KI-Agenten im Unternehmen, Band 1 Fundament, Kapitel 20.3; Bausteine B-18.1, B-19.3, B-20.1, B-20.3, B-21.2
Version 1.5 · Stand 04.11.2026 · Autor: Charlie Moore
Lizenz: eigene Lizenz, Wortlaut in LICENSE.md · Namensnennung: Charlie Moore, KI-Agenten im Unternehmen, Band 1 · Nutzen und Anpassen erlaubt, auch im eigenen Unternehmen, Weiterverkauf und Weitergabe gegen Entgelt nicht erlaubt, keine Gewähr für Richtigkeit und Eignung · Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.

Kommentiertes Skelett, plattformneutral. Es enthält KEINEN Anbieter-Code und ruft kein Modell auf.
Die Stelle, an der ein Agent aufgerufen wird (rufe_agent_auf), müssen Sie für Ihre Plattform selbst
umsetzen. Nur Python-Standardbibliothek.

Was das Skelett zeigt (Kapitel 20.3):
  1. Fester Weg: Das Programm bestimmt, welcher Agent in welcher Reihenfolge arbeitet.
     Die Agenten entscheiden nur innerhalb ihres Schritts.
  2. Zustand je Vorgang: jeder Beleg hat eine Kennung und genau einen Zustand.
  3. Erlaubnisliste: nur eingetragene Agenten mit eingetragenen Teilaufgaben (B-18.1, B-19.3).
  4. Wiederaufnahme am letzten bestätigten Zustand, nicht von vorn.
  5. Keine doppelte Wirkung: vor der Übergabe in den Stapel Prüfung anhand der Kennung.
  6. Begrenzte Wiederholungen mit Wartezeit, danach Ausnahme. Kein Ausweichen auf andere Agenten.
  7. Version je Vorgang: ein Vorgang endet mit der Version, mit der er begonnen hat.
  8. Freigabe und Festschreibung immer durch Menschen. Das Programm gibt nichts frei.
  9. Reifegrad je Vorgangsart (B-21.2, Kapitel 21.2): Vorschläge zu Vorgangsarten „in Erprobung“
     gehen unabhängig von der Staffel einzeln zur Freigabe. Ohne Eintrag gilt „in Erprobung“.
     Der Reifegrad steht im Betriebsprotokoll und beginnt bei „in Erprobung“.

Geheimnisse (Kapitel 14.6): Den Zugang zur Plattform liest das Programm nur über lies_geheimnis aus der
Umgebungsvariablen MODELL_API_SCHLUESSEL (Name in .env.example, Wert im Tresor). Fehlt der Wert, nennt die
Meldung den Namen; der Wert wird nie ausgegeben oder protokolliert.

Aufruf:
  python programmskelett_steuerung.py --selbsttest
      läuft mit einem Platzhalter-Agenten ohne Modell und prüft Wiederaufnahme und Idempotenz.
"""

import csv
import json
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from pathlib import Path

# ---------------------------------------------------------------------------
# Einstellungen. Werte sind Platzhalter; legen Sie sie im Verbundplan (DL-123) fest.
# ---------------------------------------------------------------------------
HOECHSTZAHL_WIEDERHOLUNGEN = 2      # [ANZAHL]: technische Fehler höchstens so oft wiederholen (Kapitel 20.3)
WARTEZEIT_SEKUNDEN = 0              # [WARTEZEIT] zwischen zwei Versuchen; im Selbsttest 0
PROBEZEIT = False                   # aus dem Einrichtungsprotokoll, Frage 8
# [REIFEGRAD JE VORGANGSART] nach B-21.2, geführt im Betriebsprotokoll (nicht im Einrichtungsprotokoll):
# nur "erprobt" oder "in Erprobung". Den Eintrag ändert nur ein Mensch.
# Beim Start steht jede Vorgangsart auf "in Erprobung"; ohne Eintrag gilt dasselbe.
REIFEGRAD = {}
MODELL_ZUGANG_NAME = "MODELL_API_SCHLUESSEL"   # nur der Name; der Wert liegt im Tresor (Kapitel 14.6)

# Zustände aus Kapitel 20.3 (B-20.3). Ein Vorgang ist immer in genau einem Zustand.
ZUSTAENDE = ("eingegangen", "ausgelesen", "vorgeschlagen", "geprüft",
             "freigegeben", "im Stapel", "Ausnahme")

# Fester Weg: Zustand -> (Teilaufgabe, nächster Zustand). "geprüft" nur, wenn eine Prüfschleife eingetragen ist.
WEG = {
    "eingegangen": ("auslesen", "ausgelesen"),
    "ausgelesen": ("kontieren", "vorgeschlagen"),
}

# Teilaufgaben, die nie abgegeben werden (B-19.3). Sie bleiben beim KI-Buchhalter.
NIE_ABGEBEN = {"kontieren", "Freigabestufe", "Freigabeanfrage", "Entwurf Voranmeldung", "Bericht"}

# Pflichtangaben des Übergabevermerks (B-20.1)
VERMERK_FELDER = ("Vorgang", "Beleg", "Von / an", "Teilaufgabe", "Ergebnis",
                  "Unsicher", "Offen", "Wissensstand")


# ---------------------------------------------------------------------------
# Erlaubnisliste (B-18.1, B-19.3): nur eingetragene Agenten und Teilaufgaben
# ---------------------------------------------------------------------------
def lade_erlaubnisliste(pfad):
    """Liest die Erlaubnisliste (CSV mit BOM, Semikolon). Rückgabe: {Teilaufgabe: (Agent, Version)}."""
    erlaubt = {}
    with open(pfad, encoding="utf-8-sig", newline="") as f:
        for zeile in csv.DictReader(f, delimiter=";"):
            if zeile.get("erlaubt", "").strip().lower() != "ja":
                continue
            agent, version = zeile["Agent"].strip(), zeile["Version Agentendatei"].strip()
            if agent.startswith("[") or version.startswith("["):
                continue  # Platzhalter: nicht eingetragen, also nicht erlaubt
            erlaubt[zeile["Teilaufgabe"].strip()] = (agent, version)
    return erlaubt


# ---------------------------------------------------------------------------
# Vorgang und Protokoll
# ---------------------------------------------------------------------------
@dataclass
class Vorgang:
    kennung: str            # eindeutige Kennung, z. B. aus Belegeingang und Rechnungsnummer
    beleg: str              # Verweis auf den Originalbeleg
    zustand: str = "eingegangen"
    version: dict = field(default_factory=dict)   # Agent -> Version, festgelegt beim Beginn des Vorgangs
    vermerk: dict = field(default_factory=dict)    # letzter angenommener Übergabevermerk
    vorschlag: dict = field(default_factory=dict)
    grund: str = ""


class Protokoll:
    """Unveränderliches Protokoll als JSON-Zeilen: nur anhängen, nie ändern (B-16.3)."""

    def __init__(self, pfad):
        self.pfad = Path(pfad)

    def schreibe(self, vorgang, alt, neu, agent, version, hinweis=""):
        eintrag = {"zeit": datetime.now().isoformat(timespec="seconds"), "vorgang": vorgang.kennung,
                   "von": alt, "nach": neu, "agent": agent, "version": version, "hinweis": hinweis}
        with self.pfad.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(eintrag, ensure_ascii=False) + "\n")

    def letzter_zustand(self):
        """Letzter bestätigter Zustand je Vorgang, für die Wiederaufnahme."""
        stand = {}
        if self.pfad.exists():
            for zeile in self.pfad.read_text(encoding="utf-8").splitlines():
                e = json.loads(zeile)
                stand[e["vorgang"]] = e["nach"]
        return stand


def wechsle(vorgang, neu, protokoll, agent, hinweis=""):
    assert neu in ZUSTAENDE, neu
    alt = vorgang.zustand
    vorgang.zustand = neu
    protokoll.schreibe(vorgang, alt, neu, agent, vorgang.version.get(agent, "-"), hinweis)


# ---------------------------------------------------------------------------
# Hier setzen Sie Ihre Plattform ein. Kein Anbieter-Code im Skelett.
# ---------------------------------------------------------------------------
class GeheimnisFehlt(RuntimeError):
    """Ein benötigtes Geheimnis ist nicht als Umgebungsvariable gesetzt. Die Meldung nennt nur den Namen."""


def lies_geheimnis(name):
    """Liest ein Geheimnis aus der Umgebungsvariablen `name` (Kapitel 14.6, Verweis statt Wert).
    Entwicklung: eine lokale Datei .env setzt die Variable; .env steht in .gitignore und wird nie eingecheckt,
    die Namen stehen in .env.example. Betrieb: der Tresor (etwa Azure Key Vault, AWS Secrets Manager,
    Google Secret Manager oder HashiCorp Vault) stellt die Variable bereit. Der Wert wird nie ausgegeben."""
    wert = os.environ.get(name, "").strip()
    if not wert:
        raise GeheimnisFehlt("Geheimnis %s fehlt: Umgebungsvariable nicht gesetzt oder leer. Wert im Tresor "
                             "hinterlegen und als Umgebungsvariable bereitstellen (Kapitel 14.6); "
                             "in der Entwicklung über eine lokale .env nach dem Muster .env.example." % name)
    return wert


def _pruefe_geheimnis_lesen(name):
    """Selbsttest ohne echten Wert: fehlt -> klare Meldung mit Namen; gesetzt -> Wert zurück, nie ausgegeben."""
    alt = os.environ.pop(name, None)
    try:
        try:
            lies_geheimnis(name)
            return False
        except GeheimnisFehlt as e:
            if name not in str(e):
                return False
        os.environ[name] = "TESTWERT-nicht-echt-4711"
        return lies_geheimnis(name) == "TESTWERT-nicht-echt-4711"
    finally:
        os.environ.pop(name, None)
        if alt is not None:
            os.environ[name] = alt


class TechnischerFehler(Exception):
    """Modell antwortet nicht, Werkzeug meldet Fehler, Zeit überschritten."""


def rufe_agent_auf(agent, version, teilaufgabe, auftrag):
    """
    Ruft einen Agenten mit seiner Agentendatei in der angegebenen Version auf und gibt den
    Übergabevermerk (dict mit VERMERK_FELDER) bzw. den Vorschlag zurück.
    Der Auftrag nennt vier Dinge (Kapitel 19.3): Belege oder Zeitraum, Teilaufgabe,
    Ausgabe als Übergabevermerk, was nicht dazugehört. Nur die nötigen Daten mitgeben.
    Den Zugang holen Sie hier mit schluessel = lies_geheimnis(MODELL_ZUGANG_NAME), nie als Wert im Code.
    """
    raise NotImplementedError("Aufruf des Agenten für Ihre Plattform umsetzen [PRÜFEN: Plattformband]")


# ---------------------------------------------------------------------------
# Tore (Kapitel 19.1, 20.2): Programme prüfen zwischen den Schritten
# ---------------------------------------------------------------------------
def tor_vermerk(vermerk):
    """Tor 1: Vermerk vollständig? Fehlt eine Angabe, wird das Ergebnis nicht angenommen (B-20.1)."""
    fehlt = [f for f in VERMERK_FELDER if not str(vermerk.get(f, "")).strip()]
    return (not fehlt), ("fehlende Angaben im Übergabevermerk: " + ", ".join(fehlt)) if fehlt else ""


def tor_vorschlag(vorschlag):
    """Tor 2: Ausgabeformat vorhanden und Soll gleich Haben (B-13.3). Pflichtfelder an B-13.3 anpassen."""
    for f in ("Konto", "Gegenkonto", "Betrag", "Rechnungsbetrag brutto", "Stufe", "Begründung", "Soll", "Haben"):
        if f not in vorschlag:
            return False, "Ausgabeformat unvollständig: " + f
    if Decimal(str(vorschlag["Soll"])) != Decimal(str(vorschlag["Haben"])):
        return False, "Soll ungleich Haben"
    return True, ""


def stufe_aus_betrag(brutto):
    """Staffel nach B-08.2: Grenzbetrag gehört immer zur unteren Freigabestufe."""
    b = Decimal(str(brutto))
    if b <= Decimal("2500"):
        return 1
    if b <= Decimal("10000"):
        return 2
    return 3


def in_erprobung(vorgangsart):
    """B-21.2: ohne Eintrag gilt eine Vorgangsart als "in Erprobung"."""
    return REIFEGRAD.get(vorgangsart, "in Erprobung") != "erprobt"


def einzelfreigabe_noetig(brutto, stufe, vorgangsart=None):
    """Vorgangsart in Erprobung: immer Einzelfreigabe, unabhängig von der Staffel (B-21.2).
    Probezeit: über 500 € Einzelfreigabe; genau 500,00 € nicht (B-08.2)."""
    if in_erprobung(vorgangsart):
        return True
    if stufe >= 2:
        return True
    return PROBEZEIT and Decimal(str(brutto)) > Decimal("500")


# ---------------------------------------------------------------------------
# Steuerung
# ---------------------------------------------------------------------------
class Steuerung:
    def __init__(self, erlaubnisliste, protokoll, stapel, aufrufer=rufe_agent_auf):
        self.erlaubt = erlaubnisliste
        self.protokoll = protokoll
        self.stapel = stapel            # Menge der Kennungen im Buchungsstapel (Festschreibung 0)
        self.aufrufer = aufrufer

    def beginne(self, vorgang):
        """Version je Vorgang festhalten: der Vorgang endet mit dieser Version (B-20.3)."""
        if not vorgang.version:
            vorgang.version = {a: v for a, v in self.erlaubt.values()}

    def _aufruf_mit_wiederholung(self, vorgang, teilaufgabe):
        if teilaufgabe not in self.erlaubt:
            # Kein Ausweichen: nicht eingetragene Teilaufgabe oder Agent -> Ausnahme (Kapitel 20.3, Grundsatz 4)
            raise LookupError("Teilaufgabe nicht in der Erlaubnisliste: " + teilaufgabe)
        agent, _ = self.erlaubt[teilaufgabe]
        version = vorgang.version.get(agent)
        auftrag = {"Beleg": vorgang.beleg, "Teilaufgabe": teilaufgabe,
                   "Ausgabe": "Übergabevermerk nach B-20.1", "Nicht dazu": "[WAS NICHT DAZUGEHÖRT]"}
        for versuch in range(HOECHSTZAHL_WIEDERHOLUNGEN + 1):
            try:
                return agent, self.aufrufer(agent, version, teilaufgabe, auftrag)
            except TechnischerFehler as fehler:
                letzter = str(fehler)
                if versuch < HOECHSTZAHL_WIEDERHOLUNGEN:
                    time.sleep(WARTEZEIT_SEKUNDEN)
        raise TechnischerFehler("nach %d Wiederholungen: %s" % (HOECHSTZAHL_WIEDERHOLUNGEN, letzter))

    def bearbeite(self, vorgang):
        """Führt einen Vorgang vom aktuellen Zustand aus weiter (Wiederaufnahme inklusive)."""
        self.beginne(vorgang)
        while vorgang.zustand in WEG:
            teilaufgabe, ziel = WEG[vorgang.zustand]
            try:
                agent, ergebnis = self._aufruf_mit_wiederholung(vorgang, teilaufgabe)
            except (TechnischerFehler, LookupError) as fehler:
                wechsle(vorgang, "Ausnahme", self.protokoll, "Steuerung", str(fehler))
                return vorgang
            ok, grund = (tor_vermerk(ergebnis) if teilaufgabe == "auslesen" else tor_vorschlag(ergebnis))
            if not ok:
                # Fehlerpfad: Ausnahme, kein zweiter Versuch auf anderem Weg (Kapitel 20.2)
                wechsle(vorgang, "Ausnahme", self.protokoll, agent, grund)
                return vorgang
            if teilaufgabe == "auslesen":
                vorgang.vermerk = ergebnis
            else:
                vorgang.vorschlag = ergebnis
                eigene = stufe_aus_betrag(ergebnis["Rechnungsbetrag brutto"])
                if eigene != int(ergebnis["Stufe"]):
                    # Abweichende Freigabestufe: es gilt die höhere (B-16.2, B-19.5)
                    ergebnis["Stufe"] = max(eigene, int(ergebnis["Stufe"]))
            wechsle(vorgang, ziel, self.protokoll, agent)
        if vorgang.zustand == "vorgeschlagen":
            v = vorgang.vorschlag
            if in_erprobung(v.get("Vorgangsart")):
                v["Begründung"] = str(v.get("Begründung", "")) + " · Vorgangsart in Erprobung"
            if not einzelfreigabe_noetig(v["Rechnungsbetrag brutto"], int(v["Stufe"]), v.get("Vorgangsart")):
                self.uebergib_in_stapel(vorgang)  # Freigabestufe 1: Stapel, der Buchhalter sichtet und schreibt fest
            # sonst wartet der Vorgang auf die Freigabe durch Menschen (Freigabeschritt, B-16.2, B-19.6)
        return vorgang

    def freigabe_durch_menschen(self, vorgang, name, zeitpunkt):
        """Wird vom Freigabekanal aufgerufen, nie von einem Agenten. Freigabestufe 3 braucht zwei Personen."""
        wechsle(vorgang, "freigegeben", self.protokoll, "Mensch", "%s, %s" % (name, zeitpunkt))
        self.uebergib_in_stapel(vorgang)

    def uebergib_in_stapel(self, vorgang):
        """Keine doppelte Wirkung: Prüfung anhand der Kennung (Kapitel 20.3, Grundsatz 2)."""
        if vorgang.kennung in self.stapel:
            wechsle(vorgang, "im Stapel", self.protokoll, "Steuerung", "lag schon im Stapel, nicht erneut übergeben")
            return
        self.stapel.add(vorgang.kennung)   # hier: Übergabe in den Buchungsstapel mit Festschreibung 0
        wechsle(vorgang, "im Stapel", self.protokoll, "Steuerung")


def wiederaufnahme(vorgaenge, protokoll):
    """Setzt jeden Vorgang auf den letzten bestätigten Zustand aus dem Protokoll (Grundsatz 1)."""
    stand = protokoll.letzter_zustand()
    for v in vorgaenge:
        v.zustand = stand.get(v.kennung, v.zustand)
    return vorgaenge


# ---------------------------------------------------------------------------
# Selbsttest ohne Modell: Ausfall, Ausnahme, Wiederaufnahme, Idempotenz
# ---------------------------------------------------------------------------
def _selbsttest():
    import tempfile
    tmp = Path(tempfile.mkdtemp())
    liste = tmp / "erlaubnisliste.csv"
    liste.write_text("\ufeffAgent;Rolle;Version Agentendatei;Teilaufgabe;erlaubt;Übergabeweg\r\n"
                     "Agent für die vorbereitende Buchhaltung;Arbeitsagent;1.0;auslesen;ja;Übergabevermerk\r\n"
                     "KI-Buchhalter;Orchestrator;1.21;kontieren;ja;-\r\n", encoding="utf-8")
    ausfall = {"aktiv": True}

    def platzhalter_agent(agent, version, teilaufgabe, auftrag):
        if ausfall["aktiv"] and teilaufgabe == "kontieren":
            raise TechnischerFehler("Modell antwortet nicht")
        if teilaufgabe == "auslesen":
            return {"Vorgang": auftrag["Beleg"], "Beleg": auftrag["Beleg"], "Von / an": "%s %s / KI-Buchhalter" % (agent, version),
                    "Teilaufgabe": "auslesen", "Ergebnis": "Beträge", "Unsicher": "keine", "Offen": "keine",
                    "Wissensstand": "nicht verwendet"}
        return {"Konto": "[KONTO]", "Gegenkonto": "[KONTO]", "Betrag": "100.00", "Rechnungsbetrag brutto": "2500.00",
                "Vorgangsart": "Eingangsrechnungen und sonstige Kostenbelege",
                "Stufe": 1, "Begründung": "[REGEL, FUNDSTELLE]", "Soll": "100.00", "Haben": "100.00"}

    REIFEGRAD["Eingangsrechnungen und sonstige Kostenbelege"] = "erprobt"   # Praxisbeispiel 21.2
    prot = Protokoll(tmp / "protokoll.jsonl")
    stapel = {"B-2"}                                   # B-2 lag schon vor dem Ausfall im Stapel
    st = Steuerung(lade_erlaubnisliste(liste), prot, stapel, platzhalter_agent)
    vorgaenge = [Vorgang("B-1", "Ablage/B-1.pdf"), Vorgang("B-2", "Ablage/B-2.pdf")]
    for v in vorgaenge:
        st.bearbeite(v)
    assert all(v.zustand == "Ausnahme" for v in vorgaenge), [v.zustand for v in vorgaenge]
    # Nach der Störung: Mensch setzt die Ausnahme zurück auf den letzten bestätigten fachlichen Zustand
    ausfall["aktiv"] = False
    for v in vorgaenge:
        wechsle(v, "ausgelesen", prot, "Mensch", "Lauf nach Störung fortgesetzt")
    for v in wiederaufnahme(vorgaenge, prot):
        st.bearbeite(v)
    assert [v.zustand for v in vorgaenge] == ["im Stapel", "im Stapel"]
    assert len(stapel) == 2
    assert stufe_aus_betrag("2500.00") == 1 and stufe_aus_betrag("10000.00") == 2 and stufe_aus_betrag("10000.01") == 3
    # B-21.2: Vorgangsart in Erprobung oder ohne Eintrag -> Einzelfreigabe auch in Freigabestufe 1
    assert einzelfreigabe_noetig("1900.00", 1, "Eingangsrechnungen und sonstige Kostenbelege") is False
    assert einzelfreigabe_noetig("1900.00", 1, "Anlagenzugänge") is True
    assert einzelfreigabe_noetig("1900.00", 1, None) is True
    assert "lag schon im Stapel" in (tmp / "protokoll.jsonl").read_text(encoding="utf-8")
    assert _pruefe_geheimnis_lesen(MODELL_ZUGANG_NAME)     # Kapitel 14.6: Name statt Wert, klare Meldung
    assert "TESTWERT" not in (tmp / "protokoll.jsonl").read_text(encoding="utf-8")
    print("Selbsttest bestanden:", len(prot.pfad.read_text(encoding="utf-8").splitlines()), "Protokollzeilen")


if __name__ == "__main__":
    if "--selbsttest" in sys.argv:
        _selbsttest()
    else:
        print(__doc__)
