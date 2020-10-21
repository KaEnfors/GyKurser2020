import arcade




class KarlBall():
    pos_x : float
    pos_y : float
    dx : float
    dy : float
    size : float
    speed : float

    def __init__(self, x=0, y=0):
        super().__init__(width,height,title)

        self.pos_x = x
        self.pos_y = y
        self.dx = 0.0
        self.ddx = 0.0
        self.dy = 0.0
        self.ddy = 0.0
        self.speed = 10.0
        self.size = 50.0


class KarlGame(arcade.Window):

    WINDOW_W: int
    WINDOW_H: int
    TITLE: str



    pos_x : float
    pos_y : float
    dx : float
    dy : float
    size : float
    speed : float



    def __init__(self, width=800, height=660, title="Title"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width
        self.pos_x = width/2
        self.pos_y = height/2
        self.dx = 0.0
        self.ddx = 0.0
        self.dy = 0.0
        self.ddy = 0.0
        self.speed = 10.0
        self.size = 20.0
        


    def run(self):
        

        arcade.run()

    def on_key_press(self, key, modifiers):


        if key == arcade.key.UP:
            self.ddy += 1
        elif key == arcade.key.DOWN:
            self.ddy -= 1


        if key == arcade.key.RIGHT:
            self.ddx += 1
        elif key == arcade.key.LEFT:
            self.ddx -= 1


    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.ddy -= 1
        elif key == arcade.key.DOWN:
            self.ddy += 1


        if key == arcade.key.RIGHT:
            self.ddx -= 1
        elif key == arcade.key.LEFT:
            self.ddx += 1


    def contain_ball(self):
        if self.pos_x > self.WINDOW_W or self.pos_x < 0:
            self.dx *= -3
        if self.pos_y > self.WINDOW_H or self.pos_y < 0:
            self.dy *= -3

    
    def on_update(self, deltatime):
        """
        Funktion som körs i början av varje frame, varje "tick". 
        Updaterar alla modeller, och dess värden.
        """        
        super().on_update(deltatime)
        self.dx = arcade.lerp(self.dx, self.ddx * self.speed, 0.05)
        self.dy = arcade.lerp(self.dy, self.ddy * self.speed, 0.05)
        self.contain_ball()

        self.pos_x += self.dx
        self.pos_y += self.dy


    
    def on_draw(self):
        """
        Funktion som körs i slutet av varje frame. Renderar bilden.
        """
        arcade.start_render()
        arcade.set_background_color(arcade.color.RED)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.size,  arcade.color.BLUE)

        super().on_draw()