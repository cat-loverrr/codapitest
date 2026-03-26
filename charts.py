import matplotlib.pyplot as plt
from collections import Counter
from api import character_list
from codex import codex

# This function counts how many characters belong to each
# faction and displays the results as a bar chart.
#
# Steps:
# 1. Extract the primary faction for each character.
# 2. Count how many characters belong to each faction.
# 3. Plot the results using Matplotlib.
def plot_characters_per_faction():
    # Extract the first faction listed (before any semicolon)
    factions = [c["faction"].split(";")[0].strip() for c in character_list]
    # Count how many times each faction appears
    counts = Counter(factions)

    # Create a bar chart showing faction counts
    plt.bar(counts.keys(), counts.values())
    plt.xticks(rotation=45, ha="right") # Rotate labels for readability
    plt.title("Characters per Faction")
    plt.ylabel("Number of Characters")
    plt.tight_layout() # Prevent label cutoff
    plt.show()



# This function counts how many characters appear in each
# Call of Duty game and displays the results as a bar chart.
#
# Steps:
# 1. Collect all game titles from every character.
# 2. Count how many characters appear in each game.
# 3. Plot the results using Matplotlib.
def plot_characters_per_game():
    games = []
    # Add all games from each character into a single list
    for c in character_list:
        games.extend(c["games"])

    # Count how many characters appear in each game
    counts = Counter(games)

    # Create a bar chart showing game counts
    plt.bar(counts.keys(), counts.values())
    plt.xticks(rotation=45, ha="right")
    plt.title("Characters per Game")
    plt.ylabel("Number of Characters")
    plt.tight_layout()
    plt.show()



# This function shows how many characters the user has added
# to their personal CoD-dex compared to the total available.
#
# Steps:
# 1. Count total characters in the dataset.
# 2. Count how many characters the user has collected.
# 3. Calculate how many remain.
# 4. Display a pie chart showing progress.
def plot_codex_progress():
    total = len(character_list) # Total characters available
    collected = len(codex)  # Characters user has added
    remaining = total - collected # Characters not yet collected

    # Labels and values for the pie chart
    labels = ["Collected", "Remaining"]
    sizes = [collected, remaining]
    colors = ["green", "gray"]

    # Create a pie chart showing collection progress
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors)
    plt.title("Your CoD-dex Progress")
    plt.show()


