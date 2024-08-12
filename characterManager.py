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