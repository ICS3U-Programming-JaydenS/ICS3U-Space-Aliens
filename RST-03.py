#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This code Displays The background on the pybadge

import ugame
import stage


def game_scene():
    # Loads the background image bank from the BMP file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Loads the background sprite bank from the BMP file
    image_bank_sprite = stage.Bank.from_bmp("stage_aliens.bmp")
    # Selects the ship sprite and places it in X 75 and Y 66
    ship = stage.Sprite(image_bank_sprite, 5, 75, 66)

    # Creates a background grid using the image bank, sized 10 tiles wide by 8 tiles tall
    background = stage.Grid(image_bank_background, 10, 8)

    # Refreshes the game every 60 pixels a second
    game = stage.Stage(ugame.display, 60)
    # Layers the game to draw the ship then the background
    game.layers = [ship] + [background]
    # Renders the layers
    game.render_block()
    while True:
        # get user input
        # update game logic
        # redraw Sprites

        # Renders the sprite
        game.render_sprites([ship])

        # Refreshes whats on screen
        game.tick()
if __name__ == "__main__":
    game_scene()