from characterManager import CharacterManager
from validation import validate_playtime, validate_console, validate_stats
from videoGameCharacter import VideoGameCharacter

def main():
    manager = CharacterManager()
    manager.load_characters('characters.json')

    while True:
        print("\nVideo Game Character Manager")
        print("1. List Characters")
        print("2. Add Character")
        print("3. Remove Character")
        print("4. Search Characters")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.list_characters()
        elif choice == "2":
            game_title = input("Enter game title: ")
            game_description = input("Enter game description: ")
            username = input("Enter creator's username: ")
            console = input("Enter game console (PC, Nintendo, Xbox, PlayStation): ")
            console = validate_console(console)
            abilities = input("Enter character abilities (comma-separated): ").split(',')
            stats = input("Enter character stats (JSON format): ")
            stats = validate_stats(stats)
            character_name = input("Enter character name: ")
            playtime = input("Enter playtime as character (hours): ")
            playtime = validate_playtime(playtime)
            bio = input("Enter character biography: ")
            achievements = input("Enter character achievements (comma-separated): ").split(',')
            
            if console and stats and playtime is not None:
                character = VideoGameCharacter(game_title, game_description, username, console, abilities, stats, character_name, playtime, bio, achievements)
                manager.add_character(character)
                manager.save_characters('characters.json')
                print("Character added.")
            if playtime is not None:
                character = VideoGameCharacter(game_title, game_description, username, console, abilities, stats, character_name, playtime, bio, achievements)
                manager.add_character(character)
                manager.save_characters('characters.json')
                print("Character added.")
        elif choice == "3":
            character_name = input("Enter character name to remove: ")
            manager.remove_character(character_name)
            manager.save_characters('characters.json')
            print("Character removed.")
        elif choice == "4":
            attribute = input("Enter attribute to search by (game_title, username, console, character_name): ")
            value = input("Enter value to search for: ")
            found_characters = manager.search_characters(attribute, value)
            if found_characters:
                for character in found_characters:
                    print(character)
            else:
                print("No characters found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()