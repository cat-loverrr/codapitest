import requests
from datetime import datetime

# Base URL for the Flask API search endpoint.
# The program appends the user's search term to this URL.
API_URL = "http://127.0.0.1:5000/search?q="
# Dictionary storing all characters the user has added
# to their personal CoD-dex. Keys = character names.
codex = {}

# Sends a GET request to the API using the user's search term.
# Logs the search action, handles both list and single-dict responses,
# and returns the matching character data.
def search_character(name):
    response = requests.get(f"{API_URL}{name.lower()}")
    log_interaction(f"Searched for: {name}")
    # If the API request succeeds
    if response.status_code == 200:
        data = response.json()


        # If API returns a single dict, wrap it in a list
        if isinstance(data, dict):
            data = [data]


        return data
    #If no character is found
    else:
        print("Character not found.")
        return None

# Searches for a character and adds all matching results
# to the user's CoD-dex dictionary.
def add_character(name):
    results = search_character(name)
    if results:
        for character in results:
            codex[character["name"]] = character
            print(f"{character['name']} added to your CoD-dex.")
            log_interaction(f"Added: {name}")
    else:
        print("Invalid input.")

# Displays all characters currently stored in the user's CoD-dex.
# Shows key details for each character and logs the action.
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

# Removes a character whose name contains the user's input.
# Matching is case-insensitive and supports partial matches.
def remove_character(name):
    key = name.lower()
    # Convert codex.items() to a list to avoid runtime modification issues
    for stored_name, details in list(codex.items()):
        if key in details["name"].lower():
            del codex[stored_name]
            print(f"{stored_name} removed from your CoD-dex.")
            log_interaction(f"Removed: {name}")
            return
    else:
        print("Character not found in your CoD-dex.")

# Writes a timestamped entry to interaction_log.txt.
# Used for tracking all user actions in the program.
def log_interaction(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("interaction_log.txt", "a") as f:
        f.write(f"[{timestamp}] {text}\n")

# Reads and prints all logged user actions.
# Handles missing log files gracefully.
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

# Displays instructions, menu explanations, common issues,
# and general usage tips for the CoD-dex program.
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


