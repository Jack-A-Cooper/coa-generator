from PIL import Image, ImageDraw, ImageFont
import os
import random

# Define the base path for the image library
script_dir = os.path.dirname(os.path.abspath(__file__))
base_image_lib_path = os.path.join(script_dir, 'imageLib')

# Paths to the different elements directories
shield_paths = os.path.join(base_image_lib_path, 'shields')
crest_paths = os.path.join(base_image_lib_path, 'crests')
helm_paths = os.path.join(base_image_lib_path, 'helms')
supporter_paths = os.path.join(base_image_lib_path, 'supporters')
symbol_paths = os.path.join(base_image_lib_path, 'symbols')
charge_paths = os.path.join(base_image_lib_path, 'charges')
exterior_paths = os.path.join(base_image_lib_path, 'exteriors')

def random_image_from_directory(directory):
    try:
        files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        if not files:
            print(f"The directory {directory} is empty or does not contain any image files.")
            return None
        return os.path.join(directory, random.choice(files))
    except FileNotFoundError:
        print(f"Error: The directory {directory} was not found.")
        return None

def create_coat_of_arms():
    # Create a blank canvas
    coat_of_arms = Image.new('RGBA', (500, 600), (255, 255, 255, 0))

    # Define function to paste elements onto the coat of arms
    def paste_element(element_path, position):
        if element_path:
            element = Image.open(element_path)
            coat_of_arms.paste(element, position, element.convert('RGBA'))
        else:
            element_name = os.path.basename(os.path.dirname(element_path))
            print(f"No {element_name} image was found. The coat of arms will not include a {element_name}.")

    # Select and paste random elements onto the coat of arms
    paste_element(random_image_from_directory(shield_paths), (100, 200))
    paste_element(random_image_from_directory(crest_paths), (150, 50))
    paste_element(random_image_from_directory(helm_paths), (150, 150))
    # ... repeat for other directories

    # For symbols and charges, you might want to paste multiple images
    for _ in range(random.randint(1, 3)):  # Random number of symbols/charges
        paste_element(random_image_from_directory(symbol_paths), (random.randint(50, 450), random.randint(250, 550)))
        paste_element(random_image_from_directory(charge_paths), (random.randint(50, 450), random.randint(250, 550)))

    # Optionally add an exterior element
    paste_element(random_image_from_directory(exterior_paths), (0, 0))

    # Save or display the result
    coat_of_arms.show()
    coat_of_arms.save(os.path.join(script_dir, 'random_coat_of_arms.png'))

create_coat_of_arms()
