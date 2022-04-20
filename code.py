#!/usr/bin/env python3

# Created by: Aleksandr Ten 
# Created on: April 2022
# This program is the "Space Aliens" program on the PyBadge


import constants
import stage
import ugame

def menu_scene():
    # this function is the main menu scene

    # image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # sets the background, 10x8
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # creates a stage, sets to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # order of layers
    game.layers = text + [background]
    # render the background and sprite list, most likely once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # redraw Sprites
        game.tick()


def game_scene():
    # this function is the main game game_scene

    # image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # sets the background, 10x8
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # creates a stage, sets to 60fps
    game = stage.Stage(ugame.display, 60)
    # order of layers
    game.layers = [ship] + [alien] + [background]
    # render the background and sprite list, most likely once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

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

        # A button to fire
        if keys & ugame.K_X != 0:
            print("A")
        if keys & ugame.K_O != 0:
            print("B")
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN != 0:
            ship.move(ship.x, ship.y + 1)

        # update game logic
        # play sound on A being pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()
