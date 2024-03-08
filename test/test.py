class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        print("je m'éxecute father")
        Base.__nb_instances += 1
        self.id = Base.__nb_instances
        self.__privateone = "I'm private motherfucker"

class User(Base):
    """ My User class """
    def __init__(self):
        print("Je m'éxecute son")
        super().__init__()
    def essaie(self):
        print("Je m'éxecute son")
u = User()
print(u._Base__privateone)
