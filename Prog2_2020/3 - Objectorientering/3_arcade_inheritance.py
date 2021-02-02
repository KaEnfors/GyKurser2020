import arcade



class Character(arcade.Sprite):

    def on_update(self, delta_time: float = 1/60):
        super().on_update(delta_time=delta_time)

        

    def draw(self):
        pass




class Game(arcade.Window):
    player : Character
    scene : arcade.SpriteList

    def on_update(self, delta_time: float):
        pass


    def on_draw(self):
        pass





