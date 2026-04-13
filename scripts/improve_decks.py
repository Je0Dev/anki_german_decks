#!/usr/bin/env python3
import os
import re
import random

OUTPUT_DIR = "German_Decks_v4"

BETTER_EXAMPLES = {
    "herum": [
        "Ich muss immer an etwas Bestimmtes denken.",
        "Lass uns einfach drauflos arbeiten.",
        "Sie hat das Problem einfach ignoriert.",
    ],
    "nervig": [
        "Das Warten ist so nervig.",
        "Dein ständiges Jammern geht mir auf die Nerven.",
        "Diese Situation ist echt nervend.",
    ],
    "mitfahren": [
        "Kann ich mitfahren?",
        "Sie sind mit dem Auto mitgefahren.",
        "Wir sind zusammen mitgefahren.",
    ],
    "Mehrfamilienhaus": [
        "Das Mehrfamilienhaus hat zehn Stockwerke.",
        "In dem Mehrfamilienhaus wohnen viele Familien.",
        "Das Mehrfamilienhaus wurde renoviert.",
    ],
    "austoben": [
        "Die Kinder müssen sich austoben können.",
        "Er hat sich im Sport ausgetobt.",
        "Lass dich ruhig austoben!",
    ],
    "immerhin": [
        "Immerhin hast du es versucht.",
        "Das Haus ist immerhin bezahlbar.",
        "Immerhin hat es geregnet.",
    ],
    "austauschen": [
        "Wir sollten unsere Nummern austauschen.",
        "Er hat die Batterie ausgetauscht.",
        "Die Meinungen wurden ausgetauscht.",
    ],
    "rasant": [
        "Die Stadt wächst rasant.",
        "Die Technologie entwickelt sich rasant.",
        "Sein Zustand verschlechterte sich rasant.",
    ],
    "Schwerpunkt": [
        "Der Schwerpunkt liegt auf der Wirtschaft.",
        "Wir verlagern den Schwerpunkt.",
        "Der Schwerpunkt hat sich verschoben.",
    ],
    "Element": [
        "Jedes Element hat seine Eigenschaften.",
        "Das ist ein wichtiges Element.",
        "Feuer ist eines der vier Elemente.",
    ],
    "aufwerten": [
        "Die Renovierung wertet die Wohnung auf.",
        "Qualifikationen werten den Lebenslauf auf.",
        "Das verbessert das Image.",
    ],
}


def clean_grammar(text):
    text = re.sub(r"\s*\(der/die/das\)\s*", "", text)
    text = re.sub(r"\s*\(regelmäßig\)\s*", "", text)
    text = re.sub(r"\s*\([^)]+\)\s*", "", text)
    return text.strip()


def improve_card(line):
    parts = line.split("\t")
    if len(parts) < 3:
        return None

    front = parts[0]
    back_example = parts[1]
    tags = parts[2]

    match = re.search(r"\{\{c1::([^:]+)::([^\}]+)\}\}", front)
    if not match:
        return None

    word = match.group(1).strip()
    syns_raw = match.group(2).strip()
    syns = [s.strip() for s in syns_raw.split("|") if s.strip()]

    syns = [s for s in syns if s][:2]
    while len(syns) < 2:
        syns.append("")

    synonyms_str = " | ".join([s for s in syns if s])

    new_front = f"{{{{c1::{word}::{synonyms_str}}}}}"
    new_back = back_example.strip()
    new_tags = tags.split(";")[0] + ";" + (tags.split(";")[-1] if ";" in tags else "A1")

    return f"{new_front}\t{new_back}\t{new_tags}"


def process_all_decks():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    input_dir = "German_Decks_v3"

    for filename in os.listdir(input_dir):
        if not filename.endswith(".txt"):
            continue

        input_path = os.path.join(input_dir, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        output_lines = []

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                output_lines.append(line)
                continue

            improved = improve_card(line)
            if improved:
                output_lines.append(improved)
            else:
                output_lines.append(line)

        output_filename = filename.replace("v3", "v4")
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))

        card_count = len([l for l in output_lines if l and not l.startswith("#")])
        print(f"Done: {filename} -> {output_filename} ({card_count} cards)")


if __name__ == "__main__":
    process_all_decks()
