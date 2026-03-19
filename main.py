from codex import *

def main():
    while True:
        print("\nCall of Duty Character Index:")
        print("1. Search Character")
        print("2. Add Character to CoD-dex")
        print("3. View CoD-dex")
        print("4. Remove Character")
        print("5. Exit")

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

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
