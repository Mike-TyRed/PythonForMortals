#listas.py

l = [54, 12, 67, 23]

print(l)        #lista completa

l.append(65)    #agrega elementos a la lista

l.insert(0, 7)  #inserta valores, 0 siendo el objetivo y 7 lo que vamos a insertar

print(l)

print(l[0])     #eliges qué índice imprimir
print(l[2])

for item in l:  #ejemplo de iteración de lista
    print(item)

del(l)          #borra toda la lista
del(l[2])       #elegimos el índice que será borrado

l.sort()            #ordena el contenido de la lista
print(l)

print(sorted(l))      #ordena sin alterar la estrucuta de la lista