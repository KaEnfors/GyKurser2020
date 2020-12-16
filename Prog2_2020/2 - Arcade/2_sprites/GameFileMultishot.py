import arcade, os, math
from arcade import Sprite


class Projectile(arcade.Sprite):
    
    def __init__(self, file=None, scale=1.0, x=0, y=0, angle=0, tilt_angle=0, tilt_distance=0, tilt_speed=1):
        super().__init__(filename=file, scale=scale)
        self.angle = angle
        self.center_x = x + (-math.sin(math.radians(self.angle +tilt_angle)) * tilt_distance)
        self.center_y = y + (math.cos(math.radians(self.angle +tilt_angle)) * tilt_distance)

        self.change_x = -math.sin(math.radians(self.angle)) * 5 * tilt_speed
        self.change_y = math.cos(math.radians(self.angle)) * 5 * tilt_speed
    
    


class Player(arcade.Sprite):
    

    def __init__(self, file=None, scale=1.0, x=0, y=0, projfile=None):
        super().__init__(filename=file, scale=scale)

        self.center_x = x
        self.center_y = y

        self.accx = 0
        self.accy = 0

        self.velx = 0
        self.vely = 0

        self.dangle = 0
        
        self.dspeed = 0
        self.speed = 0


        self.projectile = projfile
        self.cooldown = 0

    def fire(self):
        if(self.cooldown > 0): return None
        self.cooldown = 30
        deltaspeed = self.speed/2
        right = Projectile(self.projectile, scale=0.7, x=self.center_x, y=self.center_y, angle=self.angle, tilt_angle=75, tilt_distance=30)
        left = Projectile(self.projectile, scale=0.7, x=self.center_x, y=self.center_y, angle=self.angle, tilt_angle=-75, tilt_distance=30)
        return [left, right]
        

    
    def update(self):
        self.angle += self.dangle

        ddx = -math.sin(math.radians(self.angle))
        ddy = math.cos(math.radians(self.angle))

        self.velx = arcade.lerp(self.velx, ddx, 0.05)
        self.vely = arcade.lerp(self.vely, ddy, 0.05)

        self.speed = arcade.lerp(self.speed, self.dspeed, 0.05)
        
        self.change_x = self.velx * self.speed
        self.change_y = self.vely * self.speed

        if self.cooldown > 0:
            self.cooldown -= 3

        super().update()


class SpriteGame(arcade.Window):

    player : object
    projectiles : object
    
    def __init__(self, width=800, height=660, title="SpriteGame"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width


    def setup(self):
        path = os.path.abspath(__file__)
        directory = os.path.dirname(path)
        spritefile = directory + '/static/ship_blue.png'

        projfile = directory + '/static/beam.png'

        self.player = Player(file=spritefile, scale=0.6, x=self.WINDOW_W/2, y=self.WINDOW_H/2, projfile=projfile) 
        self.projectiles = arcade.SpriteList()

    def run(self):
        arcade.run()


    def on_key_press(self, key, modifiers):

        p = self.player

        if key == arcade.key.W:
            self.player.dspeed += 10
        if key == arcade.key.S:
            p.dspeed += -5
        if key == arcade.key.A:
            p.dangle += 10
        if key == arcade.key.D:
            p.dangle += -10
        if key == arcade.key.SPACE:
            newProjectile = p.fire()
            if newProjectile:
                for p in newProjectile:
                    self.projectiles.append(p)


    def on_key_release(self, key, modifiers):

        p = self.player

        if key == arcade.key.W:
            p.dspeed -= 10
        if key == arcade.key.S:
            p.dspeed -= -5
        if key == arcade.key.A:
            p.dangle -= 10
        if key == arcade.key.D:
            p.dangle -= -10





    def on_update(self, deltatime):

        self.projectiles.update()
        self.player.update()

    def on_draw(self):

        
        arcade.start_render()
        
        self.projectiles.draw()
        self.player.draw()
