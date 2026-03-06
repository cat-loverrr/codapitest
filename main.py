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

        if choice == "1":
            name = input("Enter character name: ").strip()
            result = search_character(name)
            if result:
                for key, value in result.items():
                    print(f"{key}: {value}")

        elif choice == "2":
            name = input("Enter character name to add: ").strip()
            add_character(name)

        elif choice == "3":
            view_codex()

        elif choice == "4":
            name = input("Enter character name to remove: ").strip()
            remove_character(name)

        elif choice == "5":
            print("Exiting CoD-dex.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

