import arcade, math, os, random
from random import randrange
from arcade.gui import UIManager

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
CURSOR_SCALLING = 1 
menuheight = SCREEN_HEIGHT*0.9
BULLET_SPEED = 10
BULLET_COOLDOWN_TICKS = 15
SCREEN_TITLE = "Rickad Hämtar kaffe "

#Shooting Speed


def draw_background():
    """This function draws menu"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH,SCREEN_HEIGHT, menuheight, (0, 0, 127, 100))


class Bullet(arcade.Sprite):
    def __init__(self, file=None, scale=1.0, x=0, y=0, angle=0, tilt_angle=90, rot_angle=0, rot_speed=2):
        super().__init__(filename=file, scale=scale)
        self.angle = angle
        self.center_x = x + (-math.sin(math.radians(self.angle +tilt_angle)) * rot_angle)
        self.center_y = y + (math.cos(math.radians(self.angle +tilt_angle)) * rot_angle)

        self.change_x = -math.sin(math.radians(self.angle)) * 5 * rot_speed
        self.change_y = math.cos(math.radians(self.angle)) * 5 * rot_speed 


class Turret(arcade.Sprite):
    projectiles : object

    def __init__(self, file=None, scale=1.0, x=0, y=0, projfile=None):
        super().__init__(filename=file, scale=scale)

        #Spawn pos for turrets
        self.center_x = x
        self.center_y = y
        #Bullet
        self.projectile = projfile
        #print("Turret Init Loaded")
        

    def update(self, mouse_x=0, mouse_y=0):
        # (x,y) pos for the turret
        self.start_x = self.center_x 
        self.start_y = self.center_y
        #Get the dest for the target
        dest_x = mouse_x
        dest_y = mouse_y
 
        #Calculate the dis to get the angle, by using atan2
        x_diff = dest_x - self.start_x
        y_diff = dest_y - self.start_y
        angleData = Aim_angle = math.atan2(y_diff, x_diff)
        self.angle = math.degrees(Aim_angle)-90
        
        super().update()

        

def TurretBuy(self):
    SCREEN_WIDTH_WP_MENU = SCREEN_WIDTH - 50
    dir = os.path.dirname(os.path.abspath(__file__))

    self.background = arcade.load_texture(dir + "/images/bk/TileableBackGround.png")
    self.trigger_sprite = arcade.Sprite(dir + "/images/turrets/lvlturret1.png", scale=0.5, center_x=SCREEN_WIDTH_WP_MENU, center_y=menuheight+30)
    self.trigger_sprite1 = arcade.Sprite(dir + "/images/random/elonsexy.jpg", scale=0.1, center_x=65, center_y=menuheight+30)
    
def turret(self, turretlevelTexture):
    if self.TurretLevel == 1:
        self.turrets = Turret(file=turretlevelTexture, scale=0.6, x=self.WINDOW_W/2, y=self.WINDOW_H/2)
        self.turrets_list.append(self.turrets)
    elif self.TurretLevel == 2:
        self.turrets2 = Turret(file=turretlevelTexture, scale=0.6, x=self.WINDOW_W/2, y=self.WINDOW_H/2)
        self.turrets_list.append(self.turrets2)
    elif self.TurretLevel == 3:
        self.turrets3 = Turret(file=turretlevelTexture, scale=0.6, x=self.WINDOW_W/2, y=self.WINDOW_H/2)
        self.turrets_list.append(self.turrets3)

def mouse(self, texturemouse):
    self.mouse_list = arcade.SpriteList()
    self.mouse_sprite = arcade.Sprite(texturemouse, CURSOR_SCALLING)
    self.mouse_sprite.center_x = 0
    self.mouse_sprite.center_y = 0
    self.mouse_list.append(self.mouse_sprite)

def shooting_Turret(self):
        for turrets in self.turrets_list:
            turrets.update(mouse_x=self.mouse_x , mouse_y=self.mouse_y)
            
            #Target
            dest_x = self.mouse_x
            dest_y = self.mouse_y
            #Main POS
            start_x = turrets.center_x
            start_y = turrets.center_y
            #cal the angle
            x_diffrence = dest_x - start_x
            y_diffrence = dest_y - start_y
            Aim_angle = math.atan2(y_diffrence, x_diffrence)
            angleData = math.degrees(Aim_angle)- random.randint(85,95)
            dir = os.path.dirname(os.path.abspath(__file__))
            if self.frame_count % random.randint(self.FROM_SHOT_FIRED, self.AFTER_SHOT_FIRED) == 0:
                leftp = Bullet(dir + "/images/bullet/bullet.png", scale=1*1.2, x=turrets.center_x, y=turrets.center_y, angle=angleData, tilt_angle=self.rot_angle, rot_angle=0)
                self.bullet_list.append(leftp)
                arcade.play_sound(self.gun_sound)
            if self.frame_count % random.randint(self.FROM_SHOT_FIRED, self.AFTER_SHOT_FIRED) == 0:
                rightp = Bullet(dir + "/images/bullet/bullet.png", scale=1*1.2, x=turrets.center_x, y=turrets.center_y, angle=angleData, tilt_angle=self.rot_angle, rot_angle=0)
                self.bullet_list.append(rightp)
                arcade.play_sound(self.gun_sound)


class MyGame(arcade.Window):

    def __init__(self, width=800, height=660, title="SpriteGame"):
        super().__init__(width,height,title)
        # Sound
        dir = os.path.dirname(os.path.abspath(__file__))
        self.gun_sound = arcade.load_sound(dir + "/images/sound/shootsound.mp3")

        # List of games we are dragging with the mouse
        self.held_players = None
        
        # Original location of playerheld we are dragging with the mouse in case
        # they have to go back.
        self.held_players_original_position = None 

        #Mouse click (This is bad mouse interigation, but for now it has to do)
        self.mouse_cooldown = 0
        #Loading Var
        self.background = None
        
        #List Data storage
        self.mouse_list = None
        self.mouse_sprite = None
        
        #Turret
        self.turrets_list = None
        self.trigger_sprite = None

        #Bullets
        self.bullet_list = None
        self.bullet_list2 = None
        self.cooldown = 0
        
        #Window Height
        self.WINDOW_H = height
        self.WINDOW_W = width
        self.Mouse_clicked = False
        self.frame_count = 0
        
        #The Game money
        self.money=1000 +200
        print("Loaded main init")



    def setup(self):
        
        #Turret level
        self.TurretLevel = 1
        self.tilt_angle = 1
        self.tilt_angle_negativ = 1
        self.rot_angle = 75
        #shooting speed
        self.FROM_SHOT_FIRED = 30
        self.AFTER_SHOT_FIRED = 35

        self.bullet_list = arcade.SpriteList()
        self.bullet_list2 = arcade.SpriteList()
        self.turrets_list = arcade.SpriteList()
        # Texture Loading
        dir = os.path.dirname(os.path.abspath(__file__))
        self.TurretspriteLvl1 = dir + "/images/turrets/lvlturret1.png"
        self.TurretspriteLvl2 = dir + "/images/turrets/lvlturret2.png"
        self.TurretspriteLvl3 = dir + "/images/turrets/lvlturret3.png"

        self.turretlevelTexture = self.TurretspriteLvl1


        self.bullettexture = dir + "/images/bullet/bullet.png"
        #Mouse coursor Texuture
        self.mouse_UnPressed = dir + "/images\mouse\cursor.png"
        self.mouse_Pressed = dir + "/images\mouse\cursorpressed.png"

        #make mouse invisible 
        self.set_mouse_visible(False)
        TurretBuy(self)
        mouse(self, self.mouse_UnPressed)
        self.held_player = []
        self.held_player_original_position = []

        #Bullet intervall speed


        print("Main setup Loaded")

    def on_update(self, delta_time):
        #A bad way of making fucking delay; change this later on. Or game will lag!
        self.frame_count += 1

        #Mouse cooldown(bad idea!)
        self.mouse_cooldown += 1
        hit_trigger = arcade.check_for_collision(self.mouse_sprite, self.trigger_sprite)
        if hit_trigger:
            if self.Mouse_clicked==True and self.money > 0:
                if self.mouse_cooldown < BULLET_COOLDOWN_TICKS:
                    return
                self.mouse_cooldown = 0
                #Levling up system for turrets texturing
                if self.TurretLevel == 1:
                    self.turretlevelTexture = self.TurretspriteLvl1

                elif self.TurretLevel == 2:
                    self.turretlevelTexture = self.TurretspriteLvl2
                    self.tilt_angle = 18
                    self.tilt_angle_negativ = -18

                elif self.TurretLevel == 3:
                    self.turretlevelTexture = self.TurretspriteLvl3
                turret(self, self.turretlevelTexture)
                self.money -= 200
                print("SPAWN SPAWN SPAWn")
        #Make var; take mouse pos for coursor
        self.mouse_y = self.mouse_sprite.center_y
        self.mouse_x = self.mouse_sprite.center_x
        self.turrets_list.update()
        shooting_Turret(self)



        # Loop through each bullet

        for bullet in self.bullet_list:
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()
                #print("bullet removed")
            
        self.bullet_list.update()
    # Fun when key pressed
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.TurretLevel += 1
            self.FROM_SHOT_FIRED = 20
            self.AFTER_SHOT_FIRED = 21
            for turrets in self.turrets_list:
                self.turrets_list.update()
            print("Upgraded")
    #Fun when mouse unpressed
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.Mouse_clicked = True
        mouse(self, self.mouse_Pressed)
        self.mouse_sprite.center_x = x
        self.mouse_sprite.center_y = y
        print("helo iam being clikced :fluhed:")

        # Get list of playerheld we've clicked on
        playerheld = arcade.get_sprites_at_point((x, y), self.turrets_list)
        # Have we clicked on a card?
        if len(playerheld) > 0:
            # Might be a stack of playerheld, get the top one
            primary_player = playerheld[-1]
            # All other cases, grab the face-up card we are clicking on
            self.held_player = [primary_player]
            # Save the position
            self.held_player_original_position = [self.held_player[0].position]
            # Put on top in drawing order
            # self.pull_to_top(self.held_player[0])   
    #When mouse un pressed
    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.Mouse_clicked = False
        mouse(self, self.mouse_UnPressed)
        self.mouse_sprite.center_x = x
        self.mouse_sprite.center_y = y
        print("Unclicked ;(")
    
        # If we don't have any playerheld, who cares
        if len(self.held_player) == 0:
            return
        # We are no longer holding playerheld
        self.held_player = []

    #Mouse motion
    def on_mouse_motion(self, x, y, dx, dy):
        # Move the center of the mouse sprite to match the mouse x, y
        self.mouse_sprite.center_x = x
        self.mouse_sprite.center_y = y
        
        # If we are holding playerheld, move them with the mouse
        for card in self.held_player:
            card.center_x += dx
            card.center_y += dy

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        start_y = self.WINDOW_H/1.2
        start_x = self.WINDOW_W/1.1
        arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Money: "+str(self.money)+"$", start_x, start_y, arcade.color.BLACK, 14, width=200, align="center", anchor_x="center", anchor_y="center")
        self.bullet_list.draw()
        self.turrets_list.draw()
        draw_background()
        self.trigger_sprite.draw()
        self.trigger_sprite1.draw()
        self.mouse_list.draw()

        
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    #print("\n"*100)
    #print("(((: WELCOME TO MY GAME\nPRESS ENTER TO CONTINUE :))))\nV:1.0")
    #input("\n")
    main()