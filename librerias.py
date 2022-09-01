import random
import math

print(random.randint(1, 100))   #numero random entre inicio y límite

print(random.random())          #numero random entre 0 y 1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         #numero random dentro de una lista
r = random.choice(lista)
print(math.sin(r))
print(r)

