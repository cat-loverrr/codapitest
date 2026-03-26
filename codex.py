import requests
from datetime import datetime


API_URL = "http://127.0.0.1:5000/search?q="
codex = {}


def search_character(name):
    response = requests.get(f"{API_URL}{name.lower()}")
    log_interaction(f"Searched for: {name}")
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
            log_interaction(f"Added: {name}")
    else:
        print("Invalid input.")


def view_codex():
    if codex:
        for name, details in codex.items():
            print(f"{name}")
            print(f"First Appearance: {details['first_appearance']}")
            print(f"Faction: {details['faction']}")
            print(f"Games: {', '.join(details['games'])}")
            print(f"Wiki: {details['wiki_url']}")
            print()
            log_interaction("Viewed CoD-dex")
    else:
        print("Your CoD-dex is empty.")


def remove_character(name):
    key = name.lower()
    for stored_name, details in list(codex.items()):
        if key in details["name"].lower():
            del codex[stored_name]
            print(f"{stored_name} removed from your CoD-dex.")
            log_interaction(f"Removed: {name}")
            return
    else:
        print("Character not found in your CoD-dex.")


def log_interaction(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("interaction_log.txt", "a") as f:
        f.write(f"[{timestamp}] {text}\n")


def view_interaction_log():
    try:
        with open("interaction_log.txt", "r") as f:
            logs = f.readlines()


        if not logs:
            print("No interactions recorded yet.")
            return


        print("\n=== Interaction Log ===")
        for line in logs:
            print(line.strip())
        print("=======================\n")


    except FileNotFoundError:
        print("No interaction log found yet.")


def show_help():
    print("\n=== CoD-dex Help & Troubleshooting ===\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Menu Options:")
    print("1. Search Character – Search by name or keyword. Results return any matching words in your query.  ")
    print("2. Add Character – Adds a character to your CoD-dex.")
    print("3. View CoD-dex – Shows all saved characters.")
    print("4. Remove Character – Removes a character from your CoD-dex.")
    print("6. View Charts – Opens Matplotlib chart options.")
    print("7. View Interaction Log – Shows all logged actions.")
    print("8. Help – Shows this help screen.\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Common Issues & Fixes:")
    print("- 'Character not found': Check spelling or try a broader keyword.")
    print("- 'API not responding': Make sure api.py is running.")
    print("- 'Charts not showing': Ensure Matplotlib is installed.")
    print("- 'No interaction log found': Perform an action first (search/add/remove).")
    print("- 'Invalid choice': Enter a number from the menu.\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Tips:")
    print("- Searches are case-insensitive, meaning that lowercase and caps do not matter.")
    print("- The interaction log refreshes when you run the program.")
    print("- You can run the program as many times as you want.\n")


    print("=======================================\n")


