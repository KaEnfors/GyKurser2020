import arcade, os
from arcade import Sprite


class SpriteGame(arcade.Window):

    
    def __init__(self, width=800, height=660, title="SpriteGame"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width


    def setup(self):
#        path = os.path.abspath(__file__)
#        directory = os.path.dirname(path)
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory


    def run(self):
        arcade.run()


        

    def on_update(self, deltatime):
        pass

    def on_draw(self):

        arcade.start_render()

