# DL-901 (vormals DL-010): Minimaler Wissens-MCP-Server, Skelett
# Version 1.4 · Stand 03.11.2026 · Band 1, Kapitel 13.7, 14.5 und 14.6
# Lizenz: eigene Lizenz, Wortlaut in LICENSE.md · Namensnennung: Charlie Moore, KI-Agenten im Unternehmen, Band 1 · Nutzen und Anpassen erlaubt, auch im eigenen Unternehmen, Weiterverkauf und Weitergabe gegen Entgelt nicht erlaubt, keine Gewähr für Richtigkeit und Eignung · Keine Steuer- oder Rechtsberatung, alle Fälle sind Beispiele.
#
# Ursprünglicher Inhalt (Version 1.0):
#   # Erweitern mit RAG, Versionierung, Gültigkeitszeiträumen
#   print("Skelett für Abteilungsserver Finanzen")
#
# Was dieses Skelett zeigt (Kapitel 13.7):
#   - Jedes Wissensstück trägt Version, gültig ab, gültig bis und Prüfsumme.
#   - Der Server liefert nie "das aktuelle Wissen", sondern das Wissen, das zum Belegdatum galt.
#   - Jede Anfrage trägt alle nötigen Angaben selbst (zustandslos).
#   - Online geht nur, was ein Mensch freigegeben hat. Alte Versionen bleiben erhalten.
#   - Drei Werkzeuge: finanzen_muss_wissen_abrufen („Muss-Wissen abrufen“), finanzen_kontierungsregel_suchen,
#     finanzen_aenderung_vorschlagen. Das dritte ändert nichts am Server.
#
# Nicht enthalten: Anmeldung, Rechteprüfung je Dienstkonto, Verschlüsselung, dauerhafte Ablage der
# Änderungsvorschläge, Volltext- oder Vektorsuche. Zugangsschlüssel nie im Code oder Prompt (Kapitel 14.6).
# Betreiben Sie den Server mit Anmeldung (ANMELDUNG_AN = True), liest er seinen Zugang nur über lies_geheimnis aus
# der Umgebungsvariablen WISSENSSERVER_ZUGANG (Name in .env.example, Wert im Tresor) und gibt den Wert nie aus.
#
# Aufruf:
#   python mcp_wissensserver_skelett.py --selbsttest [wissensstuecke.csv]
#   python mcp_wissensserver_skelett.py [wissensstuecke.csv]   (startet den MCP-Server, braucht ein MCP-SDK)
# [PRÜFEN: Anbindung an das MCP-SDK gegen die eingesetzte SDK-Version und die Spezifikation vom 28.07.2026 testen]

import csv
import hashlib
import os
import sys
from datetime import date, datetime
from pathlib import Path

SERVER_NAME = "server_finanzen"
STANDARD_CSV = Path(__file__).with_name("beispiel_ki_buchhalter_wissensstuecke.csv")
MAX_TREFFER = 5  # sparsam mit Umfang (Kapitel 14.5)
ANMELDUNG_AN = False                     # Anmeldung selbst umsetzen [PRÜFEN: Autorisierung laut MCP-Spezifikation]
ZUGANG_NAME = "WISSENSSERVER_ZUGANG"     # nur der Name; der Wert liegt im Tresor (Kapitel 14.6)


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


def _datum(text):
    text = (text or "").strip()
    if not text:
        return None
    return datetime.strptime(text, "%d.%m.%Y").date()


def _datum_oder_none(text, stueck_id):
    """Platzhalter wie [DATUM] gelten als nicht ausgefüllt: das Wissensstück wird nicht ausgeliefert."""
    try:
        return _datum(text)
    except ValueError:
        print("Hinweis: %s hat kein gültiges Datum (%s) und wird nicht ausgeliefert." % (stueck_id, text),
              file=sys.stderr)
        return None


def pruefsumme(inhalt):
    """Fingerabdruck eines Wissensstücks. Ändert sich ein Zeichen, ändert sich die Prüfsumme."""
    return hashlib.sha256(inhalt.encode("utf-8")).hexdigest()


def lade_wissensstuecke(pfad):
    """Liest die Wissensstücke. Spalten: id;thema;titel;version;gueltig_ab;gueltig_bis;freigegeben_von;
    freigegeben_am;lieferant;leistung;konto;fundstelle;inhalt (UTF-8 mit BOM, Semikolon)."""
    stuecke = []
    with open(pfad, encoding="utf-8-sig", newline="") as f:
        for zeile in csv.DictReader(f, delimiter=";"):
            if not (zeile.get("id") or "").strip():
                continue
            zeile["gueltig_ab_d"] = _datum_oder_none(zeile.get("gueltig_ab"), zeile["id"])
            zeile["gueltig_bis_d"] = _datum_oder_none(zeile.get("gueltig_bis"), zeile["id"])
            zeile["pruefsumme"] = pruefsumme(zeile.get("inhalt") or "")
            stuecke.append(zeile)
    return stuecke


def _freigegeben(stueck):
    return bool((stueck.get("freigegeben_von") or "").strip() and (stueck.get("freigegeben_am") or "").strip())


def _gilt_am(stueck, stichtag):
    ab, bis = stueck["gueltig_ab_d"], stueck["gueltig_bis_d"]
    return ab is not None and ab <= stichtag and (bis is None or stichtag <= bis)


def _ausgabe(stueck):
    return {
        "titel": stueck["titel"],
        "thema": stueck["thema"],
        "version": stueck["version"],
        "gueltig_ab": stueck["gueltig_ab"],
        "gueltig_bis": stueck.get("gueltig_bis") or "bis zur nächsten Fassung",
        "pruefsumme": stueck["pruefsumme"],
        "fundstelle": stueck.get("fundstelle") or "",
        "inhalt": stueck.get("inhalt") or "",
    }


def finanzen_muss_wissen_abrufen(stuecke, belegdatum, themen):
    """Muss-Wissen abrufen: Liefert die freigegebenen Wissensstücke des Muss-Wissens Finanzen, die zum Belegdatum gelten,
    zu den genannten Themen, etwa "Kontenrahmen" oder "Wertgrenzen". Nutze es als ersten Aufruf jedes
    Laufs und für jedes neue Belegdatum. Es ändert nichts."""
    try:
        stichtag = _datum(belegdatum)
    except ValueError:
        return {"fehler": "Belegdatum nicht lesbar. Bitte im Format TT.MM.JJJJ angeben."}
    if stichtag is None:
        return {"fehler": "Belegdatum fehlt. Ohne Belegdatum liefert der Server kein Wissen."}
    gesucht = {t.strip().lower() for t in themen if t.strip()}
    treffer = [s for s in stuecke if _freigegeben(s) and _gilt_am(s, stichtag)
               and (not gesucht or s["thema"].lower() in gesucht)]
    fehlend = sorted(gesucht - {s["thema"].lower() for s in treffer})
    antwort = {"belegdatum": belegdatum, "wissensstuecke": [_ausgabe(s) for s in treffer]}
    if fehlend:
        antwort["hinweis"] = ("Kein gültiges Wissen zum Belegdatum für: " + ", ".join(fehlend)
                              + ". Bitte Ausnahme melden; nicht schätzen.")
    return antwort


def finanzen_kontierungsregel_suchen(stuecke, belegdatum, lieferant_name, leistungsbeschreibung):
    """Sucht im Muss-Wissen Finanzen die Kontierungsregel, die zum Belegdatum für diesen Lieferanten und
    diese Leistung gilt. Nutze es vor jedem Buchungsvorschlag. Es ändert nichts."""
    try:
        stichtag = _datum(belegdatum)
    except ValueError:
        return {"fehler": "Belegdatum nicht lesbar. Bitte im Format TT.MM.JJJJ angeben."}
    if stichtag is None:
        return {"fehler": "Belegdatum fehlt."}
    lieferant = (lieferant_name or "").strip().lower()
    leistung = (leistungsbeschreibung or "").strip().lower()
    treffer = []
    for s in stuecke:
        if s["thema"].lower() != "kontierungsregel" or not _freigegeben(s) or not _gilt_am(s, stichtag):
            continue
        l_regel = (s.get("lieferant") or "").strip().lower()
        k_regel = (s.get("leistung") or "").strip().lower()
        if l_regel and l_regel not in lieferant:
            continue
        if k_regel and k_regel not in leistung:
            continue
        treffer.append(s)
    if not treffer:
        return {"ergebnis": "Keine Regel gefunden. Bitte Ausnahme an die Buchhaltung melden; nicht schätzen."}
    antwort = {"regeln": [dict(_ausgabe(s), konto=s.get("konto") or "") for s in treffer[:MAX_TREFFER]]}
    if len(treffer) > MAX_TREFFER:
        antwort["hinweis"] = "Mehr Treffer als angezeigt. Bitte Lieferant und Leistung genauer angeben."
    return antwort


_VORSCHLAEGE = []  # nur im Speicher; in Betrieb eine Ablage, die ein Mensch prüft


def finanzen_aenderung_vorschlagen(stuecke, wissensstueck, vorschlag, begruendung, beispielbelege):
    """Legt einen Vorschlag zur Änderung eines Wissensstücks ab, den ein Mensch prüft. Es ändert nichts
    am Server. Neues Wissen speichert der Agent nicht selbst (B-13.7)."""
    if not (vorschlag or "").strip() or not (begruendung or "").strip():
        return {"fehler": "Vorschlag und Begründung sind Pflicht."}
    kennung = "AV-%03d" % (len(_VORSCHLAEGE) + 1)
    _VORSCHLAEGE.append({"kennung": kennung, "wissensstueck": wissensstueck, "vorschlag": vorschlag,
                         "begruendung": begruendung, "beispielbelege": beispielbelege,
                         "eingereicht": date.today().strftime("%d.%m.%Y"), "status": "zur Prüfung"})
    return {"kennung": kennung, "hinweis": "Vorschlag abgelegt. Keine Änderung am Server; ein Mensch prüft und gibt frei."}


def selbsttest(stuecke):
    a = finanzen_muss_wissen_abrufen(stuecke, "28.12.2026", ["Kontenrahmen"])
    b = finanzen_muss_wissen_abrufen(stuecke, "05.01.2027", ["Kontenrahmen"])
    print("28.12.2026:", [w["version"] for w in a["wissensstuecke"]])
    print("05.01.2027:", [w["version"] for w in b["wissensstuecke"]], b.get("hinweis", ""))
    print(finanzen_kontierungsregel_suchen(stuecke, "06.10.2026", "Unbekannt GmbH", "Beratung"))
    print(finanzen_aenderung_vorschlagen(stuecke, "Kontierungsrichtlinie", "Regel ergänzen", "drei Ausnahmen", "ER-1"))
    ok = _pruefe_geheimnis_lesen(ZUGANG_NAME)
    print(("OK    " if ok else "FEHLER") + " Geheimnis aus Umgebungsvariable: Name statt Wert, klare Meldung")
    return ok


def starte_server(stuecke):
    try:
        from mcp.server.fastmcp import FastMCP  # MCP-SDK, nicht Teil dieses Skeletts
    except ImportError:
        print("Kein MCP-SDK installiert. Selbsttest mit --selbsttest möglich.", file=sys.stderr)
        sys.exit(1)
    if ANMELDUNG_AN:
        try:
            zugang = lies_geheimnis(ZUGANG_NAME)  # an Ihre Anmeldung übergeben, nie ausgeben
        except GeheimnisFehlt as fehler:
            print(fehler, file=sys.stderr)
            sys.exit(1)
    server = FastMCP(SERVER_NAME)

    # Name und Beschreibung wie in Kapitel 14.5: Bereich und Tätigkeit im Namen, Beschreibung aus dem Docstring.
    # [PRÜFEN: Parameter name und description gegen die eingesetzte SDK-Version]
    @server.tool(name="finanzen_muss_wissen_abrufen", description=finanzen_muss_wissen_abrufen.__doc__)
    def _abrufen(belegdatum: str, themen: list[str]) -> dict:
        return finanzen_muss_wissen_abrufen(stuecke, belegdatum, themen)

    @server.tool(name="finanzen_kontierungsregel_suchen", description=finanzen_kontierungsregel_suchen.__doc__)
    def _suchen(belegdatum: str, lieferant_name: str, leistungsbeschreibung: str) -> dict:
        return finanzen_kontierungsregel_suchen(stuecke, belegdatum, lieferant_name, leistungsbeschreibung)

    @server.tool(name="finanzen_aenderung_vorschlagen", description=finanzen_aenderung_vorschlagen.__doc__)
    def _vorschlagen(wissensstueck: str, vorschlag: str, begruendung: str, beispielbelege: str) -> dict:
        return finanzen_aenderung_vorschlagen(stuecke, wissensstueck, vorschlag, begruendung, beispielbelege)

    server.run()


if __name__ == "__main__":
    argumente = [a for a in sys.argv[1:] if not a.startswith("--")]
    pfad = Path(argumente[0]) if argumente else STANDARD_CSV
    wissen = lade_wissensstuecke(pfad)
    if "--selbsttest" in sys.argv:
        sys.exit(0 if selbsttest(wissen) else 1)
    else:
        starte_server(wissen)
