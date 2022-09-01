def hello(name = "Anonimo"):
    return "Hello world!", name

def sumar(x = 1, y = 2):
    return x + y

x = int(input("Escribe un número: "))
y = int(input("Escribe otro número: "))

print(sumar(x, y))

