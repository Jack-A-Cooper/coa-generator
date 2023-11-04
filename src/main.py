# main.py
from coat_of_arms import CoatOfArms
from heraldic_elements import heraldic_elements

def main():
    # Here, we can define some user preferences. These could also be collected via input from the user.
    user_preferences = {
        'ordinaries': ['Bend', 'Chevron'],
        'charges': ['animals', 'objects']  # Assuming user wants to include both categories
    }

    # Create a CoatOfArms instance with the specified rules and user preferences.
    coat_of_arms_generator = CoatOfArms(heraldic_elements, user_preferences)

    # Generate the coat of arms by selecting each element.
    coat_of_arms_generator.select_division()
    coat_of_arms_generator.select_tinctures()
    coat_of_arms_generator.select_ordinaries()
    coat_of_arms_generator.select_charges()
    
    # Retrieve and print the generated coat of arms elements.
    coat_of_arms = coat_of_arms_generator.get_elements()
    print(f"Generated Coat of Arms: {coat_of_arms}")

    # If you have a rendering function, you could also display the coat of arms visually.
    # coat_of_arms_generator.render_coat_of_arms()
    coat_of_arms_generator.assemble_coat_of_arms()

if __name__ == "__main__":
    main()
