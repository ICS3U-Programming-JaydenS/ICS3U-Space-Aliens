# Created By: Jayden Smith
# Date: May 12, 2025
# This is the RST project

import ugame
import stage
import random
import time
import constants

# Splash screen scene – shows intro visuals and plays a sound before menu
def splash_scene():
    # Plays coin sound at start
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # Load background image for splash screen
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Set background grid size
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Draws text tiles (logo or title made with tiles)
    background.tile(2, 2, 0)
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

    # Setup stage with background
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # Waits for 2 seconds before moving to the menu
    while True:
        time.sleep(2.0)
        menu_scene()
        game.tick()

# Menu screen that prompts the player to press START
def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    text = []

    # Title text
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(12, 10)
    text1.text("Jay's Game Studios")
    text.append(text1)

    # Start prompt text
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    # Waits for player to press START
    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            game_scene()
        game.tick()

# Main gameplay scene
def game_scene():
    # Shows a single alien on the screen
    def show_alien():
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    score = 0

    # Display text for score
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # Load images
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Initialize buttons
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Load sounds
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')

    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Create player ship sprite
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Create background grid
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Create alien and laser sprites
    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X/2 - constants.SCREEN_Y/2), 16)

    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    show_alien()

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [score_text] + lasers + [ship] + aliens + [background]
    game.render_block()

    # Game loop
    while True:
        keys = ugame.buttons.get_pressed()

        # Button press logic
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

        # Debug prints (optional)
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")

        # Movement logic
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

        # Fire laser
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # Move laser upward
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # Collision detection: Laser hits alien
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].y > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y,
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

        # Move alien downward
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # Redraw sprites on screen
        game.render_sprites(aliens + lasers + [ship])
        game.tick()

# Start the game at the splash screen
if __name__ == "__main__":
    splash_scene()