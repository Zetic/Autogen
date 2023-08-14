from PIL import Image, UnidentifiedImageError
import os
import json

def is_blank(img):
    if img.mode != 'RGBA':
        return False
    data = img.getdata()
    return all(pixel[3] == 0 for pixel in data)

def upscale_image(image_path, output_path, scale_factor=3):
    with Image.open(image_path) as img:
        img_resized = img.resize((img.width * scale_factor, img.height * scale_factor), Image.NEAREST)
        img_resized.save(output_path)

def split_sprite_sheet(filename, rows, cols):
    with Image.open(filename) as img:
        sprite_width = img.width // cols
        sprite_height = img.height // rows
        
        if not os.path.exists("IFPokemon"):
            os.makedirs("IFPokemon")

        count = 1
        for j in range(rows):
            for i in range(cols):
                left = i * sprite_width
                upper = j * sprite_height
                right = left + sprite_width
                lower = upper + sprite_height
                
                sprite = img.crop((left, upper, right, lower))
                
                if not is_blank(sprite):
                    sprite.save(os.path.join("IFPokemon", f"{count}.png"))
                    count += 1

def split_sprite(sprite_path, output_top_path, output_bottom_path):
    img = Image.open(sprite_path)
    split_point = img.height // 2
    top_half = img.crop((0, 0, img.width, split_point))
    bottom_half = img.crop((0, split_point, img.width, img.height))
    top_half.save(output_top_path)
    bottom_half.save(output_bottom_path)

def combine_sprites(top_path, bottom_path, output_path, max_size=(288, 288)):
    top_sprite = Image.open(top_path)
    bottom_sprite = Image.open(bottom_path)
    combined_sprite = Image.new("RGBA", (top_sprite.width, top_sprite.height + bottom_sprite.height))
    combined_sprite.paste(top_sprite, (0, 0))
    combined_sprite.paste(bottom_sprite, (0, top_sprite.height))
    combined_sprite.save(output_path)

def main():
    # Upscale the sprites.png
    upscale_image("sprites.png", "sprites_upscaled.png")
    
    # Split sprites_upscaled.png
    split_sprite_sheet("sprites_upscaled.png", 20, 21)

    # Split each sprite in IFPokemon into top and bottom
    top_directory = "Top"
    bottom_directory = "Bottom"
    if not os.path.exists(top_directory):
        os.mkdir(top_directory)
    if not os.path.exists(bottom_directory):
        os.mkdir(bottom_directory)

    for file in os.listdir("IFPokemon"):
        if file.endswith(".png"):
            sprite_path = os.path.join("IFPokemon", file)
            base_name = os.path.splitext(file)[0]
            output_top_path = os.path.join(top_directory, f"{base_name}.top.png")
            output_bottom_path = os.path.join(bottom_directory, f"{base_name}.bottom.png")
            split_sprite(sprite_path, output_top_path, output_bottom_path)

    # Combine sprites from "Top" and "Bottom" into Fusion
    fusion_directory = "Fusion"
    if not os.path.exists(fusion_directory):
        os.mkdir(fusion_directory)
    
    top_sprites = [f for f in os.listdir(top_directory) if f.endswith('.top.png')]
    bottom_sprites = [f for f in os.listdir(bottom_directory) if f.endswith('.bottom.png')]
    total_combinations = len(top_sprites) * len(bottom_sprites)
    print(f"Starting to combine {total_combinations} sprite combinations...")
    count = 0

    for top_sprite in top_sprites:
        for bottom_sprite in bottom_sprites:
            top_number = os.path.splitext(top_sprite)[0].split(".")[0]
            bottom_number = os.path.splitext(bottom_sprite)[0].split(".")[0]
            output_name = f"{top_number}.{bottom_number}.png"
            output_path = os.path.join(fusion_directory, output_name)
            top_path = os.path.join(top_directory, top_sprite)
            bottom_path = os.path.join(bottom_directory, bottom_sprite)
            combine_sprites(top_path, bottom_path, output_path)
            count += 1
            print(f"Processed {count}/{total_combinations}: {output_name}")

    print("All sprite combinations processed successfully!")

if __name__ == "__main__":
    main()