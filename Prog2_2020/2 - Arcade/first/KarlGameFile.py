import arcade



class KarlGame(arcade.Window):

    WINDOW_W: int
    WINDOW_H: int
    TITLE: str

    def __init__(self, width=800, height=600, title="Title"):
        super().__init__(width,height,title)

    def run(self):
        arcade.run()

    
    def on_update(deltatime):
        """
        Funktion som körs i början av varje frame, varje "tick". Updaterar alla modeller, och dess värden.
        """
        super().on_update()
    
    def on_draw():
        """
        Funktion som körs i slutet av varje frame. Renderar bilden.
        """
        arcade.start_render()

        super().on_draw()