from core import PhysicsSprite




class Muskroom(PhysicsSprite):
    pass



class Muscrab(PhysicsSprite):
    animation_frame = 0
    animation_speed = 4
    animation_count = 2

    def on_update(self, delta):
        super().on_update(delta)
        self.animation_frame += delta * self.animation_speed #0-1.99999999999
        if self.animation_frame >= self.animation_count:
            self.animation_frame = 0

        self.texture = self.textures[int(self.animation_frame)] #[tex1, tex2]




