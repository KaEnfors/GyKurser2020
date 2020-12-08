"""
Platformer Game
"""
import random
import os
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Rickad Hämtar kaffe "
#Game character
CHARACTER_SCALING = 0.1
#Player speed, per frame 
MOVEMENT_SPEED = 0

class MyGame(arcade.Window):
    # Main Code
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        #arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.background = None
        print("Loaded init")
        #Game list collison 
        self.player_list = None
        #Sprite variable
        self.player_sprite = None

        #Player keep tracks of player movement
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Drag and drop
        # List of games we are dragging with the mouse
        self.held_players = None

        # Original location of playerheld we are dragging with the mouse in case
        # they have to go back.
        self.held_players_original_position = None 

    def setup(self):
        # Call to Restart Game
        self.background = arcade.load_texture("C:/Users/abdulrahman.sulayma/Desktop/PythonArcade/images/bk/TileableBackGround.png")
        print("Loaded setup")
        #Loads sprite for the game
        
        #Load player sprite
        self.player_list = arcade.SpriteList()

        #Settings up sprite coordinates
        image_source = "images/player/player.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # helad by players
        # List of playerheld we are dragging with the mouse
        self.held_player = []

        # Original location of playerheld we are dragging with the mouse in case
        # they have to go back.
        self.held_player_original_position = []


    def on_draw(self):
        arcade.start_render()
        """ Render the screen. """
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()
        # Code to draw the screen goes here

    def on_update(self, delta_time):
        MOVEMENT_SPEED = + 10

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0 
        self.player_sprite.change_y = 0 

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = +MOVEMENT_SPEED 

        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED 

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED 

        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = +MOVEMENT_SPEED 

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False



    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        
        # Get list of playerheld we've clicked on
        playerheld = arcade.get_sprites_at_point((x, y), self.player_list)

        # Have we clicked on a card?
        if len(playerheld) > 0:

            # Might be a stack of playerheld, get the top one
            primary_player = playerheld[-1]

            # All other cases, grab the face-up card we are clicking on
            self.held_player = [primary_player]
            # Save the position
            self.held_player_original_position = [self.held_player[0].position]
            # Put on top in drawing order
            self.pull_to_top(self.held_player[0])

    def on_mouse_release(self, x: float, y: float, button: int,modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any playerheld, who cares
        if len(self.held_player) == 0:
            return

        # We are no longer holding playerheld
        self.held_player = []

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding playerheld, move them with the mouse
        for card in self.held_player:
            card.center_x += dx
            card.center_y += dy

    
          

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()