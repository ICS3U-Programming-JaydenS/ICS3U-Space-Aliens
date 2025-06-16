#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This is the RST project


import ugame
import stage
import constants

def game_scene():

    # Pulls BMP files to variables in game
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16 ("space_aliens.bmp")

    # Initialize button states to "up" (not pressed) for A, B, Start, and Select button
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Gets wav sound for pew sound and prepare audio system
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio

    # stop any other sound
    sound.stop()

    # Stops the sound from playing
    sound.mute(False)

    # Selects the ship sprite and places it in X 75 and Y 66
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Creates a background grid using the image bank, sized 10 tiles wide by 8 tiles tall
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 
    # Gets the alien Sprite
    alien = stage.Sprite (image_bank_sprites, 9, int(constants.SCREEN_X/2 - constants.SCREEN_Y/2), 16)

    # Refreshes the game every 60 pixels a second
    game = stage.Stage(ugame.display, constants.FPS)

    # Layers the game to draw the ship then the background
    game.layers = [ship] + [alien] + [background]

    # Renders the sprite and background
    game.render_sprites([ship] + [alien])
    game.render_block()
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # Checks what button you pressed and makes you move in a certain way.
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
                        
            
            pass
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            # Makes you go right in game
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        
        if keys & ugame.K_LEFT:
            # Makes you go left
            if ship.x <= 0:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        
        if a_button == constants.button_state ["button_just_pressed"]:
            
            # If buttons pressed play pew sound
            sound.play (pew_sound)
        # update game logic
        # redraw Sprites
        game.render_sprites([ship, alien])
        game.tick()
if __name__ == "__main__":
    game_scene()