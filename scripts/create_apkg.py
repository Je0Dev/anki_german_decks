#!/usr/bin/env python3
import os


def create_apkg_files():
    print("Creating Anki package files...")
    print("""
To create .apkg files, you need to:
1. Install anki: pip install anki
2. Run this script again OR manually import in Anki

For manual import:
1. Open Anki
2. File > Import
3. Select .txt files from German_Decks_v4/

The .apkg format is binary and requires the anki Python library.
""")


def merge_all_decks():
    print("Creating merged deck with all categories...")

    input_dir = "German_Decks_v4"
    output_file = "German_All_in_One.txt"

    all_lines = [
        "#separator:tab",
        "#html:true",
        "#tags column:3",
        "#deck:German Vocabulary::All",
    ]

    for filename in sorted(os.listdir(input_dir)):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(input_dir, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                all_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(all_lines))

    cards = len([l for l in all_lines if l and not l.startswith("#")])
    print(f"Created: {output_file} ({cards} cards)")

    return cards


if __name__ == "__main__":
    create_apkg_files()
    cards = merge_all_decks()
    print(f"\nTotal: {cards} cards in merged deck")
    print("\nImport German_All_in_One.txt into Anki for one-click import!")
