
import random
import arcade
import os
import PIL
from arcade.draw_commands import Texture

SPRITE_SCALING_SHIP = 0.1
SPRITE_SCALING_METEOR = 0.08
SPRITE_SCALING_LASER = 0.8
METEOR_COUNT = 80

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"

BULLET_SPEED = 5

EXPLOSION_TEXTURE_COUNT = 60


class Explosion(arcade.Sprite):
    """ Den här klassen skapar en explotion animation """

    def __init__(self, texture_list):
        super().__init__()

        # starta vid första bilden
        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        # uppdatera till nästa bild i animationen. om vi är vid slutet
        # av våra frames, radera då denna sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()


class MyGame(arcade.Window):
    """ Main klassen """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # variabler som håller sprite listorna
        self.player_list = None
        self.meteor_list = None
        self.bullet_list = None
        self.explosions_list = None

        # fixa player infot 
        self.player_sprite = None
        self.score = 0

        # visa inte muspekaren
        self.set_mouse_visible(False)

        # Pre-load animation frames. Vi gör inte detta i __init__
        # för explotionen därför att
        # det tar för kång tid så spelet skulle pausas.
        self.explosion_texture_list = []

        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = ":resources:images/spritesheets/explosion.png"

        # Ladda explotions animationen
        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        # Ladda ljuden som skall användas
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")

        arcade.set_background_color(arcade.color.ARSENIC)

    def setup(self):

        """ Ställ in spelet och initialisera variablerna. """

        # Sprite listorna
        self.player_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        # ställ in spelaren
        self.score = 0

        # Ladda player bilden
        self.player_sprite = arcade.Sprite("Spaceship.png", SPRITE_SCALING_SHIP)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Skapa meteorerna 
        for meteor_index in range(METEOR_COUNT):

            # Skapa meteor variabeln
            # ladda bilden på meteoren
            meteor = arcade.Sprite("Meteor.png", SPRITE_SCALING_METEOR)

            # positionera meteoren
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(150, SCREEN_HEIGHT)

            # addera meteroren till listan
            self.meteor_list.append(meteor)

        # bakgrunds bild/färg
        arcade.set_background_color(arcade.color.ARSENIC)

    def on_draw(self):
        """
        rendera skärmen.
        """

        # börja rendera skärmen
        arcade.start_render()

        # rita alla sprites.
        self.meteor_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.explosions_list.draw()

        # rendera texten
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Gunshot sound
        arcade.sound.play_sound(self.gun_sound)

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90

        # Give it a speed
        bullet.change_y = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()
        self.explosions_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a meteor
            hit_list = arcade.check_for_collision_with_list(bullet, self.meteor_list)

            # If it did...
            if len(hit_list) > 0:

                # Make an explosion
                explosion = Explosion(self.explosion_texture_list)

                # Move it to the location of the meteor
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y

                # Call update() because it sets which image we start on
                explosion.update()

                # Add to a list of sprites that are explosions
                self.explosions_list.append(explosion)

                # Get rid of the bullet
                bullet.remove_from_sprite_lists()

            # For every meteor we hit, add to the score and remove the meteor
            for meteor in hit_list:
                meteor.remove_from_sprite_lists()
                self.score += 1

                # Hit Sound
                arcade.sound.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()