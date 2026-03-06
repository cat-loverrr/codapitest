import requests

API_URL = "http://127.0.0.1:5000/characters/"
codex = {}

def search_character(name):
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        codex = {
            "name": data["name"].capitalize(),
            "games": data["games"],
            "faction": data["faction"],
            "first_appearance": data["first_appearance"],
            "wiki_url": data["wiki_url"]
            }
        return codex
    else:
        print("Character not found.")
        return None

def add_character(name):
    character = search_character(name)
    if character:
        codex[character["name"]] = character
        print(f"{character['name']} added to your CoD-dex.")

def view_codex():
    if codex:
        for name, details in codex.items():
            print(f"{name}")
            print(f"First Appearance: {details['first_appearance']}")
            print(f"Faction: {details['faction']}")
            print(f"Games: {', '.join(details['games'])}")
            print(f"Wiki: {details['wiki_url']}")
            print()
    else:
        print("Your CoD-dex is empty.")

def remove_character(name):
    formatted = name.title()
    if formatted in codex:
        del codex[formatted]
        print(f"{formatted} removed from your CoD-dex.")
    else:
        print("Character not found in your CoD-dex.")

