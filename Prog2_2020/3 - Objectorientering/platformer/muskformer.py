import arcade, os
from core import InputController
from player.character import Character
from enemy.muskrooms import Muskroom



class MuskFormer(arcade.Window):
    """

    """
    player : Character
    physics = {
        'gravity' : 100
    }
    enemies = []

    def run(self):
        print("Run game")

        path = os.path.dirname(__file__)
        self.player = Character(physics=self.physics, filename=path+'/player/player_sprite.png', scale=0.2, center_x=500, center_y=500)

        for i in range(10):
            newenemy = Muskroom(physics=self.physics, filename=path+'/enemy/muskroom_sprite.png', scale=0.2, center_x=200+i*30, center_y=400)
            self.enemies.append(newenemy)


        arcade.run()
        

    def on_key_press(self, key, modifiers):
        print("You pressed:", key)

    def on_key_release(self, key, modifiers):
        print("You released:", key)


    

    def on_update(self, deltatime):
        #print("Update!")

        self.player.on_update(delta=deltatime)

        for enemy in self.enemies:
            enemy.on_update(delta=deltatime)

        self.physics['gravity'] = 0
        print("No gravity")

    def on_draw(self):
        #print("Draw!")
        arcade.start_render()
        self.player.draw()

        for enemy in self.enemies:
            enemy.draw()


if __name__ == "__main__":
    MuskFormer(fullscreen=False, title="Muskformer").run()