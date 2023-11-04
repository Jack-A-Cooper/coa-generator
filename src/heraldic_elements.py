# heraldic_elements.py
# Defines the elements and rules for heraldry within the coat of arms generation system

import random

class Charge:
    def __init__(self, name, image_path, symbolism):
        self.name = name
        self.image_path = image_path
        self.symbolism = symbolism

    def __repr__(self):
        return f"{self.name} ({self.symbolism})"

# Defining possible tinctures, divisions, and charges with their symbolism
heraldic_elements = {
    "tinctures": {
        "colors": ["Gules", "Azure", "Vert", "Sable"],
        "metals": ["Or", "Argent"]
    },
    "divisions": [
        "Pale", "Fess", "Chevron", "Cross", "Saltire"
    ],
    "charges": {
        "animals": [
            Charge("Lion", "path/to/lion/image.png", "Bravery"),
            Charge("Eagle", "path/to/eagle/image.png", "Perspective and clarity"),
            Charge("Wolf", "path/to/wolf/image.png", "Ferocity and strength"),
            Charge("Dragon", "path/to/dragon/image.png", "Protection and power"),
        ],
        "objects": [
            Charge("Sword", "path/to/sword/image.png", "Justice and military honour"),
            Charge("Castle", "path/to/castle/image.png", "Safety and home"),
            Charge("Crown", "path/to/crown/image.png", "Authority and royalty"),
            Charge("Anchor", "path/to/anchor/image.png", "Hope and steadfastness"),
        ]
    },
    "ordinaries": [
        "Chief", "Bend", "Fess", "Pale", "Chevron", "Cross", "Saltire"
    ],
    "rules_of_tincture": {
        "color_on_color": False,
        "metal_on_metal": False
    }
}

# Rule of Tincture: A function to check that metal is not placed on metal and color is not placed on color
def check_rule_of_tincture(tincture1, tincture2):
    colors = heraldic_elements['tinctures']['colors']
    metals = heraldic_elements['tinctures']['metals']
    if (tincture1 in colors and tincture2 in colors) or \
       (tincture1 in metals and tincture2 in metals):
        return False
    return True

# Select a random element from a list, optionally excluding some elements
def select_element(elements, avoid_list=None):
    avoid_list = avoid_list or []
    choices = [element for element in elements if element not in avoid_list]
    return random.choice(choices) if choices else None

# Example usage of selecting a charge
selected_charge = select_element(heraldic_elements['charges']['animals'] + heraldic_elements['charges']['objects'])
print(f"Selected charge: {selected_charge}")

# Example usage of rule of tincture
tincture1 = select_element(heraldic_elements['tinctures']['colors'] + heraldic_elements['tinctures']['metals'])
tincture2 = select_element(heraldic_elements['tinctures']['colors'] + heraldic_elements['tinctures']['metals'])
while not check_rule_of_tincture(tincture1, tincture2):
    tincture2 = select_element(heraldic_elements['tinctures']['colors'] + heraldic_elements['tinctures']['metals'])
print(f"Selected tinctures: {tincture1}, {tincture2} - Rule of tincture check: {check_rule_of_tincture(tincture1, tincture2)}")

# ... Other functions or classes for divisions, ordinaries, etc. can be similarly defined.
