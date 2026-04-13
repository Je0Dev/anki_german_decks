#!/usr/bin/env python3
import os
import re
import shutil

INPUT_DIR = "German_Decks_v4"
OUTPUT_DIR = "German_Decks_by_Level"

LEVELS = {"A1": [], "A2": [], "B1": [], "B2": []}


def extract_level(tags):
    if ";A1" in tags:
        return "A1"
    elif ";A2" in tags:
        return "A2"
    elif ";B1" in tags:
        return "B1"
    elif ";B2" in tags:
        return "B2"
    return "A1"


def process_all_decks():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(INPUT_DIR, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split("\t")
            if len(parts) < 3:
                continue

            tags = parts[2]
            level = extract_level(tags)
            LEVELS[level].append(line)

    for level, cards in LEVELS.items():
        output_file = os.path.join(OUTPUT_DIR, f"German_Deck_{level}.txt")
        header = f"#separator:tab\n#html:true\n#tags column:3\n#deck:German Vocabulary::{level}\n"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(header + "\n".join(cards))

        print(f"Created: {output_file} ({len(cards)} cards)")


if __name__ == "__main__":
    process_all_decks()
