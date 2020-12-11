


class Cloud():
    
    def __init__(self, size=50):
        self.size = 50


class Tree():
    
    def __init__(self):
        pass

class Background():
    
    def __init__(self):
        self.cloud = Cloud(size=75)


game = Background()
game.cloud.size

