import arcade, os, math
from arcade import Sprite



class Player(arcade.Sprite):
    

    def __init__(self, file=None, scale=1.0, x=0, y=0):
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
    
    def update(self):
        self.angle += self.dangle

        ddx = -math.sin(math.radians(self.angle))
        ddy = math.cos(math.radians(self.angle))

        self.velx = arcade.lerp(self.velx, ddx, 0.05)
        self.vely = arcade.lerp(self.vely, ddy, 0.05)

        self.speed = arcade.lerp(self.speed, self.dspeed, 0.05)
        
        self.change_x = self.velx * self.speed
        self.change_y = self.vely * self.speed


        super().update()



class SpriteGame(arcade.Window):

    player : object
    
    def __init__(self, width=800, height=660, title="SpriteGame"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width


    def setup(self):
        path = os.path.abspath(__file__)
        directory = os.path.dirname(path)
        spritefile = directory + '/static/ship_blue.png'
        self.player = Player(file=spritefile, scale=0.6, x=self.WINDOW_W/2, y=self.WINDOW_H/2)
        self.player2 = Player(file=spritefile, scale=0.6, x=self.WINDOW_W/3, y=self.WINDOW_H/3)

    def run(self):
        arcade.run()

    

    def on_key_press(self, key, modifiers):

        p = self.player

        if key == arcade.key.W:
            p.dspeed += 10
        if key == arcade.key.S:
            p.dspeed += -5
        if key == arcade.key.A:
            p.dangle += 10
        if key == arcade.key.D:
            p.dangle += -10

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

        self.player.update()
        self.player2.update()

    def on_draw(self):


        arcade.start_render()
        
        self.player.draw()
        self.player2.draw()