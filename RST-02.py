#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This code Displays The background on the pybadge



import ugame
import stage

def game_scene():
    space_aliens_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(space_aliens_background, 10, 8)
    game = stage.Stage (ugame.display, 60)
    game.layers = [background]
    game.render_block()
    while True:
        pass
if __name__ == "__main__":
    game_scene()
