#!/usr/bin/env python3
import os
import re

INPUT_DIR = "German_Decks_v3"
OUTPUT_DIR = "German_Decks_v4"

BETTER_EXAMPLES = {
    "herum": [
        "Das Kind rennt schon wieder herum.",
        "Sie hat eine Runde gedreht.",
        "Lass uns einfach herumlaufen.",
        "Er ging im Zimmer herum.",
    ],
    "nervig": [
        "Das Warteln ist so nervig.",
        "Dein Gerede geht mir auf die Nerven.",
        "Dieses Problem ist echt nervend.",
        "Die Situation ist mega nervig.",
    ],
    "mitfahren": [
        "Kann ich mitfahren?",
        "Sie sind mit dem Auto mitgefahren.",
        "Wir fahren zusammen in die Stadt.",
        "Meine Eltern haben mich mitfahren lassen.",
    ],
    "Mehrfamilienhaus": [
        "Das Mehrfamilienhaus hat viele Wohnungen.",
        "In dem Mehrfamilienhaus wohnen hunderte people.",
        "Das neue Mehrfamilienhaus ist fertig.",
    ],
    "austoben": [
        "Die Kinder müssen sich austoben.",
        "Er hat sich beim Sport ausgetobt.",
        "Lass dich ruhig austoben!",
        "Nach dem Lernen muss er sich austoben.",
    ],
    "immerhin": [
        "Immerhin hast du es versucht.",
        "Das Haus ist immerhin bezahlbar.",
        "Immerhin hat es geregnet.",
        "Du hast immerhin angerufen.",
    ],
    "austauschen": [
        "Wir sollten unsere Nummern austauschen.",
        "Er hat die Batterie ausgetauscht.",
        "Die Meinungen wurden ausgetauscht.",
        "Können wir die Infos austauschen?",
    ],
    "rasant": [
        "Die Stadt wächst rasant.",
        "Die Technologie entwickelt sich rasant.",
        "Die Preise steigen rasant.",
        "Sein Zustand verbesserte sich rasant.",
    ],
    "Schwerpunkt": [
        "Der Schwerpunkt liegt auf der Wirtschaft.",
        "Wir verlagern den Schwerpunkt.",
        "Der neue Schwerpunkt ist klar.",
        "Das ist unser Schwerpunkt.",
    ],
    "Element": [
        "Jedes Element hat Eigenschaften.",
        "Das ist ein wichtiges Element.",
        "Feuer ist ein Element.",
        "Chemische Elemente.",
    ],
    "aufwerten": [
        "Die Renovierung wertet die Wohnung auf.",
        "Das verbessert das Image.",
        "Neue Qualifikationen werten dich auf.",
        "Das wertet das Angebot auf.",
    ],
    "ins Auge": [
        "Das fiel mir sofort ins Auge.",
        "Seine Kleidung fiel allen ins Auge.",
        "Ein Detail fiel mir ins Auge.",
        "Der Fehler fiel ihm ins Auge.",
    ],
    "Gesicht": [
        "Sie hat ein schönes Gesicht.",
        "Das Gesicht verrät nichts.",
        "Sein Gesicht wurde blass.",
        "Sie verbarg ihr Gesicht.",
    ],
    "Stimmung": [
        "Die Stimmung ist gut.",
        "Die Stimmung war gedrückt.",
        "Die Musik verbessert die Stimmung.",
        "Das verdirbt die Stimmung.",
    ],
    "Vorteil": [
        "Das ist ein großer Vorteil.",
        "Es gibt viele Vorteile.",
        "Der Vorteil liegt auf der Hand.",
        "Das hat nur Vorteile.",
    ],
    "Nachteil": [
        "Der Nachteil ist klar.",
        "Es gibt auch Nachteile.",
        "Der Nachteil: hohe Kosten.",
        "Das ist唯一的 Nachteil.",
    ],
    "Grund": [
        "Der Grund ist unbekannt.",
        "Aus welchem Grund?",
        "Der wahre Grund.",
        "Aus diesem Grund.",
    ],
    "Bedeutung": [
        "Die Bedeutung ist klar.",
        "Das hat keine Bedeutung.",
        "Von großer Bedeutung.",
        "Eine besondere Bedeutung.",
    ],
    "Gefahr": [
        "Die Gefahr ist real.",
        "Große Gefahr droht.",
        "Keine Gefahr.",
        "Ohne Gefahr.",
    ],
    "Möglichkeit": [
        "Es gibt nur eine Möglichkeit.",
        "Jede Möglichkeit nutzen.",
        "Eine weitere Möglichkeit.",
        "Keine andere Möglichkeit.",
    ],
    "Entscheidung": [
        "Die Entscheidung fiel schwer.",
        "Eine wichtige Entscheidung.",
        "Die Entscheidung ist getroffen.",
        "Eine falsche Entscheidung.",
    ],
    "Eindruck": [
        "Der erste Eindruck zählt.",
        "Ein guter Eindruck.",
        "Der Eindruck täuscht.",
        "Kein guter Eindruck.",
    ],
    "Voraussetzung": [
        " Eine wichtige Voraussetzung.",
        "Keine Voraussetzung.",
        "Die Voraussetzung ist erfüllt.",
        "Als Voraussetzung.",
    ],
    "Bedingung": [
        "Unter dieser Bedingung.",
        "Neue Bedingungen.",
        "Keine Bedingung.",
        "Strenge Bedingungen.",
    ],
    "Zusammenhang": [
        "Der Zusammenhang ist klar.",
        "In diesem Zusammenhang.",
        "Kein Zusammenhang.",
        "Ein direkter Zusammenhang.",
    ],
    "Begriff": [
        "Ein wichtiger Begriff.",
        "Der neue Begriff.",
        "Alle Begriffe.",
        "Der richtige Begriff.",
    ],
    "Methode": [
        "Eine bewährte Methode.",
        "Neue Methoden.",
        "Die beste Methode.",
        "Verschiedene Methoden.",
    ],
    "Mittel": [
        "Ein wirksames Mittel.",
        "Alle Mittel.",
        "Mit allen Mitteln.",
        "Das rechte Mittel.",
    ],
    "Weg": [
        "Der beste Weg.",
        "Ein neuer Weg.",
        "Verschiedene Wege.",
        "Der gleiche Weg.",
    ],
    "Mittel": [
        "Das rechte Mittel.",
        "Mit allen Mitteln.",
        "Finanzielle Mittel.",
        "Technische Mittel.",
    ],
}


def clean_tags(text):
    text = re.sub(r"\s*\(der/die/das\)\s*", "", text)
    text = re.sub(r"\s*\(regelmäßig\)\s*", "", text)
    text = re.sub(r"\s*\([^)]*\)\s*", "", text)
    text = re.sub(r"\|\s*\|", "|", text)
    text = text.replace("|", " | ").replace("  ", " ")
    return text.strip().strip("|").strip()


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            output.append(line)
            continue

        parts = line.split("\t")
        if len(parts) < 3:
            output.append(line)
            continue

        front = parts[0]
        back = parts[1]
        tags = parts[2]

        m = re.search(r"\{\{c1::([^:]+)::([^\}]+)\}\}", front)
        if not m:
            output.append(line)
            continue

        word = m.group(1).strip()

        syn_inner = m.group(2).strip()
        syns = [s.strip() for s in syn_inner.split("|") if s.strip()]
        syns = [s for s in syns if s][:2]

        while len(syns) < 2:
            syns.append("")

        final_syns = " | ".join([s for s in syns if s])

        new_front = f"{{{{c1::{word}::{final_syns}}}}}"

        cleaned_tags = clean_tags(tags)

        output.append(f"{new_front}\t{back}\t{cleaned_tags}")

    return output


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for fname in os.listdir(INPUT_DIR):
        if not fname.endswith(".txt"):
            continue

        fpath = os.path.join(INPUT_DIR, fname)
        result = process_file(fpath)

        outname = fname.replace("v3", "v4")
        outpath = os.path.join(OUTPUT_DIR, outname)

        with open(outpath, "w", encoding="utf-8") as f:
            f.write("\n".join(result))

        cards = len([r for r in result if r and not r.startswith("#")])
        print(f"Done: {fname} → {outname} ({cards} cards)")


if __name__ == "__main__":
    main()
