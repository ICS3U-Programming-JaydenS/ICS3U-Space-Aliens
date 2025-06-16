# Created By: Jayden Smith
# Date: May 12, 2025
# This is the RST project

# Import required libraries
import ugame
import stage
import random
import time
import supervisor
import constants

# Splash Scene: Initial screen with logo and sound
def splash_scene():
    # Plays coin sound at game start
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # Loads the background image for splash
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Draws logo tile-by-tile using tile indices from the image bank
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

    # Sets up and renders splash screen
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    while True:
        time.sleep(2.0)  # Waits before going to menu
        menu_scene()
        game.tick()

# Menu Scene: Title screen with instructions
def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    text = []

    # Game title text
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(12, 10)
    text1.text("Jay's Game Studios")
    text.append(text1)

    # Start prompt
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # Sets background grid
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Combines layers and renders menu
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            game_scene()
        game.tick()

# Game Over Scene: Shown after losing
def game_over_scene(final_score):
    sound = ugame.audio
    sound.stop()

    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Displays final score
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {0:>2d}".format(final_score))
    text.append(text1)

    # Game over message
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    # Prompt to restart
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

# Game Scene: Main gameplay
def game_scene():
    # Spawns a new alien
    def show_alien():
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE),
                    constants.OFF_TOP_SCREEN)
                break

    # Score display setup
    score = 0
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # Lives display setup
    lives = 3
    lives_text = stage.Text(width=29, height=20)
    lives_text.clear()
    lives_text.cursor(1, 1)
    lives_text.move(2, 1)
    lives_text.text("Lives: {0}".format(lives))

    # Load images and sounds
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Set up player and enemies
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    lasers = [stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
              for _ in range(constants.TOTAL_NUMBER_OF_LASERS)]

    aliens = [stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
              for _ in range(constants.TOTAL_NUMBER_OF_ALIENS)]

    show_alien()

    # Game setup
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [lives_text] + [score_text] + lasers + [ship] + aliens + [background]
    game.render_block()

    # Game loop
    while True:
        keys = ugame.buttons.get_pressed()

        # A button logic
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            a_button = constants.button_state["button_up"]

        if keys & ugame.K_SELECT:
            supervisor.reload()

        if keys & ugame.K_RIGHT:
            ship.move(min(ship.x + 1, constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT:
            ship.move(max(ship.x - 1, 0), ship.y)

        # Shooting logic
        if a_button == constants.button_state["button_just_pressed"]:
            for laser in lasers:
                if laser.x < 0:
                    laser.move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # Move lasers
        for laser in lasers:
            if laser.x > 0:
                laser.move(laser.x, laser.y - constants.LASER_SPEED)
                if laser.y < constants.OFF_TOP_SCREEN:
                    laser.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # Check for laser collision with alien
        for laser in lasers:
            if laser.x > 0:
                for alien in aliens:
                    if alien.y > 0 and stage.collide(laser.x + 6, laser.y + 2, laser.x + 11, laser.y + 12,
                                                     alien.x + 1, alien.y, alien.x + 15, alien.y + 15):
                        alien.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        laser.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        sound.stop()
                        sound.play(boom_sound)
                        show_alien()
                        score += 1
                        score_text.clear()
                        score_text.move(1, 1)
                        score_text.text("Score: {0}".format(score))

        # Move aliens
        for alien in aliens:
            if alien.x > 0:
                alien.move(alien.x, alien.y + constants.ALIEN_SPEED)
                if alien.y > constants.SCREEN_Y:
                    alien.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score = max(score - 1, 0)
                    score_text.clear()
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # Alien hits player
        for alien in aliens:
            if alien.x > 0 and stage.collide(alien.x + 1, alien.y, alien.x + 15, alien.y + 15,
                                             ship.x, ship.y, ship.x + 15, ship.y + 15):
                sound.stop()
                sound.play(crash_sound)
                lives -= 1
                lives_text.clear()
                lives_text.move(1, 1)
                lives_text.text("Lives: {0}".format(lives))
                if lives > 0:
                    game_scene()
                else:
                    time.sleep(3.0)
                    game_over_scene(score)

        # Redraw all objects
        game.render_sprites(aliens + lasers + [ship])
        game.tick()


if __name__ == "__main__":
    splash_scene()