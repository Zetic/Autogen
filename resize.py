from PIL import Image
import os

def upscale_sprites(input_folder, output_folder, scale_factor=3):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all sprites in the input folder
    sprites = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    total_sprites = len(sprites)
    print(f"Starting to upscale {total_sprites} sprites...")

    for idx, sprite in enumerate(sprites, 1):
        sprite_path = os.path.join(input_folder, sprite)
        img = Image.open(sprite_path)

        # Ensure all sprites are of size 96x96 before upscaling
        if img.size == (96, 96):
            img_resized = img.resize((img.width * scale_factor, img.height * scale_factor), Image.NEAREST)
            img_resized.save(os.path.join(output_folder, sprite))
            print(f"Processed {idx}/{total_sprites}: {sprite}")
        else:
            print(f"Skipped {sprite} as its size is not 96x96")

    print("All sprites processed successfully!")

if __name__ == "__main__":
    upscale_sprites("Fusion", "FusionScaled")