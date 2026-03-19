import requests

API_URL = "http://127.0.0.1:5000/search?q="
codex = {}

def search_character(name):
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()

        # If API returns a single dict, wrap it in a list
        if isinstance(data, dict):
            data = [data]

        return data
    else:
        print("Character not found.")
        return None

def add_character(name):
    results = search_character(name)
    if results:
        for character in results:
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
    key = name.lower()
    for stored_name, details in list(codex.items()):
        if key in details["name"].lower():
            del codex[stored_name]
            print(f"{stored_name} removed from your CoD-dex.")
            return
    else:
        print("Character not found in your CoD-dex.")
