#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This code Displays The background on the pybadge

import ugame
import stage


def game_scene():
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp("stage_aliens.bmp")
    ship = stage.Sprite(image_bank_sprite, 5, 75, 66)
    background = stage.Grid(space_aliens_background, 10, 8)
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()
    while True:
        # get user input
        # update game logic
        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
