


class MySuperClass():
    
    myvalue : int

    def __init__(self):
        self.myvalue = 55


class MyChildClass(MySuperClass):
    
    def __init__(self):
        self.myvalue = 65
        super().__init__()

obj = MyChildClass()

print(obj.myvalue)