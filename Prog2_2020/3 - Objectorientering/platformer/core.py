from arcade import Sprite, lerp

class InputController:
    pass





class PhysicsSprite(Sprite):

    ax, ay = 0, 0
    vx, vy = 0, 0

    def __init__(self, physics:dict, filename:str, scale=1.0, center_x=0, center_y=0):
        super().__init__(filename=filename, scale=scale, center_x=center_x, center_y=center_y)
        self.phys = physics


    def on_update(self, delta):
#        print('Updating physics')

        # Gravitation är alltid neråt -ay
        self.ay = self.phys['gravity'] *-4 *delta
#        print("Deltatime:",delta)
#        print(self.vy)


        # vx,vy ändras utifrån ax,ay
        self.vx, self.vy = lerp(self.vx, self.ax, 0.01), lerp(self.vy, self.ay, 0.01)

        if (self.position[1] < self.height/2): # Om Elon är längst ner, 
            self.vy = 0 #...sätt hastighet y-led till 0
#        print("Hastighet y-led:", self.vy)
        
        self.position = [self._position[0] + self.vx, self._position[1] + self.vy]
        self.angle += self.change_angle

        





    def get_movement_vector():
        pass

    def get_acceleration_vector():
        pass

