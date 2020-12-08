import arcade, os, math
from arcade import Sprite


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
        self.player = Sprite(filename=spritefile, scale=0.6)
        self.player.center_x = self.WINDOW_W/2
        self.player.center_y = self.WINDOW_H/2

        self.speed = 0
        self.rotation = 0
        self.dangle = 0
        
        

    def run(self):
        arcade.run()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            self.speed += 10
        if key == arcade.key.S:
            self.speed += -5
        if key == arcade.key.A:
            self.dangle += 10
        if key == arcade.key.D:
            self.dangle += -10

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W:
            self.speed -= 10
        if key == arcade.key.S:
            self.speed -= -5
        if key == arcade.key.A:
            self.dangle -= 10
        if key == arcade.key.D:
            self.dangle -= -10





    def on_update(self, deltatime):

        self.rotation += self.dangle        
        dx = -math.sin(math.radians(self.rotation)) * self.speed
        dy = math.cos(math.radians(self.rotation)) * self.speed
        
        self.player.change_x = dx
        self.player.change_y = dy
        self.player.angle = self.rotation
        self.player.update()

    def on_draw(self):

        arcade.start_render()

        self.player.draw()