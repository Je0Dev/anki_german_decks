#!/usr/bin/env python3
import os
import re
import random

INPUT_DIR = "German_Decks_v4"
OUTPUT_DIR = "German_Decks_with_Images"
IMAGE_DIR = "images"

FREE_IMAGE_APIS = [
    "https://source.unsplash.com/300x200/?german,word",
    "https://loremflickr.com/300/200/german,word",
    "https://placehold.co/300x200/1a1a2e/FFFFFF?text=German",
]

WORD_IMAGE_MAP = {
    "der Apfel": "apple",
    "die Katze": "cat",
    "der Hund": "dog",
    "das Haus": "house",
    "das Auto": "car",
    "das Buch": "book",
    "die Schule": "school",
    "der Bahnhof": "train station",
    "das Restaurant": "restaurant",
    "das Hotel": "hotel",
    "der Strand": "beach",
    "der Berg": "mountain",
    "der Wald": "forest",
    "der Fluss": "river",
    "das Wasser": "water",
    "die Sonne": "sun",
    "der Mond": "moon",
    "der Stern": "star",
    "das Pferd": "horse",
    "die Kuh": "cow",
    "das Schaf": "sheep",
    "die Ziege": "goat",
    "das Huhn": "chicken",
    "die Ente": "duck",
    "der Fisch": "fish",
    "die Maus": "mouse",
    "der Hase": "rabbit",
    "das Brot": "bread",
    "der Käse": "cheese",
    "die Milch": "milk",
    "der Kaffee": "coffee",
    "der Tee": "tea",
    "das Bier": "beer",
    "der Wein": "wine",
    "das Wasser": "water",
    "die Orange": "orange",
    "die Banane": "banana",
    "die Erdbeere": "strawberry",
    "der Vogel": "bird",
}


def extract_word(text):
    match = re.search(r"\{\{c1::([^:]+)::", text)
    if match:
        return match.group(1).strip()
    return None


def create_cards_with_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(INPUT_DIR, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        output_lines = []
        image_refs = []

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                output_lines.append(line)
                continue

            word = extract_word(line)
            if word and word in WORD_IMAGE_MAP:
                eng_word = WORD_IMAGE_MAP[word]
                image_url = f'<img src="https://dummyimage.com/300x200/1a1a2e/FFFFFF?text={eng_word.replace(" ", "+")}">'
                image_refs.append(image_url)

            parts = line.split("\t")
            if len(parts) >= 3:
                new_line = f"{parts[0]}\t{parts[1]}\t{parts[2]}"
                output_lines.append(new_line)
            else:
                output_lines.append(line)

        new_filename = filename.replace(".txt", "_Images.txt")
        output_path = os.path.join(OUTPUT_DIR, new_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))

        cards = len([l for l in output_lines if l and not l.startswith("#")])
        img_count = len(image_refs)
        print(f"Done: {filename} -> {new_filename} ({cards} cards, {img_count} images)")


def create_anki_package():
    print("\n=== Creating .apkg files ===")
    print("Note: This requires the anki module")
    print("Install with: pip install anki")
    print("Then run: python3 create_apkg.py")


if __name__ == "__main__":
    create_cards_with_images()
    create_anki_package()
