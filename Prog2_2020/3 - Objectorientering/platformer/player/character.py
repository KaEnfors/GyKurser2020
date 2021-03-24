from core import PhysicsSprite
import arcade

class Character(PhysicsSprite):
    keys = None
    
    jetforce = 20
    maxfuel = 3
    jettime = maxfuel
    texture_left = None
    texture_right = None

    fire = False
    flame : arcade.Sprite = None
    flame_textures : None #left1, left2, right1, right2
    flame_texture_alt = 0


    health = 100

    def on_update(self, delta):
        
        
        if self.keys['LEFT']:
            self.direction = 'LEFT'
            self.ax += -1 * self.movementspeed
            self.texture = self.texture_left
            #Change direction left
            
        if self.keys['RIGHT']:
            self.direction = 'RIGHT'
            self.ax += 1 * self.movementspeed
            self.texture = self.texture_right

        if self.keys['UP'] and self.jettime > 0:
            self.ay += self.jetforce
            self.jettime -= delta
#            print("JUMP!", self.ay)
            #Change direction right

        if self.position[1] <= self.height/2: #Nuddar marken? true/false
            if self.jettime < self.maxfuel:
                self.jettime += delta*2
            
            # Starta timer om ingen timer igång...
            # Om.. timer 0 -> sätt jettime till max...

        if self.keys['FIRE'] and not self.fire:
            self.flame = arcade.Sprite(scale=0.3)
            self.fire = True
        elif not self.keys['FIRE'] and self.fire:
            self.flame = None
            self.fire = False

        if self.fire:
            offset = int(self.flame_texture_alt)
            if self.direction == 'RIGHT':
                self.flame.texture = self.flame_textures[0 + offset] #Left = 0,1
                self.flame.center_x, self.flame.center_y = self.center_x, self.center_y
                self.flame.center_x +=120
            else:
                self.flame.texture = self.flame_textures[2 + offset] #Right = 2,3
                self.flame.center_x, self.flame.center_y = self.center_x, self.center_y
                self.flame.center_x -=120
            self.flame_texture_alt += delta*15
            self.flame_texture_alt %= 2

        super().on_update(delta)
#        print(self.keys)

    
    def set_keys(self, keymap):
        self.keys = keymap

    def take_damage(self, amount):
        if self.health > 0:
            self.health -= amount


    def draw(self):
        super().draw()
        
        if self.fire:
            self.flame.draw()

        fuelpercentage = (self.jettime / self.maxfuel) * 100
        if fuelpercentage < 0:
            fuelpercentage = 0
        elif fuelpercentage > 100:
            fuelpercentage = 100

        arcade.draw_text("Fuel:" + str(int(fuelpercentage)) + "%", start_x=0,  start_y=300, color=arcade.color.WHITE)
        arcade.draw_text("Health:" + str(self.health), start_x=0,  start_y=330, color=arcade.color.RED)
#        self.draw_hit_box(color=arcade.color.GREEN) 