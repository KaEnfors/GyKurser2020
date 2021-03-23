import arcade
from core import PhysicsSprite


class Enemy(PhysicsSprite):

    target : arcade.Sprite = None
    checkpoint = None

    def on_update(self, delta):
        self.checkpoint = self.target.position
        #Kod för alla enemies...
        if self.direction == 'LEFT' and self.position[0] > self.checkpoint[0] +10:
            self.ax = -1 * self.movementspeed
        elif self.direction == 'RIGHT' and self.position[0] < self.checkpoint[0] -10:
            self.ax = 1 * self.movementspeed
            
#        print(self.checkpoint)
        if self.position[0] > self.checkpoint[0]: # 0 -> x 1 -> y
            self.direction = 'LEFT'
        elif self.position[0] < self.checkpoint[0]: # 0 -> x 1 -> y
            self.direction = 'RIGHT'

        super().on_update(delta)


class Muskroom(Enemy):
    pass



class Muscrab(Enemy):
    animation_frame = 0

    animation_speed = 2
    animation_count = 2

    movementspeed = 4

    next_hit_delay = 0

    def on_update(self, delta):
        super().on_update(delta)
        self.animation_frame += delta * self.animation_speed #0-1.99999999999
        if self.animation_frame >= self.animation_count:
            self.animation_frame = 0

        self.texture = self.textures[int(self.animation_frame)] #[tex1, tex2]

        if self.next_hit_delay <= 0:
            if arcade.check_for_collision(self.target, self):
                self.next_hit_delay = 1
                self.target.take_damage(10)
        else:
            self.next_hit_delay -= delta




#    def draw(self):
        #self.draw_hit_box(color=arcade.color.GREEN)    


