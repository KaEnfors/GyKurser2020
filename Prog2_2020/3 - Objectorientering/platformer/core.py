from arcade import Sprite, lerp







class PhysicsSprite(Sprite):

    ax, ay = 0, 0
    vx, vy = 0, 0
    accspeed = 0.1
    frame__time = 0

    def __init__(self, physics:dict, filename:str, scale=1.0, center_x=0, center_y=0):
        super().__init__(filename=filename, scale=scale, center_x=center_x, center_y=center_y)
        self.phys = physics

    def on_update(self, delta):
#        print('Updating physics')
        self.frame__time += delta
        

        if self.frame__time > 1:
            print("pre ay", self.ay)
        # Gravitation är alltid neråt -ay
        self.ay += (self.phys['gravity'] * -0.1)

        if self.frame__time > 1:
            self.frame__time = 0
            print("post ay", self.ay)

        # vx,vy ändras utifrån ax,ay
        self.vx, self.vy = lerp(self.vx, self.ax, self.accspeed), lerp(self.vy, self.ay, self.accspeed)

        if (self.position[1] < self.height/2 and self.vy < 0): # Om Elon är längst ner, 
            self.vy = 0 #...sätt hastighet y-led till 0
#        print("Hastighet y-led:", self.vy)
        
        self.position = [self._position[0] + self.vx, self._position[1] + self.vy]
        self.angle += self.change_angle

        self.ay = 0
        self.ax = 0





    def get_movement_vector():
        pass

    def get_acceleration_vector():
        pass

