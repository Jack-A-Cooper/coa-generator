# Import necessary libraries
from PIL import Image, ImageDraw
import random

# Define the colors (You would have more colors and these values would correspond to heraldic tinctures)
HERALDIC_COLORS = {
    'gules': (255, 0, 0),      # Red
    'azure': (0, 0, 255),       # Blue
    'sable': (0, 0, 0),         # Black
    'vert': (0, 255, 0),        # Green
    'purpure': (160, 32, 240),  # Purple
    'or': (255, 223, 0),        # Gold
    'argent': (255, 255, 255),  # Silver
}

# Define a class for Ordinaries
class Ordinary:
    def __init__(self, shape, color_name, shield_size):
        self.shape = shape
        self.color = HERALDIC_COLORS[color_name]
        self.image = Image.new('RGBA', shield_size)
        self.draw = ImageDraw.Draw(self.image)
        self.create_ordinary()

    def create_ordinary(self):
        # For simplicity, this will only create a horizontal band called a fess
        if self.shape == 'fess':
            width, height = self.image.size
            band_height = height // 5
            self.draw.rectangle([(0, (height - band_height) // 2), (width, (height + band_height) // 2)], fill=self.color)

# Define a base Shield class
class Shield:
    def __init__(self):
        self.base_image = Image.new('RGB', (300, 400), color=HERALDIC_COLORS['argent'])  # Default to silver/white
        self.draw = ImageDraw.Draw(self.base_image)
        self.colors_assigned = []  # This will keep track of assigned colors to follow the rule of tinctures

    def add_tincture(self, color_name):
        # Ensures that tinctures adhere to heraldic rules before adding
        if self.check_rule_of_tincture(color_name):
            self.colors_assigned.append(color_name)
        else:
            raise ValueError(f"Adding {color_name} would break the rule of tinctures.")

    def check_rule_of_tincture(self, new_color):
        # Check for compliance with the rule of tincture
        new_is_metal = new_color in ['or', 'argent']
        for assigned_color in self.colors_assigned:
            assigned_is_metal = assigned_color in ['or', 'argent']
            if new_is_metal == assigned_is_metal:
                return False
        return True


    def divide_shield(self):
        width, height = self.base_image.size
        quarter_width, quarter_height = width // 2, height // 2

        # Define separate pools for metals and colors
        metals = ['or', 'argent']
        colors = [tincture for tincture in HERALDIC_COLORS.keys() if tincture not in metals]

        # We'll reserve one metal and one color for the charge
        reserved_metal = random.choice(metals)
        reserved_color = random.choice(colors)
        metals.remove(reserved_metal)
        colors.remove(reserved_color)

        # Start by assigning a tincture to the first quadrant, not from the reserved ones
        first_tincture = random.choice(metals + colors)
        self.add_tincture(first_tincture)
        self.draw.rectangle([0, 0, quarter_width, quarter_height], fill=HERALDIC_COLORS[first_tincture])

        # Proceed with the remaining quadrants
        for i in range(1, 4):
            # Choose a tincture that does not violate the rule
            # And is not the same as the one in the quadrant to its immediate left (or above for the bottom row)
            allowed_tinctures = metals + colors
            if i % 2 == 1:  # For quadrants 1 and 3 (top right and bottom right)
                allowed_tinctures.remove(self.colors_assigned[i-1])  # Remove the color of the left quadrant
            if i == 2:  # For quadrant 2 (bottom left)
                allowed_tinctures.remove(self.colors_assigned[i-2])  # Remove the color of the top left quadrant

            # Choose a tincture from the remaining pool and apply it to the current quadrant
            next_tincture = random.choice(allowed_tinctures)
            self.add_tincture(next_tincture)
            x = (i % 2) * quarter_width
            y = (i // 2) * quarter_height
            self.draw.rectangle([x, y, x + quarter_width, y + quarter_height], fill=HERALDIC_COLORS[next_tincture])

        # Now we return the reserved tinctures so they can be used for the charge
        return reserved_metal, reserved_color    
       
    def add_ordinary(self, ordinary):
        # Overlay an ordinary onto the shield
        self.base_image.paste(ordinary.image, (0, 0), ordinary.image)

# Define a base Charge class
class Charge:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        # Load the charge image (this would be more complex in a full implementation)
        self.image = Image.new('RGB', self.size, color='black') # Placeholder image

    # Additional methods for charge placement will go here

# Define a class for coloring and shading
class HeraldicColor:
    @staticmethod
    def apply_color(shield, charge, reserved_metal, reserved_color):
        # Decide the color of the charge based on the shield's colors
        # Here you may want to implement more complex logic depending on your needs
        if shield.check_rule_of_tincture(reserved_color):
            charge_color = HERALDIC_COLORS[reserved_color]
        else:
            charge_color = HERALDIC_COLORS[reserved_metal]
        
        # Apply the color to the charge
        charge_draw = ImageDraw.Draw(charge.image)
        charge_draw.rectangle([0, 0, charge.size[0], charge.size[1]], fill=charge_color)
        
        # Now overlay the charge onto the shield
        position = ((shield.base_image.width - charge.size[0]) // 2, (shield.base_image.height - charge.size[1]) // 2)
        shield.base_image.paste(charge.image, position)

# Make sure that this adjusted `apply_color` method is used correctly when you create the charges

def generate_coat_of_arms():
    try:
        shield = Shield()
        
        # Divide the shield and apply tinctures
        reserved_metal, reserved_color = shield.divide_shield()
        
        # Create a charge
        charge = Charge(name='lion', size=(50, 50))  # Placeholder values
        
        # Apply color to charge
        HeraldicColor.apply_color(shield, charge, reserved_metal, reserved_color)
        
        # Add an ordinary, ensuring it doesn't break the rule of tincture
        possible_ordinary_colors = [color for color in HERALDIC_COLORS if color not in shield.colors_assigned]
        ordinary_color = random.choice(possible_ordinary_colors)
        ordinary = Ordinary(shape='fess', color_name=ordinary_color, shield_size=(300, 400))
        shield.add_ordinary(ordinary)
        
        # Save or display the shield
        shield.base_image.show()
        shield.base_image.save("coat_of_arms.png")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the generator
generate_coat_of_arms()