import arcade, os
from core import InputController
from player.character import Character



class MuskFormer(arcade.Window):
    """

    """
    player : Character
    physics = {
        'gravity' : 100
    }


    def run(self):
        print("Run game")

        path = os.path.dirname(__file__)
        self.player = Character(physics=self.physics, filename=path+'/player/player_sprite.png', scale=0.2, center_x=500, center_y=500)
        arcade.run()
        

    def on_key_press(self, key, modifiers):
        print("You pressed:", key)

    def on_key_release(self, key, modifiers):
        print("You released:", key)


    

    def on_update(self, deltatime):
        #print("Update!")
        self.player.on_update(delta=deltatime)


    def on_draw(self):
        #print("Draw!")
        arcade.start_render()
        self.player.draw()

if __name__ == "__main__":
    MuskFormer(fullscreen=False, title="Muskformer").run()