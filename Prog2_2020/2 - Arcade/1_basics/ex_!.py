


class Structure():

    def __init__(self, arg1, arg2, arg3=None, status="-"):
        self.status=status # RUnning
        self.values = arg1 + arg2 #7
        self.sample = arg3 # 999

    def display(self):
        print(self.values) #7
        print(self.status) #Running
        print(self.sample) #999

ob = Structure(5,2, 999, "Running")
ob.display()
