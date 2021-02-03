import arcade
from .core import InputController


class MuskFormer(arcade.Window):
    
    

    def run(self):
        print("Run game")
        arcade.run()
        


    def on_key_press(self, key, modifiers):
        print("You pressed:", key)

    def on_key_release(self, key, modifiers):
        print("You released:", key)


if __name__ == "__main__":
    MuskFormer(fullscreen=False, title="Muskformer").run()