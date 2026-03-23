from codex import *
from charts import (
    plot_characters_per_faction,
    plot_characters_per_game,
    plot_codex_progress
)

def main():
    while True:
        print("\nCall of Duty Character Index:")
        print("1. Search Character")
        print("2. Add Character to CoD-dex")
        print("3. View CoD-dex")
        print("4. Remove Character")
        print("5. Exit")
        print("6. View Charts")

        choice = input("Choose an option: ").strip()

        # SEARCH CHARACTER
        if choice == "1":
            name = input("Enter character name or keyword: ").strip()
            results = search_character(name)

            if results:
                print(f"\nFound {len(results)} result(s):")
                for character in results:
                    print("\n--- Character ---")
                    for key, value in character.items():
                        print(f"{key}: {value}")
            else:
                print("No matching characters found.")

        # ADD CHARACTER
        elif choice == "2":
            name = input("Enter character name to add: ").strip()
            add_character(name)

        # VIEW CODEX
        elif choice == "3":
            view_codex()

        # REMOVE CHARACTER
        elif choice == "4":
            name = input("Enter character name to remove: ").strip()
            remove_character(name)

        # EXIT
        elif choice == "5":
            print("Exiting CoD-dex.")
            break

        # VIEW CHARTS
        elif choice == "6":
            print("\nCharts:")
            print("1. Characters per Faction")
            print("2. Characters per Game")
            print("3. CoD-dex Progress")

            chart_choice = input("Choose a chart: ").strip()

            if chart_choice == "1":
                plot_characters_per_faction()
            elif chart_choice == "2":
                plot_characters_per_game()
            elif chart_choice == "3":
                plot_codex_progress()
            else:
                print("Invalid chart option.")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
