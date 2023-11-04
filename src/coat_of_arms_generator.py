# coat_of_arms_generator.py
from heraldic_elements import heraldic_elements, check_rule_of_tincture, select_element
import random

class CoatOfArms:
    def __init__(self, user_preferences=None):
        self.user_preferences = user_preferences or {}
        self.division = None
        self.tinctures = None
        self.ordinaries = []
        self.charges = []

    def select_division(self):
        # Randomly select a division based on user preferences if available
        self.division = select_element(self.user_preferences.get('divisions', heraldic_elements['divisions']))

    def select_tinctures(self):
        # Randomly select tinctures making sure not to violate the rule of tincture
        primary_tincture = select_element(heraldic_elements['tinctures']['colors'] + heraldic_elements['tinctures']['metals'])
        # The loop ensures the selected secondary tincture complies with the rule of tincture
        secondary_tincture = select_element(heraldic_elements['tinctures']['colors'] + heraldic_elements['tinctures']['metals'])
        while not check_rule_of_tincture(primary_tincture, secondary_tincture):
            secondary_tincture = select_element(heraldic_elements['tinctures']['colors'] + heraldic_elements['tinctures']['metals'])

        self.tinctures = {
            'primary': primary_tincture,
            'secondary': secondary_tincture
        }

    def select_ordinaries(self):
        # Randomly select ordinaries, considering user preferences if any
        self.ordinaries = [select_element(self.user_preferences.get('ordinaries', heraldic_elements['ordinaries']))]

    def select_charges(self):
        # Randomly select charges, considering user preferences and making sure they fit with the division and ordinaries
        available_charges = heraldic_elements['charges']['animals'] + heraldic_elements['charges']['objects']
        if 'charges' in self.user_preferences:
            prefs = self.user_preferences['charges']
            # Ensure we match preferences against charge names
            avoid_list = [charge for charge in available_charges if charge.name in prefs]
            self.charges = [select_element(available_charges, avoid_list)]
        else:
            self.charges = [select_element(available_charges)]

    def assemble_coat_of_arms(self):
        # Assemble the coat of arms using the selected elements
        # This is where the logic for positioning and sizing elements would go
        pass

    def get_elements(self):
        # Return the selected elements
        return {
            'division': self.division,
            'tinctures': self.tinctures,
            'ordinaries': self.ordinaries,
            'charges': self.charges
        }

# Example usage
if __name__ == "__main__":
    user_preferences = {
        'divisions': ["Pale"],
        'charges': ["Lion", "Sword"]
    }
    coat_of_arms = CoatOfArms(user_preferences)
    coat_of_arms.select_division()
    coat_of_arms.select_tinctures()
    coat_of_arms.select_ordinaries()
    coat_of_arms.select_charges()
    print(coat_of_arms.get_elements())
