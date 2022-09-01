from unicodedata import name


class Miclase(object):
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        return self.name

objeto = Miclase("John Wick")

print(objeto.get_name())
print(objeto.set_name("Neo"))