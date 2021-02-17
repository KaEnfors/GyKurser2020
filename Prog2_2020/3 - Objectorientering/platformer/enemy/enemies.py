from core import PhysicsSprite




class Muskroom(PhysicsSprite):
    pass



class Muscrab(PhysicsSprite):
    animation_frame = 0

    def on_update(self, delta):
        super().on_update(delta)
        self.animation_frame += delta
        if self.animation_frame >= 2:
            self.animation_frame = 0

        self.texture = self.textures[int(self.animation_frame)]




