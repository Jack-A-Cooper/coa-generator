# code_of_arms.py

from PIL import Image, ImageDraw
import cairosvg
from heraldic_elements import heraldic_elements, get_rgb_color, check_rule_of_tincture
import random
import io
import xml.etree.ElementTree as ET

class HeraldryRules:
    @staticmethod
    def enforce_tincture_rule(primary, secondary):
        return check_rule_of_tincture(primary, secondary)

    @staticmethod
    def get_contrasting_tincture(background_tincture):
        colors = heraldic_elements['tinctures']['colors']
        metals = heraldic_elements['tinctures']['metals']
        
        if background_tincture in colors:
            return random.choice(metals)
        else:
            return random.choice(colors)

class CoatOfArms:
    def __init__(self, rules, user_preferences=None):
        self.rules = rules
        self.user_preferences = user_preferences or {}
        self.division = None
        self.tinctures = {}
        self.ordinaries = []
        self.charges = []

    def select_division(self):
        self.division = random.choice(self.rules['divisions'] + [None])

    def select_tinctures(self):
        primary = random.choice(self.rules['tinctures']['colors'] + self.rules['tinctures']['metals'] + self.rules['tinctures']['furs'])
        secondary = random.choice(self.rules['tinctures']['colors'] + self.rules['tinctures']['metals'] + self.rules['tinctures']['furs'])

        while not HeraldryRules.enforce_tincture_rule(primary, secondary):
            secondary = random.choice(self.rules['tinctures']['colors'] + self.rules['tinctures']['metals'] + self.rules['tinctures']['furs'])
        
        self.tinctures = {'primary': primary, 'secondary': secondary}

    def select_ordinaries(self):
        """
        Selects a list of ordinaries corresponding to each division segment.
        """
        num_segments = len(self.get_division_coords(300, 360))
        self.ordinaries = [random.choice(self.rules['ordinaries'] + [None]) for _ in range(num_segments)]

    def select_charges(self):
        self.charges = [random.choice(heraldic_elements['charges']['loaded'] + [None]) for _ in range(4)]

    def render_svg_charge(self, charge):
        svg_data = open(charge.image_path).read()
        png_data = cairosvg.svg2png(bytestring=svg_data.encode('utf-8'))
        return Image.open(io.BytesIO(png_data)).convert("RGBA")

    def get_division_coords(self, width, height):
        """
        Calculates coordinates for each division type.
        """
        if self.division == 'Pale':
            return [(0, 0, width // 2, height), (width // 2, 0, width, height)]
        elif self.division == 'Fess':
            return [(0, 0, width, height // 2), (0, height // 2, width, height)]
        elif self.division == 'Quarterly':
            return [
                (0, 0, width // 2, height // 2),
                (width // 2, 0, width, height // 2),
                (0, height // 2, width // 2, height),
                (width // 2, height // 2, width, height)
            ]
        elif self.division == 'Cross':
            return [
                (0, 0, width // 2, height // 2),
                (width // 2, 0, width, height // 2),
                (0, height // 2, width // 2, height),
                (width // 2, height // 2, width, height)
            ]
        elif self.division == 'Saltire':
            return [
                (0, 0, width // 2, height // 2),
                (width // 2, 0, width, height // 2),
                (0, height // 2, width // 2, height),
                (width // 2, height // 2, width, height)
            ]
        elif self.division == 'Per Bend':
            return [(0, 0, width, height), (0, height, width, 0)]
        elif self.division == 'Per Bend Sinister':
            return [(0, 0, width, height), (width, 0, 0, height)]
        elif self.division == 'Gyronny':
            return [
                (0, 0, width // 2, height // 2),
                (width // 2, 0, width, height // 2),
                (0, height // 2, width // 2, height),
                (width // 2, height // 2, width, height)
            ]
        else:
            return [(0, 0, width, height)]

    def draw_division(self, img):
        secondary_rgb = get_rgb_color(self.tinctures['secondary'])
        draw = ImageDraw.Draw(img)
        width, height = img.size
        coords = self.get_division_coords(width, height)

        if self.division in ['Pale', 'Fess']:
            for _, coord in enumerate(coords[1:]):  # Only apply secondary color to the specified parts
                draw.rectangle(coord, fill=secondary_rgb)
        elif self.division == 'Quarterly' or self.division == 'Cross' or self.division == 'Gyronny':
            for i, coord in enumerate(coords):
                if i % 2 == 1:
                    draw.rectangle(coord, fill=secondary_rgb)
        elif self.division == 'Per Bend' or self.division == 'Per Bend Sinister':
            draw.polygon([coords[0][:2], coords[0][2:], coords[1][:2]], fill=secondary_rgb)

    def apply_tinctures(self, img):
        primary_rgb = get_rgb_color(self.tinctures['primary'])
        draw = ImageDraw.Draw(img)
        draw.rectangle([(0, 0), (img.width, img.height)], fill=primary_rgb)

    def draw_ordinaries(self, img, coords):
        draw = ImageDraw.Draw(img)
        secondary_rgb = get_rgb_color(self.tinctures['secondary'])
        
        for i, ordinary in enumerate(self.ordinaries):
            if ordinary == "Bend":
                draw.line([(coords[i][0], coords[i][3]), (coords[i][2], coords[i][1])], fill=secondary_rgb, width=20)
            elif ordinary == "Cross":
                mid_x = (coords[i][0] + coords[i][2]) // 2
                mid_y = (coords[i][1] + coords[i][3]) // 2
                draw.line([(mid_x, coords[i][1]), (mid_x, coords[i][3])], fill=secondary_rgb, width=20)
                draw.line([(coords[i][0], mid_y), (coords[i][2], mid_y)], fill=secondary_rgb, width=20)
            # Add other ordinary types here as needed

    def draw_charge(self, img, coords):
        for i, charge in enumerate(self.charges):
            if charge and i < len(coords):
                charge_img = self.render_svg_charge(charge)
                max_width, max_height = coords[i][2] - coords[i][0], coords[i][3] - coords[i][1]
                aspect_ratio = charge_img.width / charge_img.height

                if max_width > 0 and max_height > 0:
                    if charge_img.width > max_width:
                        new_width = max(1, int(max_width))
                        new_height = max(1, int(new_width / aspect_ratio))
                        charge_img = charge_img.resize((new_width, new_height), Image.LANCZOS)
                    if charge_img.height > max_height:
                        new_height = max(1, int(max_height))
                        new_width = max(1, int(new_height * aspect_ratio))
                        charge_img = charge_img.resize((new_width, new_height), Image.LANCZOS)

                    center_x = (coords[i][0] + coords[i][2]) // 2 - charge_img.width // 2
                    center_y = (coords[i][1] + coords[i][3]) // 2 - charge_img.height // 2
                    img.paste(charge_img, (center_x, center_y), charge_img)

    def assemble_coat_of_arms(self):
        img = Image.new('RGB', (300, 360), color='white')
        
        self.apply_tinctures(img)
        if self.division:
            self.draw_division(img)
        
        coords = self.get_division_coords(300, 360)
        self.draw_ordinaries(img, coords)
        self.draw_charge(img, coords)

        img.show()

    def get_elements(self):
        return {
            'division': self.division,
            'tinctures': self.tinctures,
            'ordinaries': self.ordinaries,
            'charges': self.charges
        }
