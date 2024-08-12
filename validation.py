import json

def validate_playtime(playtime):
    try:
        playtime = float(playtime)
        if playtime < 0:
            raise ValueError("Playtime must be non-negative number.")
        return playtime
    except ValueError as e:
        print(f"Invalid playtime: {e}")
        return None
    
def validate_console(console):
    valid_consoles = ["PC", "Nintendo", "Xbox", "Playstation"]
    if console not in valid_consoles:
        print(f"Invalid Console. Please choose from {valid_consoles}.")
        return None
    return console

def validate_stats(stats):
    try:
        stat_dict = json.loads(stats)
        if not all(isinstance(value, int) for value in stat_dict.values()):
            raise ValueError("Stats must be integers.")
        return stat_dict
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Invalid stats: {e}")
        return None