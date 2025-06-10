#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This is the RST project


import ugame
import stage
import constants

def game_scene():
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16 ("space_aliens.bmp")
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    background = stage.Grid(image_bank_background, 10, 8)  
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # Checks what button you pressed and makes you move in a certain way.
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            # Causes a border on right side of pybadge
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        
        if keys & ugame.K_LEFT:
            # Causes a border on left side of pybadge
            if ship.x <= 0:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        
        # update game logic
        # redraw Sprites
        game.render_sprites([ship])
        game.tick()
if __name__ == "__main__":
    game_scene()