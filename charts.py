import matplotlib.pyplot as plt
from collections import Counter
from api import character_list
from codex import codex

def plot_characters_per_faction():
    factions = [c["faction"].split(";")[0].strip() for c in character_list]
    counts = Counter(factions)

    plt.bar(counts.keys(), counts.values())
    plt.xticks(rotation=45, ha="right")
    plt.title("Characters per Faction")
    plt.ylabel("Number of Characters")
    plt.tight_layout()
    plt.show()


def plot_characters_per_game():
    games = []
    for c in character_list:
        games.extend(c["games"])

    counts = Counter(games)

    plt.bar(counts.keys(), counts.values())
    plt.xticks(rotation=45, ha="right")
    plt.title("Characters per Game")
    plt.ylabel("Number of Characters")
    plt.tight_layout()
    plt.show()


def plot_codex_progress():
    total = len(character_list)
    collected = len(codex)
    remaining = total - collected

    labels = ["Collected", "Remaining"]
    sizes = [collected, remaining]
    colors = ["green", "gray"]

    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors)
    plt.title("Your CoD-dex Progress")
    plt.show()
