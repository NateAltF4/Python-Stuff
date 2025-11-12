import random
from typing import Dict, List, Tuple

# ====================
#    Data Templates
# ====================

RACES = {
    "Human": {
        "ability_bonuses": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
        "speed": 30,
        "traits": ["Extra language"],
    },
    "Elf": {
        "ability_bonuses": {"DEX": 2},
        "speed": 30,
        "traits": ["Darkvision", "Keen Senses", "Fey Ancestry"],
    },
    "Dwarf": {
        "ability_bonuses": {"CON": 2},
        "speed": 25,
        "traits": ["Darkvision", "Dwarven Resilience"],
    },
    "Halfling": {
        "ability_bonuses": {"DEX": 2},
        "speed": 25,
        "traits": ["Lucky", "Brave"],
    },
}

CLASSES = {
    "Fighter": {
        "hit_die": 10,
        "primary_abilities": ["STR", "CON"],
        "saving_throws": "CON",
        "proficiency_choices": {"armor": ["All armor", "Shields"], "weapons": ["Simple", "Martial"]},
        "starting_equipment": ["Chain mail or leather + longbow", "Shield", "One martial weapon"],
    },
    "Wizard": {
        "hit_die": 6,
        "primary_abilities": ["INT"],
        "saving_throws": "INT",
        "proficiency_choices": {"weapons": ["Daggers", "Quarterstaffs"]},
        "starting_equipment": ["Spellbook", "Component pouch"],
    },
    "Rogue": {
        "hit_die": 8,
        "primary_abilities": ["DEX"],
        "saving_throws": "DEX",
        "proficiency_choices": {"skills": 4},
        "starting_equipment": ["Leather armor", "Two daggers", "Thieves' tools"],
    },
    "Cleric": {
        "hit_die": 8,
        "primary_abilities": ["WIS"],
        "saving_throws": "WIS",
        "proficiency_choices": {"weapons": ["Simple"], "armor": ["Light", "Medium", "Shields"]},
        "starting_equipment": ["Holy symbol", "Mace"],
    },
}

BACKGROUNDS = {
    "Soldier": {
        "skills": ["Athletics", "Intimidation"],
        "tool_proficiencies": ["Gaming set"],
        "equipment": ["Insignia of rank", "Trophy from a fallen enemy"],
    },
    "Sage": {
        "skills": ["Arcana", "History"],
        "tool_proficiencies": [],
        "equipment": ["Bottle of black ink", "Quill"],
    },
    "Criminal": {
        "skills": ["Deception", "Stealth"],
        "tool_proficiencies": ["Thieves' tools"],
        "equipment": ["Crowbar", "Dark clothes"],
    },
    "Folk Hero": {
        "skills": ["Animal Handling", "Survival"],
        "tool_proficiencies": ["Land vehicles"],
        "equipment": ["A small token", "Set of artisan tools"],
    },
}

ALL_ABILITIES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

# ====================
#       Utility
# ====================

def ability_modifier(score: int) -> int:
    return (score - 10) // 2

def roll_dice(n: int, f: int) -> List[int]:
    # n - how many dice are rolled
    # d - how many faces
    return [random.randint(1, f) for i in range(n)]

def roll_4d6_drop_lowest() -> int:
    rolls = roll_dice(4, 6)
    rolls.sort()
    return sum(rolls[1:])  # drop lowest

# ====================
#    Accessing Data
# ====================

def get_race(race: str):
    return RACES[race]

def get_class(Class: str):
    return CLASSES[Class]

def get_background(background: str):
    return BACKGROUNDS[background]

# ====================
#   Formatting Data
# ==================== 

def get_race_info(race_name):
    # Retrieve information about a specific race.
    race = RACES.get(race_name)
    if not race:
        print(f"Race '{race_name}' not found.")
        return
    print(f"\n--- {race_name} ---")
    print(f"Speed: {race['speed']}")
    print(f"Ability Bonuses: {race['ability_bonuses']}")
    print(f"Traits: {', '.join(race['traits'])}")


def get_class_info(class_name):
    # Retrieve information about a specific class.
    cls = CLASSES.get(class_name)
    if not cls:
        print(f"Class '{class_name}' not found.")
        return
    print(f"\n--- {class_name} ---")
    print(f"Hit Die: d{cls['hit_die']}")
    print(f"Primary Abilities: {', '.join(cls['primary_abilities'])}")
    print(f"Saving Throw: {cls['saving_throws']}")
    print(f"Proficiencies: {cls['proficiency_choices']}")
    print(f"Starting Equipment: {', '.join(cls['starting_equipment'])}")


def get_background_info(background_name):
    # Retrieve information about a specific background.
    bg = BACKGROUNDS.get(background_name)
    if not bg:
        print(f"Background '{background_name}' not found.")
        return
    print(f"\n--- {background_name} ---")
    print(f"Skills: {', '.join(bg['skills'])}")
    print(f"Tool Proficiencies: {', '.join(bg['tool_proficiencies']) or 'None'}")
    print(f"Equipment: {', '.join(bg['equipment'])}")

# ====================
#  Character Builder
# ====================

def pick_race():
    while True:
        try:
            race = int(input("Race: \n1. Human\n2. Elf\n3. Dwarf\n4. Halfling\n0. Random\nPick a number: "))
            if race in [0, 1, 2, 3, 4]:
                break
            else:
                print("Invalid input, please pick a number between 1 and 4. ")
        except ValueError:
            print("Invalid input, please pick a number between 1 and 4. ")
    
    if race == 0:
        race = random.randint(1, 4)
        print(race)

    if race == 1:
        print("You selected Human!\n")
        get_race("Human")
    elif race == 2:
        print("You selected Elf!\n")
        get_race("Elf")
    elif race == 3:
        print("You selected Dwarf!\n")
        get_race("Dwarf")
    elif race == 4:
        print("You selected Halfling!\n")
        get_race("Halfling")

def pick_class():
    while True:
        try:
            Class = int(input("Class: \n1. Fighter\n2. Wizard\n3. Rogue\n4. Cleric\nPick a number: "))
            if Class in [0, 1, 2, 3, 4]:
                break
            else:
                print("Invalid input, please pick a number between 1 and 4. ")
        except ValueError:
            print("Invalid input, please pick a number between 1 and 4. ")
    if Class == 0:
        Class = random.randint(1, 4)
        print(Class)

    if Class == 1:
        print("You selected Fighter!\n")
        get_class("Fighter")
    elif Class == 2:
        print("You selected Wizard!\n")
        get_class("Wizard")
    elif Class == 3:
        print("You selected Rogue!\n")
        get_class("Rogue")
    elif Class == 4:
        print("You selected Cleric!\n")
        get_class("Cleric")    

def pick_background():
    while True:
        try:
            background = int(input("Background: \n1. Soldier\n2. Sage\n3. Criminal\n4. Folk Hero\nPick a number: "))
            if background in [0, 1, 2, 3, 4]:
                break
            else:
                print("Invalid input, please pick a number between 1 and 4. ")
        except ValueError:
            print("Invalid input, please pick a number between 1 and 4. ")
    
    if background == 0:
        background = random.randint(1, 4)
        print(background)

    if background == 1:
        print("You selected Soldier!\n")
        get_background("Soldier")
    elif background == 2:
        print("You selected Sage!\n")
        get_background("Sage")
    elif background == 3:
        print("You selected Criminal!\n")
        get_background("Criminal")
    elif background == 4:
        print("You selected Folk Hero!\n")
        get_background("Folk Hero")

def stat_select():
    while True:
        try:
            print("How do you want to assign your stats?\n1. Rolling (recommended)\n2. Points buy (27 pts)\n3. Standard array")
            choice = int(input("Pick a number: "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid, please pick a number between 1 and 3")
        except ValueError:
            print("Invalid, please pick a number between 1 and 3")

    if choice == 1:
        order = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        scores = []
        character_scores = []
        for i in range(6):
            roll = roll_4d6_drop_lowest()
            scores.append(roll)
        scores = sorted(scores, reverse=True)
        print(f"Your rolls are: {scores}")

        for i in range(6):
            assign = input(f"What would you like to assign {scores[i]} to? Please select {ALL_ABILITIES} ")
            while True:
                if assign.upper() not in ALL_ABILITIES:
                    assign = input(f"Invalid choice, please pick one of the following: {ALL_ABILITIES} ")
                else:
                    character_scores.append(f"{assign.upper()}: {scores[i]}")
                    ALL_ABILITIES.remove(assign.upper())
                    break
        
        character_scores.sort(key=lambda x: order.index(x.split(':')[0]))
        print(character_scores)
            

def create_character():
    pick_race()
    pick_class()
    pick_background()

# ====================
#        Main
# ====================

create_character()