import arcade, os, math
from arcade import Sprite


class SpriteGame(arcade.Window):

    player : object
    
    def __init__(self, width=800, height=660, title="SpriteGame"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width

        self.ddx = 0
        self.ddy = 0
        self.dx = 0
        self.dy = 0


    def setup(self):
        path = os.path.abspath(__file__)
        directory = os.path.dirname(path)
        spritefile = directory + '/static/ship_blue.png'
        self.player = Sprite(filename=spritefile, scale=0.6)
        self.player.center_x = self.WINDOW_W/2
        self.player.center_y = self.WINDOW_H/2

        self.speed = 0
        self.force = 0
        self.rotation = 0
        self.dangle = 0


        

    def run(self):
        arcade.run()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            self.force += 10
        if key == arcade.key.S:
            self.force += -5
        if key == arcade.key.A:
            self.dangle += 10
        if key == arcade.key.D:
            self.dangle += -10

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W:
            self.force -= 10
        if key == arcade.key.S:
            self.force -= -5
        if key == arcade.key.A:
            self.dangle -= 10
        if key == arcade.key.D:
            self.dangle -= -10





    def on_update(self, deltatime):
        # 0 - 360          
        self.rotation += self.dangle        
        ddx = -math.sin(math.radians(self.rotation))
        ddy = math.cos(math.radians(self.rotation))

        self.dx = arcade.lerp(self.dx, ddx, 0.05)
        self.dy = arcade.lerp(self.dy, ddy, 0.05)

        self.speed = arcade.lerp(self.speed, self.force, 0.05)
        
        self.player.change_x = self.dx * self.speed
        self.player.change_y = self.dy * self.speed
        self.player.angle = self.rotation
        self.player.update()


    def on_draw(self):

        arcade.start_render()

        self.player.draw()