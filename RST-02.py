#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This code Displays The background on the pybadge


import ugame
import stage


def game_scene():
    # Loads the background image bank from the BMP file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Creates a background grid using the image bank, sized 10 tiles wide by 8 tiles tall
    background = stage.Grid(space_aliens_background, 10, 8)
    # Refreshes the game 60 frames a second
    game = stage.Stage(ugame.display, 60)
    # layers the game 
    game.layers = [background]
    # Render the blocks
    game.render_block()
    while True:
        pass


if __name__ == "__main__":
    game_scene()
