#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This is a space shooter game for PyBadge

import ugame
import stage
import time
import random
import constants


def splash_scene():
    # Plays the splash screen sound
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # Load splash screen image bank and set background
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Draw "MT Game Studio" logo manually using tile indices
    background.tile(2, 2, 0)  # white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)

    background.tile(2, 3, 0)
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)

    background.tile(2, 4, 0)
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)

    background.tile(2, 5, 0)
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)

    # Set up and render splash scene
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # Wait two seconds then move to menu
    time.sleep(2.0)
    menu_scene()


def menu_scene():
    # Load background and setup text
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    text = []

    text1 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(12, 10)
    text1.text("Jay's Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        # If start is pressed, go to game scene
        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():
    # Helper function to spawn one alien on screen
    def show_alien():
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE),
                    constants.OFF_TOP_SCREEN)
                break

    # Load image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Initialize button states
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Set up sound system
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Create player sprite
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Create background
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Create laser pool (invisible at start)
    lasers = []
    for _ in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # Create alien pool (invisible at start)
    aliens = []
    for _ in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    show_alien()

    # Setup game display
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = aliens + lasers + [ship] + [background]
    game.render_sprites(lasers + [ship])
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        # Track "A" button state
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

        # Move ship right
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)

        # Move ship left
        if keys & ugame.K_LEFT:
            if ship.x > 0:
                ship.move(ship.x - 1, ship.y)

        # Fire laser if A just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            for laser in lasers:
                if laser.x < 0:
                    laser.move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # Move lasers upward and remove off-screen ones
        for laser in lasers:
            if laser.x > 0:
                laser.move(laser.x, laser.y - constants.LASER_SPEED)
                if laser.y < constants.OFF_TOP_SCREEN:
                    laser.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # Move aliens downward and reset off-screen ones
        for alien in aliens:
            if alien.x > 0:
                alien.move(alien.x, alien.y + constants.ALIEN_SPEED)
                if alien.y > constants.SCREEN_Y:
                    alien.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # Redraw updated positions
        game.render_sprites(aliens + lasers + [ship])
        game.tick()


# Start the game at the splash screen
if __name__ == "__main__":
    splash_scene()