import arcade, os
from player.character import Character
from enemy.enemies import Muskroom, Muscrab

"""
TODO
- Skjuta 
    - rätt alignment
    - Flamethrowr?
        - samma fuel?
- Spawns?
    - Pickups
        - Fuel
    - Enemies?
- Map
    -Större? Scroll?





"""
class MuskFormer(arcade.Window):
    """

    """
    player : Character
    physics = {
        'gravity' : 100
    }
    key_map = {
        'UP' : False,
        'DOWN' : False,
        'LEFT' : False,
        'RIGHT' : False,
        'FIRE' : False
    }
    enemies = []

    gameover = False

    def run(self):
        print("Run game")

        path = os.path.dirname(__file__)
        self.player = Character(physics=self.physics, filename=path+'/player/player_sprite.png', scale=0.3, center_x=100, center_y=200)
        self.player.set_keys(keymap=self.key_map)
        self.player.texture_left = arcade.load_texture(file_name=path+'/player/player_sprite.png', flipped_horizontally=True)
        self.player.texture_right = arcade.load_texture(file_name=path+'/player/player_sprite.png')

        flame = []
        flame.append(arcade.load_texture(file_name=path+'/player/flamethrower.png'))
        flame.append(arcade.load_texture(file_name=path+'/player/flamethrower.png', flipped_vertically=True))
        flame.append(arcade.load_texture(file_name=path+'/player/flamethrower.png', flipped_horizontally=True))
        flame.append(arcade.load_texture(file_name=path+'/player/flamethrower.png', flipped_horizontally=True, flipped_vertically=True))

        self.player.flame_textures = flame



#        for i in range(10):
#            newenemy = Muskroom(physics=self.physics, filename=path+'/enemy/muskroom_sprite.png', scale=0.2, center_x=200+i*30, center_y=400)
#            self.enemies.append(newenemy)

        self.thecrab = Muscrab(physics=self.physics, filename=path+'/enemy/s_muskrab1.png', scale=0.5, center_x=500, center_y=200)
        self.thecrab.textures = []
        self.thecrab.textures.append(arcade.load_texture(file_name=path+'/enemy/s_muskrab1.png'))
        self.thecrab.textures.append(arcade.load_texture(file_name=path+'/enemy/s_muskrab2.png'))
#        self.thecrab.textures.append(arcade.load_texture(file_name=path+'/enemy/muskroom_sprite.png'))

        self.thecrab.target = self.player
        self.background_color = arcade.color.AUROMETALSAURUS
        arcade.run()
        

    def on_key_press(self, key, modifiers):
#        print("You pressed:", key)

        if arcade.key.W == key:
            self.key_map['UP'] = True
        if arcade.key.S == key:
            self.key_map['DOWN'] = True
        if arcade.key.A == key:
            self.key_map['LEFT'] = True
        if arcade.key.D == key:
            self.key_map['RIGHT'] = True
        if arcade.key.SPACE == key:
            self.key_map['FIRE'] = True





    def on_key_release(self, key, modifiers):
#        print("You released:", key)
        if arcade.key.W == key:
            self.key_map['UP'] = False
        if arcade.key.S == key:
            self.key_map['DOWN'] = False
        if arcade.key.A == key:
            self.key_map['LEFT'] = False
        if arcade.key.D == key:
            self.key_map['RIGHT'] = False
        if arcade.key.SPACE == key:
            self.key_map['FIRE'] = False

    def end_game(self):
        self.background_color = arcade.color.BLACK_BEAN


    def collision(self):

        if self.player.fire:
            if arcade.check_for_collision(self.thecrab, self.player.flame):
                self.thecrab.take_damage(1)
        
#        hits = arcade.check_for_collision_with_list(self.player.flame, self.enemies)

#        for enemyhit in hits:
#            enemyhit.kill()
#            self.enemies.remove(enemyhit)



    def on_update(self, deltatime):
        #print("Update!")
        if self.gameover:
            self.end_game()
            return

        self.player.on_update(delta=deltatime)
        self.thecrab.on_update(deltatime)
        self.thecrab.update_animation(deltatime)
        for enemy in self.enemies:
            enemy.on_update(delta=deltatime)

        if self.player.health <= 0:
            self.gameover = True

        self.collision()

#        self.physics['gravity'] = 0
#        print(self.key_map)

    def on_draw(self):
        #print("Draw!")
        arcade.start_render()
        
        self.player.draw()

        self.thecrab.draw()
        
        for enemy in self.enemies:
            enemy.draw()

        if  self.gameover:
            arcade.draw_text("GAME OVER!", 400, 300, arcade.color.RED, font_size=10)


if __name__ == "__main__":
    MuskFormer(fullscreen=False, width=1270, height=660, title="Muskformer").run()