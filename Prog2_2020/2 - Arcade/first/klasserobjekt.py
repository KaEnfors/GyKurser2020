

class User():
    name : str
    age : int

    def __init__(self, username="None", userage=-1):
        self.name = username
        self.age = userage


karl = User(userage=29, username="Kalle")
abbe = User()
efkan = User()
print(karl.name, " ", karl.age)
print(abbe.name)
print(efkan)


