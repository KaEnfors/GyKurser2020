from core import PhysicsSprite
import arcade


class Character(PhysicsSprite):
    keys = None
    movementspeed = 10
    jetforce = 20
    jettime = 2
    texture_left = None
    texture_right = None

    def on_update(self, delta):

        
        if self.keys['LEFT']:
            self.ax += -1 * self.movementspeed
            self.texture = self.texture_left
            #Change direction left
            
        if self.keys['RIGHT']:
            self.ax += 1 * self.movementspeed
            self.texture = self.texture_right

        if self.keys['UP'] and self.jettime > 0:
            self.ay += self.jetforce
            self.jettime -= delta
#            print("JUMP!", self.ay)
            #Change direction right

        if self.position[1] <= self.height/2:
            self.jettime = 2

        super().on_update(delta)
#        print(self.keys)

    
    def set_keys(self, keymap):
        self.keys = keymap


    def draw(self):
        super().draw()

        fuelpercentage = (self.jettime / 2) * 100

        arcade.draw_text("Fuel:" + str(int(fuelpercentage)) + "%", start_x=0,  start_y=300, color=arcade.color.WHITE)
