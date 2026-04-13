# Deutsche Vokabel-Karten für Anki

Deutsche Vokabel-Karten mit über **4.000 Karteikarten** in verschiedenen Kategorien und Formaten.

## Ordner-Struktur

```
German_Decks_v4/           - Hauptkategorien (29 Ordner)
German_Decks_by_Level/    - Nach CEFR-Niveau getrennt (A1, A2, B1, B2)
German_Decks_with_Images/ - Karten mit Bildverweisen
scripts/                  - Python-Hilfsskripte
```

## Kategorien (German_Decks_v4)

| Kategorie | Karten | Beschreibung |
|-----------|-------|--------------|
| Alltag | 716 | Alltagsvokabeln |
| Arbeit | 344 | Berufliche Begriffe |
| Bildung | 197 | Bildungswesen |
| Essen | 30 | Nahrungsmittel |
| Familie | 15 | Familienbeziehungen |
| Gefühle | 15 | Emotionale Zustände |
| Phrasen | 30 | Deutsche Redewendungen |
| Satzmuster | 30 | Satzstrukturen |
| Tiere | 15 | Tiernamen |
| Verben | 30 | Häufige Verben |
| ... | ... | Und mehr! |

**Gesamt: ~4.000 Karten in 29 Kategorien**

## CEFR-Niveaus (German_Decks_by_Level)

- **German_Deck_A1.txt** - 3.974 Karten (Anfänger)
- **German_Deck_A2.txt** - 19 Karten (Grundlagen)
- **German_Deck_B1.txt** - 5 Karten (Mittelstufe)
- **German_Deck_B2.txt** - 1 Karten (Oberstufe)

## Kartformat

Jede Karte hat folgendes Format:

```
{{c1::WORT::SYNONYM1 | SYNONYM2}}	Beispiel-Satz	Wortart;Niveau
```

Beispiel:
```
{{c1::laufen::eilen | rennen}}	Bitte lauf nicht so schnell	Verb;A1
```

## Import in Anki

### Option 1: Einzelne Kategorien
1. Öffne **Anki → Datei → Importieren**
2. Wähle eine `.txt` Datei aus
3. Klicke auf **Importieren**

### Option 2: Alles auf einmal
- Importiere `German_All_in_One.txt` für alle Karten

### Option 3: Nach Niveau
- Nutze Dateien aus `German_Decks_by_Level/`

## Python-Scripts

| Script | Funktion |
|--------|----------|
| `fix_format.py` | Bereinigt Format |
| `improve_decks_v2.py` | Verbessert Beispiele |
| `split_by_level.py` | Teilt nach Niveau |
| `fetch_images.py` | Fügt Bildverweise hinzu |
| `create_apkg.py` | Erstellt Merged-Deck |

### Scripts nutzen

```bash
cd scripts
python3 fix_format.py
python3 split_by_level.py
```

## Neue Karten hinzufügen

### Phrasen (Redewendungen)
- `German_Deck_Phrasen.txt` - 30 häufige Sätze

### Verben (Konjugationen)
- `German_Deck_Verben.txt` - Häufige Verben mit

### Satzmuster
- `German_Deck_Satzmuster.txt` - 30 Satzstrukturen

## CEFR-Niveaus Erklärung

- **A1** - Einfachste Ebene
- **A2** - Grundlagen 
- **B1** - Mittelstufe
- **B2** - Fortgeschritten

## Beitragen

1. Fork das Repository
2. Füge neue Karten hinzu
3. Commit und Push
4. Erstelle einen Pull Request

## Lizenz

 Frei nutzbar.