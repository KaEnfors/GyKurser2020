import arcade



class KarlGame(arcade.Window):

    WINDOW_W: int
    WINDOW_H: int
    TITLE: str


    player : object


    def __init__(self, width=800, height=660, title="Title"):
        super().__init__(width,height,title)
        self.WINDOW_H = height
        self.WINDOW_W = width
        #locx = int(1920 / 2)
        #locy = int(1080 / 2)
        #self.set_location(locx,locy)

    def run(self):
        
        self.player = [0, 0]

        arcade.run()
        arcade.start_render()
        arcade.set_background_color(arcade.color.RED)
        arcade.finish_render()
    
    def on_update(self, deltatime):
        """
        Funktion som körs i början av varje frame, varje "tick". Updaterar alla modeller, och dess värden.
        """
        

        super().on_update(deltatime)
    
    def on_draw(self):
        """
        Funktion som körs i slutet av varje frame. Renderar bilden.
        """
        arcade.start_render()
        arcade.set_background_color(arcade.color.RED)
        arcade.draw_circle_filled(600.4, 402.2, 50.0,  arcade.color.BLUE)

        super().on_draw()
        arcade.finish_render()