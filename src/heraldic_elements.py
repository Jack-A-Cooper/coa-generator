# heraldic_elements.py

import os
import random

# Dictionary of Heraldic Colors
HERALDIC_COLORS = {
    'Metals': {
        'Argent': (255, 255, 255), # Silver (often represented with white)
        'Or': (255, 215, 0)       # Gold (often represented with yellow)
    },
    'Colours': {
        'Gules': (255, 0, 0),     # Red
        'Sable': (0, 0, 0),       # Black
        'Azure': (0, 0, 255),     # Blue
        'Vert': (0, 128, 0),      # Green
        'Purpure': (128, 0, 128)  # Purple
    },
    'Furs': {
        'Ermine': (252, 252, 252),   # White with black spots (stoat fur)
        'Ermines': (0, 0, 0),        # Black with white spots
        'Erminois': (255, 215, 0),   # Gold with black spots
        'Pean': (0, 0, 0),           # Black with gold spots
        'Vair': (173, 216, 230),     # Blue-grey and white
        'Potent': (173, 216, 230)    # Variant of vair
    }
}

# Helper function to get RGB color from HERALDIC_COLORS
def get_rgb_color(tincture_name):
    for category in HERALDIC_COLORS.values():
        if tincture_name in category:
            return category[tincture_name]
    return (255, 255, 255)  # Default to white if color not found

def check_rule_of_tincture(tincture1, tincture2):
    colors = heraldic_elements['tinctures']['colors']
    metals = heraldic_elements['tinctures']['metals']
    
    if (tincture1 in colors and tincture2 in colors) or (tincture1 in metals and tincture2 in metals):
        return False
    return True

class Charge:
    def __init__(self, name, image_path, symbolism):
        self.name = name
        self.image_path = image_path
        self.symbolism = symbolism

    def __repr__(self):
        return f"{self.name} ({self.symbolism})"

def load_charges(directory='../assets/charges'):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    charges = []
    for filename in os.listdir(directory):
        if filename.endswith('.svg'):
            name = os.path.splitext(filename)[0]
            path = os.path.join(directory, filename)
            charges.append(Charge(name, path, name))
    return charges

heraldic_elements = {
    "tinctures": {
        "colors": ["Gules", "Azure", "Vert", "Sable", "Purpure"],
        "metals": ["Or", "Argent"],
        "furs": ["Ermine", "Ermines", "Erminois", "Pean", "Vair", "Potent"]
    },
    "divisions": [
        "Pale", "Fess", "Quarterly", "Cross", "Saltire", "Per Bend", "Per Bend Sinister",
        "Per Fess", "Per Pale", "Per Saltire", "Gyronny"
    ],
    "charges": {
        "loaded": load_charges()
    },
    "ordinaries": [
        "Chief", "Bend", "Fess", "Pale", "Cross", "Saltire", "Pile", "Pall", "Bordure", "Orle", "Flaunches"
    ]
}
