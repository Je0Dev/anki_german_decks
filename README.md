# Deutsche Vokabel-Karten für Anki

Willkommen zu den deutschen Vokabel-Karten! Diese Sammlung enthält über 5.000 Karteikarten in 29 Kategorien.

## Kategorien

### Bestehende Kategorien
- **Alltag** (716 Karten) - Alltagsvokabeln
- **Arbeit** (344) - Berufliche Begriffe
- **Bildung** (197) - Bildungswesen
- **Emotionen** (15) - Gefühle und Emotionen
- **Essen** (30) - Nahrungsmittel
- **Familie** (15) - Familienbeziehungen
- **Finanzen** (26) - Finanzbegriffe
- **Gaming** (48) - Gaming-Sprache
- **Geschichte** (30) - Geschichtsbegriffe
- **Gesellschaft** (218) - Gesellschaft
- **Gesundheit** (65) - Gesundheit
- **Gefühle** (15) - Emotionale Zustände
- **Immobilien** (21) - Immobilien
- **Kunst** (39) - Kunst
- **Medien** (13) - Medien
- **Musik** (14) - Musik
- **Natur** (102) - Natur
- **Philosophie** (43) - Philosophie
- **Recht** (27) - Recht
- **Reisen** (70) - Reisen
- **Religion** (8) - Religion
- **Sonstiges** (1494) - Sonstiges
- **Sport** (29) - Sport
- **Sprache** (73) - Sprache
- **Technologie** (134) - Technologie
- **Tiere** (15) - Tiernamen
- **Wetter** (15) - Wetter
- **Wirtschaft** (70) - Wirtschaft
- **Wissenschaft** (23) - Wissenschaft

## Import in Anki

### Methode 1: Direkter Import

1. Öffne Anki auf deinem Computer
2. Gehe zu **Datei → Importieren**
3. Wähle eine der `.txt` Dateien aus
4. Klicke auf **Importieren**

### Methode 2: Alle Kategorien importieren

1. Wiederhole Methode 1 für jede gewünschte Kategorie
2. Die Karten werden automatisch in die richtigen Decks sortiert

## Kartformat

Jede Karte hat folgendes Format:

- **Vorderseite**: Deutsche Frage mit Lückentext (Cloze) + 2 Synonyme
- **Rückseite**: Natürliches Beispiel für die Verwendung
- **Tags**: Wortart + CEFR-Niveau

Beispiel:
```
Vorderseite: {{c1::laufen|eilen}}
Rückerseite: Bitte lauf nicht so schnell
Tags: Verb;A1
```

## CEFR-Niveaus

Die Karten sind mit Niveaus markiert:
- **A1** - Anfänger
- **A2** - Grundlagen
- **B1** - Mittelstufe
- **B2** - Oberstufe

## Python-Scripts

Im Ordner `scripts/` befinden sichHilfsskripte:

- `transform_vocab.py` - Wandelt alte Formate in neue um
- `fix_format.py` - Bereinigt Format und Grammatik
- `improve_decks_v2.py` - Verbessert Beispiele

### Scripts nutzen

```bash
python3 scripts/transform_vocab.py
python3 scripts/fix_format.py
python3 scripts/improve_decks_v2.py
```

## Lerntipps

1. Lerne täglich 20-30 neue Karten
2. Wiederhole die Karten regelmäßig
3. Nutze die Filterfunktion nach Niveau
4. Erstelle zusätzliche eigene Karten

##Lizenz

Diese Karten sind frei nutzbar.

## Kontakt

Bei Fragen oder Verbesserungsvorschlägen bitte melden.