intentos = 3
while intentos > 0:
    if input("Escribe contraseña: ") == "contra":
        print("Contraseña CORRECTA")
        break
    intentos = intentos -1
    print("Contraseña INCORRECTA")
else:
    print("Se acabaron los intentos")