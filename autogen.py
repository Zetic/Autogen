from PIL import Image
import os

def split_sprite(sprite_path, output_top_path, output_bottom_path):
    img = Image.open(sprite_path)
    width, height = img.size
    split_point = height // 2
    top_half = img.crop((0, 0, width, split_point))
    bottom_half = img.crop((0, split_point, width, height))
    top_half.save(output_top_path)
    bottom_half.save(output_bottom_path)

def combine_sprites(top_path, bottom_path, output_path, max_size=(96, 96)):
    top_sprite = Image.open(top_path)
    bottom_sprite = Image.open(bottom_path)
    width = max(top_sprite.width, bottom_sprite.width)
    total_height = top_sprite.height + bottom_sprite.height
    combined_sprite = Image.new("RGBA", (width, total_height))
    combined_sprite.paste(top_sprite, (0, 0))
    combined_sprite.paste(bottom_sprite, (0, top_sprite.height))
    if combined_sprite.width > max_size[0] or combined_sprite.height > max_size[1]:
        combined_sprite = combined_sprite.resize(max_size, Image.ANTIALIAS)
    combined_sprite.save(output_path)

def main():
    # Split each sprite in IFPokemon
    source_directory = "IFPokemon"
    top_directory = "Top"
    bottom_directory = "Bottom"
    if not os.path.exists(top_directory):
        os.mkdir(top_directory)
    if not os.path.exists(bottom_directory):
        os.mkdir(bottom_directory)

    for file in os.listdir(source_directory):
        if file.endswith(".png"):
            sprite_path = os.path.join(source_directory, file)
            base_name = os.path.splitext(file)[0]
            output_top_path = os.path.join(top_directory, f"{base_name}.top.png")
            output_bottom_path = os.path.join(bottom_directory, f"{base_name}.bottom.png")
            split_sprite(sprite_path, output_top_path, output_bottom_path)

    # Combine sprites from "Top" and "Bottom"
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