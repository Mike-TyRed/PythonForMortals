#dicts.py

#Diccionarios, tipo de dato compuesto por clave valor

d = {"port":5432, "engine":"postgres", "host":"127.0.0.1", "odbc":"psycopg2"}

print(d["port"], d["engine"])   #imprimir un clave del diccionario en específico

print(d)
d["engine"] = "PostgreSql"      #actualizar clave del diccionario
d["host"] = "localhost"
print(d)

d[12] = 34                      #agregar clave nombre de la clave "12" y su valor "34"
d["23"] = "abc"
print(d)

del d[12]                       #borrar clave en específico
del d["23"]
print(d)

print(d.keys())                 #saber las claves existentes
print(d.values())               #saber los valores existentes
print(d.items())                #imprime la clave y valor