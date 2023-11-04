# coat_of_arms.py
import random
from PIL import Image, ImageDraw
from heraldic_elements import heraldic_elements, check_rule_of_tincture, select_element

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
        'Purpure': (128, 0, 128), # Purple
    },
    'Furs': {
        'Ermine': (252, 252, 252), # White with black spots (representing the fur of the stoat)
        'Ermines': (252, 252, 252),# Variant of ermine with more black spots
        'Erminois': (252, 252, 186),# Variant of ermine with gold spots
        'Erminites': (252, 252, 186),# Variant of ermine with gold spots
        'Pean': (252, 252, 186),   # Variant of ermine with gold spots
        'Vair': (173, 216, 230),   # Blue-grey above and white below (representing the winter coat of the red squirrel)
        'Potent': (173, 216, 230)  # Variant of vair
    },
    'Stains': {
        'Murrey': (128, 0, 64),   # Dark red or mulberry
        'Sanguine': (128, 0, 0),  # Venous-blood red
        'Tenné': (165, 42, 42)   # Orange or dark yellow to brownish
    },
    'Rare Metals': {
        'Copper': (184, 115, 51), # Copper color
        'Buff (metal in the United States)': (240, 220, 130) # Buff color in the United States
    },
    'Rare Colours': {
        'Bleu celeste': (178, 255, 255),   # Sky blue
        'Brunâtre (brown)': (139, 69, 19), # Dark brown
        'Buff (color in Canada)': (240, 220, 130), # Buff color in Canada
        'Cendrée': (192, 192, 192),        # Ashen gray
        'Ochre': (204, 119, 34),           # Ochre color
        'Orange': (255, 165, 0),           # Bright orange
        'Rose': (255, 102, 204)            # Rose color
    },
    'Realistic': {
        'Proper': (0, 0, 0),              # Proper color (usually naturalistic representation)
        'Carnation': (255, 182, 193)      # Light pink
}

class CoatOfArms:
    # The CoatOfArms class as defined previously, with its methods.

    # You might also want to add methods for rendering the coat of arms
    # or any additional functionality specific to the coat of arms.
    def __init__(self, rules, user_preferences=None):
        self.rules = rules
        self.user_preferences = user_preferences or {}
        self.division = None
        self.tinctures = None
        self.ordinaries = []
        self.charges = []

    def select_division(self):
        # Randomly select a division based on the rules and user preferences
        self.division = random.choice(self.rules['divisions'])

    def select_tinctures(self):
        # Randomly select tinctures making sure not to violate the rule of tincture
        allowed_tinctures = self.rules['tinctures']
        self.tinctures = {
            'primary': random.choice(allowed_tinctures['colors']),
            'secondary': random.choice(allowed_tinctures['metals'])
        }
        # Ensuring rule of tincture is not violated
        primary = random.choice(list(HERALDIC_COLORS['Colours'].keys()))
        secondary = random.choice(list(HERALDIC_COLORS['Metals'].keys()))
        self.tinctures = {'primary': primary, 'secondary': secondary}

    def select_ordinaries(self):
        # Check if user has preferences for ordinaries
        if 'ordinaries' in self.user_preferences:
            # Go through each preference and try to select an ordinary accordingly
            for pref in self.user_preferences['ordinaries']:
                # Make sure the preference is actually available in the rules
                if pref in self.rules['ordinaries']:
                    self.ordinaries.append(pref)
                else:
                    print(f"No such ordinary preference: {pref}")
        else:
            # Default to choosing any ordinary if no preferences are specified
            self.ordinaries = [random.choice(self.rules['ordinaries'])]
    
    def draw_division_chevron(self, draw, width, height):
        # Draw a basic chevron shape
        chevron_shape = [
            (width / 2, height * 0.2),  # Top point
            (width * 0.1, height / 2),  # Bottom left
            (width * 0.9, height / 2)   # Bottom right
        ]
        draw.polygon(chevron_shape, fill=self.tinctures['secondary'])

    def apply_tinctures(self, img):
        # Translate heraldic tinctures to RGB and apply primary tincture
        primary_color_category = 'Colours' if self.tinctures['primary'] in HERALDIC_COLORS['Colours'] else 'Metals'
        secondary_color_category = 'Metals' if self.tinctures['secondary'] in HERALDIC_COLORS['Metals'] else 'Colours'
        primary_color = HERALDIC_COLORS[primary_color_category].get(self.tinctures['primary'], (255, 255, 255))  # Default to white if not found
        secondary_color = HERALDIC_COLORS[secondary_color_category].get(self.tinctures['secondary'], (255, 255, 255))  # Default to white if not found

        # Apply primary color
        draw = ImageDraw.Draw(img)
        draw.rectangle([(0, 0), (img.width, img.height)], fill=primary_color)


    def draw_ordinaries(self, draw, ordinary, width, height):
        # Draw the ordinary, e.g., a bend, a chevron, etc.
        if ordinary == 'Bend':
            # Draw a diagonal line from top left to bottom right
            draw.line((0, 0, width, height), fill='black', width=10)
         if ordinary == 'Chevron':
            self.draw_division_chevron(draw, width, height)
        # ... handle other ordinaries ...

    def draw_charge(self, draw, charge, width, height):
        # ... existing logic ...
        if charge == 'Dragon':
            # Draw a simple representation of a dragon, or add an image
            pass
        elif charge == 'Sword':
            # Draw a simple representation of a sword, or add an image
            pass
        # ... handle other charges ...

    def assemble_coat_of_arms(self):
        # Dimensions for the coat of arms
        width, height = 300, 360

        # Create a new image with a white background
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)

        # Apply primary and secondary tinctures
        self.apply_tinctures(img)

        # Draw the division onto the image if it's a chevron
        if self.division == 'Chevron':
            self.draw_division_chevron(draw, width, height)

        # Draw the ordinaries onto the image
        for ordinary in self.ordinaries:
            self.draw_ordinaries(draw, ordinary, width, height)

        # Draw the charges onto the image
        for charge in self.charges:
            self.draw_charge(draw, charge, width, height)

        # Save the image to a file
        img.save('coat_of_arms.png')

        # Optionally, display the image
        img.show()


    def select_charges(self):
        # Randomly select charges, considering user preferences and making sure they fit with the division and ordinaries
        if 'charges' in self.user_preferences:
            self.charges = [random.choice(self.rules['charges'][pref]) for pref in self.user_preferences['charges']]
        else:
            self.charges = [random.choice(self.rules['charges'])]


    def get_elements(self):
        # Return the selected elements
        return {
            'division': self.division,
            'tinctures': self.tinctures,
            'ordinaries': self.ordinaries,
            'charges': self.charges
        }

# This class would be used by main.py to generate the coat of arms
