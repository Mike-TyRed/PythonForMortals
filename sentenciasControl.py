engine = str(input("Database Engine: --"))      #solicitar datos al usuario
#host = str(input("Host: "))
port = str(input("Port: "))

if engine == "Postgres" and port == "5432":
    print("Postgres use the next Host: 127.0.0.1")
else:
    print("Database Engine Unknow")