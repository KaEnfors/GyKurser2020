import arcade



class KarlGame(arcade.Window):

    WINDOW_W: int
    WINDOW_H: int
    TITLE: str



    def __init__(self, width=800, height=660, title="Title"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width

        self.posx = self.WINDOW_W/2
        self.posy = self.WINDOW_H/2

        self.ddx = 0
        self.ddy = 0
    
        self.dx = 0
        self.dy = 0
        self.speed = 5

        self.radius = 50

        


    def run(self):
        

        arcade.run()

    def on_key_press(self, key, modifiers):


        if arcade.key.D == key:
            self.ddx += 1
        if arcade.key.A == key:
            self.ddx += -1
        if arcade.key.W == key:
            self.ddy += 1
        if arcade.key.S == key:
            self.ddy += -1




    def on_key_release(self, key, modifiers):

        if arcade.key.D == key:
            self.ddx -= 1
        if arcade.key.A == key:
            self.ddx -= -1
        if arcade.key.W == key:
            self.ddy -= 1
        if arcade.key.S == key:
            self.ddy -= -1


    def contain_ball(self):

        print("(",self.posx, ",", self.posy,")")
        
        if self.WINDOW_W + self.radius < self.posx:
            self.posx = 0
            print("Outofbounds HÖGER")
        elif 0 > self.posx:
            self.posx = self.WINDOW_W
            print("Outofbounds VÄNSTER")
        elif self.WINDOW_H + self.radius < self.posy:
            self.posy = 0
            print("Outofbounds UPP")
        elif 0 > self.posy:
            self.posy = self.WINDOW_H
            print("Outofbounds NER")


        
    
    def on_update(self, deltatime):
        """
        Funktion som körs i början av varje frame, varje "tick". 
        Updaterar alla modeller, och dess värden.
        """        
        super().on_update(deltatime)

        self.dx += (self.ddx - self.dx)/20
        self.dy += (self.ddy - self.dy)/20


        self.posx += self.dx * self.speed
        self.posy += self.dy * self.speed

        self.contain_ball()

    
    def on_draw(self):
        """
        Funktion som körs i slutet av varje frame. Renderar bilden.
        """
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_MAGENTA)
        arcade.draw_circle_filled(self.posx, self.posy, self.radius,  arcade.color.RICH_ELECTRIC_BLUE)

        super().on_draw()

