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

def get_class(cls: str):
    return CLASSES[cls]

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
        return "Human" 
    elif race == 2:
        print("You selected Elf!\n")
        get_race("Elf")
        return "Elf" 
    elif race == 3:
        print("You selected Dwarf!\n")
        get_race("Dwarf")
        return "Dwarf" 
    elif race == 4:
        print("You selected Halfling!\n")
        get_race("Halfling")
        return "Halfling" 

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
        return "Fighter" 
    elif Class == 2:
        print("You selected Wizard!\n")
        get_class("Wizard")
        return "Wizard" 
    elif Class == 3:
        print("You selected Rogue!\n")
        get_class("Rogue")
        return "Rogue" 
    elif Class == 4:
        print("You selected Cleric!\n")
        get_class("Cleric")
        return "Cleric"    

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
        return "soldier"
    elif background == 2:
        print("You selected Sage!\n")
        get_background("Sage")
        return "sage"
    elif background == 3:
        print("You selected Criminal!\n")
        get_background("Criminal")
        return "Criminal" 
    elif background == 4:
        print("You selected Folk Hero!\n")
        get_background("Folk Hero")
        return "Folk Hero" 

def stat_select(race_name, class_name):
    # Accessing data from dataset
    race = get_race(race_name)
    cls = get_class(class_name)

    available_abilities = ALL_ABILITIES.copy()
    
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

    # Picking how you want to assign your stats
    if choice == 1:
        order = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        scores = []
        character_scores = {}
        
        # Rolling 4d6 and dropping lowest
        for i in range(6):
            roll = roll_4d6_drop_lowest()
            scores.append(roll)
        scores = sorted(scores, reverse=True)
        print(f"Your rolls are: {scores}")

        # Assigning scores
        for i in range(6):
            assign = input(f"What would you like to assign {scores[i]} to? Please select {available_abilities}."
                           f"\nDo note your chosen class is {class_name}, which has the primary stats of {cls['primary_abilities']} "
            )
            while True:
                if assign.upper() not in available_abilities:
                    assign = input(f"Invalid choice, please pick one of the following: {available_abilities} ")
                else:
                    character_scores[assign.upper()] = scores[i]
                    available_abilities.remove(assign.upper())
                    break

        # Applying racial bonuses
        print(f"\nApplying racial bonuses for {race_name}...")
        for ability, bonus in race["ability_bonuses"].items():
            if ability in character_scores:
                character_scores[ability] += bonus
                print(f"  +{bonus} to {ability} (now {character_scores[ability]})")
        
        # Sorting scores
        print("\nFinal Ability Scores (after racial bonuses):")
        for ability in order:
            print(f"{ability}: {character_scores[ability]}")
            
    elif choice == 2:
        costs = {9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9}
        scores = {a: 8 for a in ALL_ABILITIES}
        points = 27

def create_character():
    # Choosing race, class, and background
    chosen_race = pick_race()
    chosen_class = pick_class()
    chosen_background = pick_background()

    # Selecting Stats
    

# ====================
#        Main
# ====================

