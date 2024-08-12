import json

class VideoGameCharacter:
    def __init__(self, game_title, game_description, username, console, abilities, stats, character_name, playtime, bio, achievements):
        self.game_title = game_title
        self.game_description = game_description
        self.username = username
        self.console = console
        self.abilities = abilities
        self.stats = stats
        self.character_name = character_name
        self.playtime = playtime
        self.bio = bio
        self.achievements = achievements

    def __string__(self):
        return f"{self.character_name} in {self.game_title} ({self.console}) by {self.username} - Playtime: {self.playtime} hours"
    
class RPGCharacter(VideoGameCharacter):
    def __init__(self, level, class_type, equipment, **kwargs):
        super().__init__(**kwargs)
        self.level = level
        self.class_type = class_type
        self.equipment = equipment

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Level: {self.level}, Class: {self.class_type}, Equipment: {self.equipment}"

