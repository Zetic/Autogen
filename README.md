Pokémon Sprite Fusion Tool
This repository contains Python scripts designed to manage and create fused Pokémon sprites.


----------------------------------------------------------------------------------------------------------------------------------------------
Main Scripts
----------------------------------------------------------------------------------------------------------------------------------------------

Sprite Sheet Splitting Script: spritesheet_cut.py

Purpose: Extracts individual Pokémon sprites from a sprite sheet.

Splits a sprite sheet into individual Pokémon sprites.
Uses pokedex_if_list.json and sprites.json to rename and organize the sprites based on the official and Infinite Fusion Pokédex numbers.
Outputs the sprites to a directory named IFPokemon.
Pokémon Sprite Fusion Script:

----------------------------------------------------------------------------------------------------------------------------------------------

Splitter & Combiner Script: autogen.py

Purpose: Looks for a folder called IFPokemon (Can be created from the spritesheet_cut.py script and hand created with appropriate sprites).

Takes sprites directly from IFPokemon directory.
Splits the sprite in half based on the height and places them in Top and Bottom directories.
Takes sprites directly from Top and Bottom directories.
Combines the sprites, ensuring the resultant sprite fits within a 96x96 dimension.
Outputs the fused sprites to a directory named Fusion.
Provides console logging to track the progress of the script as it processes the combinations.

----------------------------------------------------------------------------------------------------------------------------------------------
Extras
----------------------------------------------------------------------------------------------------------------------------------------------

Top/Bottom Combiner Script: autogen_combine.py

Purpose: Looks for two folders Top/Bottom and then combines the sprites based on these folders. (Useful if we hand divide the two sections)

Takes sprites directly from Top and Bottom directories.
Combines the sprites, ensuring the resultant sprite fits within a 96x96 dimension.
Outputs the fused sprites to a directory named Fusion.
Provides console logging to track the progress of the script as it processes the combinations.

----------------------------------------------------------------------------------------------------------------------------------------------

Upscale Script: Resize.py

Purpose: Upscales sprites from 96x96 to 288x288

Iterates through every sprite in Fusions and upscales them.

----------------------------------------------------------------------------------------------------------------------------------------------
