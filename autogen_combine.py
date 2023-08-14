import os
from PIL import Image
import json

def combine_sprites(top_path, bottom_path, output_path, max_size=(96, 96)):
    # Open top and bottom sprite images
    top_sprite = Image.open(top_path)
    bottom_sprite = Image.open(bottom_path)
    
    # Calculate new dimensions
    width = max(top_sprite.width, bottom_sprite.width)
    total_height = top_sprite.height + bottom_sprite.height
    
    # Create new image canvas
    combined_sprite = Image.new("RGBA", (width, total_height))
    
    # Paste the sprites onto the canvas
    combined_sprite.paste(top_sprite, (0, 0))
    combined_sprite.paste(bottom_sprite, (0, top_sprite.height))
    
    # Resize if the combined sprite exceeds max dimensions
    if combined_sprite.width > max_size[0] or combined_sprite.height > max_size[1]:
        combined_sprite = combined_sprite.resize(max_size, Image.ANTIALIAS)
    
    # Save the result
    combined_sprite.save(output_path)

def main():
    top_directory = "Top"
    bottom_directory = "Bottom"
    fusion_directory = "Fusion"
    
    # Ensure fusion directory exists
    if not os.path.exists(fusion_directory):
        os.mkdir(fusion_directory)
    
    # List top and bottom sprites
    top_sprites = [f for f in os.listdir(top_directory) if f.endswith('.top.png')]
    bottom_sprites = [f for f in os.listdir(bottom_directory) if f.endswith('.bottom.png')]

    total_combinations = len(top_sprites) * len(bottom_sprites)
    print(f"Starting to combine {total_combinations} sprite combinations...")

    count = 0
    # Iterate over all combinations
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