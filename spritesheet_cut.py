from PIL import Image
import os
import json

def is_blank(img):
    if img.mode != 'RGBA':
        return False
    data = img.getdata()
    return all(pixel[3] == 0 for pixel in data)

def split_sprite_sheet(filename, rows, cols):
    with Image.open(filename) as img:
        sprite_width = img.width // cols
        sprite_height = img.height // rows
        
        if not os.path.exists("Pokemon"):
            os.makedirs("Pokemon")

        count = 1
        for j in range(rows):
            for i in range(cols):
                left = i * sprite_width
                upper = j * sprite_height
                right = left + sprite_width
                lower = upper + sprite_height
                
                sprite = img.crop((left, upper, right, lower))
                
                if not is_blank(sprite):
                    sprite.save(os.path.join("Pokemon", f"{count}.png"))
                    count += 1

def rename_and_move_files_using_json(pokemon_folder, json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    if not os.path.exists("IFPokemon"):
        os.makedirs("IFPokemon")

    for pokemon_name, dex_numbers in data.items():
        original_file = os.path.join(pokemon_folder, f"{dex_numbers['official_dex']}.png")
        new_file = os.path.join("IFPokemon", f"{dex_numbers['if_dex']}.png")

        if os.path.exists(original_file):
            os.rename(original_file, new_file)

if __name__ == "__main__":
    sprite_sheet_file = "sprites.png"
    rows = 21
    cols = 31
    split_sprite_sheet(sprite_sheet_file, rows, cols)
    rename_and_move_files_using_json("Pokemon", "pokedex_if_list.json")