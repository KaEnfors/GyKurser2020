

class Birds():
    pass

class Bugs():
    pass

class Leaf():
    color : str
    
    def change_color(self, newColor):
        self.color = newColor



class Branch():
    
    def __init__(self):
        self.leaves = []
        self.birds = []

    def fall(self):
        for l in self.leaves:
            l.change_color("orange")
        self.leaves = []

    def spring(self):
        for i in range(5):
            self.leaves.append(Leaf())
        
        for l in self.leaves:
            self.leaves.change_color('green')
            
    def add_bird():
        pass
    
    def build_nest():
        pass

class Root():
        
    def __init__(self):
        self.roots = []
        self.size = 1

    def suck_water(self):
        self.size += 1
        self.roots.append(Root())
        for root in self.roots():
            root.suck_water()

class Tree():

    def __init__(self):
        self.roots = []
        self.branches = []
        self.age = 100

        for i in range(10):
            self.grow()


    def grow(self):
        newBranch = Branch()
        newRoot = Root()

        self.branches.append(newBranch)
        self.roots.append(newRoot)

        for r in self.roots:
            r.suck_water()






tree = Tree()

tree.grow()
tree.grow()
tree.grow()
tree.grow()
tree.grow()
tree.grow()







