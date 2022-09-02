class Animal(object):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.name = name

    def get_name(self):
        return self.name


class Perro(Animal):
    def dormir(self):
        return "Estoy dormido!"

p = Perro("Firulais")

print(p.get_name())
print(p.dormir())