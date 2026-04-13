#!/usr/bin/env python3
import os
import re
import random

INPUT_DIR = "German_Decks_v3"
OUTPUT_DIR = "German_Decks_v4"

BETTER_EXAMPLES = {
    "herum": [
        "Das Kind rennt immer im Haus herum.",
        "Sie ist unruhig herumgelaufen.",
        "Er hat nachgedacht und ist herumgegangen.",
        "Lass uns nicht herumstehen.",
    ],
    "nervig": [
        "Das warteln ist so nervig.",
        "Dein Gerede geht mir total auf die Nerven.",
        "Das ist echt nervend.",
        "Die Situation ist mega nervig.",
    ],
    "mitfahren": [
        "Kann ich heute mitfahren?",
        "Sie sind mit dem Zug mitgefahren.",
        "Wir sind zusammen ans Ziel mitgefahren.",
        "Er hat sie im Auto mitfahren lassen.",
    ],
    "Mehrfamilienhaus": [
        "Das Mehrfamilienhaus hat zehn Stockwerke.",
        "In dem Mehrfamilienhaus wohnen viele Familien.",
        "Das neue Mehrfamilienhaus wurde gebaut.",
        "Wir suchen ein Mehrfamilienhaus.",
    ],
    "austoben": [
        "Die Kinder müssen sich draußen austoben.",
        "Er hat sich beim Sport ausgetobt.",
        "Lass dich ruhig austoben!",
        "Nach dem Lernen muss ich mich austoben.",
    ],
    "immerhin": [
        "Immerhin hast du es versucht.",
        "Das Haus ist immerhin günstig.",
        "Es hat immerhin geregnet.",
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
        "Sein Zustand verschlechterte sich rasant.",
    ],
    "Schwerpunkt": [
        "Der Schwerpunkt liegt auf der Wirtschaft.",
        "Wir verlagern den Schwerpunkt.",
        "Der neue Schwerpunkt ist klar.",
        "Das ist unser Schwerpunkt.",
    ],
    "Element": [
        "Jedes Element hat seine Eigenschaften.",
        "Das ist ein wichtiges Element.",
        "Feuer ist eines der Elemente.",
        "Wir studieren die chemischen Elemente.",
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
        "Das ist der einzige Nachteil.",
    ],
    "Grund": [
        "Der Grund ist unbekannt.",
        "Aus welchem Grund?",
        "Der wahre Grund ist das.",
        "Aus diesem Grund kommen wir.",
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
        "Eine wichtige Voraussetzung.",
        "Keine Voraussetzung.",
        "Die Voraussetzung ist erfüllt.",
        "Als Voraussetzung gilt.",
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
    "Reihehaus": [
        "Das Reihenhaus ist modern.",
        "Wir kaufen ein Reihenhaus.",
        "In der Straße stehen Reihenhäuser.",
        "Das Reihenhaus hat einen Garten.",
    ],
    "immerhin": [
        "Immerhin hast du es versucht.",
        "Das Hotel war immerhin sauber.",
        "Immerhin gibt es Kaffee.",
        "Du hast immerhin angerufen.",
    ],
    "aufwerten": [
        "Die Renovierung wertet das Haus auf.",
        "Das Zertifikat wertet den Lebenslauf auf.",
        "Neue Möbel werten die Wohnung auf.",
        "Das verbessert und wertet auf.",
    ],
}


def get_better_example(word, old_example):
    if word in BETTER_EXAMPLES and BETTER_EXAMPLES[word]:
        return random.choice(BETTER_EXAMPLES[word])
    return old_example


def clean_format(tags):
    tags = re.sub(r"\s*\(.*?\)\s*", "", tags)
    tags = tags.replace("|", " | ").replace("  ", " ")
    return tags.strip().strip("|").strip()


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
            continue

        front = parts[0]
        old_example = parts[1]
        tags = parts[2]

        m = re.search(r"\{\{c1::([^:]+)::([^\}]+)\}\}", front)
        if not m:
            continue

        word = m.group(1).strip()

        syn_inner = m.group(2).strip()
        syns = [
            s.strip() for s in syn_inner.split("|") if s.strip() and s.strip() != word
        ]
        syns = syns[:2]
        while len(syns) < 2:
            syns.append("")

        final_syns = " | ".join([s for s in syns if s])

        new_front = f"{{{{c1::{word}::{final_syns}}}}}"

        new_example = get_better_example(word, old_example)

        clean_tags = clean_format(tags)

        output.append(f"{new_front}\t{new_example}\t{clean_tags}")

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
