import json

from videoGameCharacter import VideoGameCharacter, RPGCharacter


class CharacterManager:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def find_character_by_name(self, character_name):
        for character in self.characters:
            if character.character_name == character.name:
                return character
        return None
    
    def search_characters(self, attribute, value):
        found_characters = [character for character in self.characters if getattr(character, attribute, None) == value]
        return found_characters
    
    def remove_character(self, character_name):
        character = self.find_character_by_name(character_name)
        if character:
            self.characters.remove(character)

    def list_characters(self):
        for character in self.characters:
            print(character)

    def load_characters(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for character_data in data:
                    if 'level' in character_data:
                        character = RPGCharacter(**character_data)
                    else:
                        character = VideoGameCharacter(**character_data)
                    self.add_character(character)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading characters: {e}")

    def save_characters(self, filename):
        with open(filename, 'w') as file:
            data = []
            for character in self.characters:
                char_dict = character.__dict__.copy()
                if isinstance(character, RPGCharacter):
                    char_dict['type'] = 'RPGCharacter'
                else:
                    char_dict['type'] = 'VideoGameCharacter'
                data.append(char_dict)
            json.dump(data, file, indent=4)