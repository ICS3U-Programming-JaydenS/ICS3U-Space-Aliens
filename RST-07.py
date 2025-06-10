# Created By: Jayden Smith
# Date: May 12, 2025
# This is the RST project


import ugame
import stage
import constants
def menu_scene():
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    text = []
    text1 = stage.Text (width = 29, height = 12, font =None, palette = constants.NEW_PALETTE, buffer=None)
    text1.move(12,10)
    text1.text("Jay's Game Studios")
    text.append(text1)

    text2 = stage.Text(width = 29, height = 12, font =None, palette = constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    
    
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 
    
    
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()
    
    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            game_scene()
      
        # redraw Sprites
        
        game.tick()
def game_scene():
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16 ("space_aliens.bmp")
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 
    alien = stage.Sprite (image_bank_sprites, 9, int(constants.SCREEN_X/2 - constants.SCREEN_Y/2), 16)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [alien] + [background]
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
            sound.play (pew_sound)
        # update game logic
        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()
        
if __name__ == "__main__":
    menu_scene()