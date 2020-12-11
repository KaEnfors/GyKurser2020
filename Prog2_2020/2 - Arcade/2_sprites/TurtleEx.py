import turtle


class Head(turtle.Turtle):

    def __init__(self, color):
        super().__init__()
        self.pencolor(color)

    def grow(self):
        self.pensize(5)

class SnakeGame():
    

    def __init__(self):
        self.display = turtle.Screen()

    def run(self):
#        self.snake = Head('blue')
#        self.snake2 = Head('green')

#        self.snake.forward(100)
#        self.snake2.back(100)

        self.display.mainloop()



# Run game...
game = SnakeGame()
game.run()
