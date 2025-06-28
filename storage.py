import json

def load_books(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(filename, books):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([b.to_dict() for b in books], f, indent=4, ensure_ascii=False)
