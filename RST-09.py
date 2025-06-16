# Created By: Jayden Smith
# Date: May 12, 2025
# This is the RST project


import ugame
import stage
import random
import time

import constants
def splash_scene():
    # Plays coin sound
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # Gets image library 
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # Sets the background to all the area of the pybadge
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # Sets the background color to white
    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white


    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white


    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white


    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()
   
    while True:
        # Waits two seconds  before entering the menu
        time.sleep (2.0)
        menu_scene()
        # redraw Sprites
       
        game.tick()
def menu_scene():
    # Pulls MT studio BMP
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Sets text list
    text = []

    # Defines where the location of the text should go
    text1 = stage.Text (width = 29, height = 12, font =None, palette = constants.NEW_PALETTE, buffer=None)
    text1.move(12,10)

    # What the text is
    text1.text("Jay's Game Studios")
    text.append(text1)

    # Defines the location of the text
    text2 = stage.Text(width = 29, height = 12, font =None, palette = constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    # What the text says
    text2.text("PRESS START")
    text.append(text2)
    
    
    # Sets the background
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 
    
    # Refreshes at 60 frames per second
    game = stage.Stage(ugame.display, constants.FPS)
    # Renders the sprite and background
    game.layers = text + [background]
    game.render_block()
    
    while True:
        keys = ugame.buttons.get_pressed()
        # When you press start the game starts
        if keys & ugame.K_START != 0:
            game_scene()
      
        # redraw Sprites
        
        game.tick()
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
    # Creates a random background
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
        
            tile_picked = random.randint(1, 3)
       
            background.tile(x_location, y_location, tile_picked)

    # Gets the alien Sprite
    alien = stage.Sprite (image_bank_sprites, 9, int(constants.SCREEN_X/2 - constants.SCREEN_Y/2), 16)

    # Creates lasers list
    lasers = []
    # Makes sure you cannot make more then 5 laser on a screen at once
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):

        # Selects lasers sprite and places it in the list
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = lasers + [ship] + [alien] + [background]
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
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
       
        if keys & ugame.K_LEFT:
            if ship.x <= 0:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
       
        if a_button == constants.button_state ["button_just_pressed"]:
            # Fires laser
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
                    
        # Move each laser upward and check if it goes off the top of the screen
        for laser_number in range(len(lasers)):
            # Ensures that the only lasers that are updated are the ones on screen
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)

                # If it goes off screen it gets hidden
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        # update game logic
        # redraw Sprites
        game.render_sprites(lasers + [ship] + [alien])
        game.tick()
       
if __name__ == "__main__":
    splash_scene()