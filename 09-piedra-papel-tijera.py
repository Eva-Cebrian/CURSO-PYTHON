import random
opciones = ["piedra", "papel", "tijera"]
eleccion_usuario = input("elige piedra, papel o tijera: ")
if eleccion_usuario == "piedra":
    resultado_usuario = opciones[0]
elif eleccion_usuario == "papel":
    resultado_usuario = opciones[1]
else:
    resultado_usuario = opciones[2]

eleccion_ordenador = random.choice(opciones)

print(f"{eleccion_ordenador} - ORDENADOR")

binomio1 = ["piedra", "papel"]
binomio1_1 =["papel", "piedra"]
binomio2 = ["piedra", "tijera"]
binomio2_2 = ["tijera", "papel"]
binomio3 = ["papel", "tijera"]
binomio3_3 = ["tijera", "papel"]

lista_obtenida = [eleccion_usuario, eleccion_ordenador]
print(lista_obtenida)

if lista_obtenida == binomio1:
    print("Ha ganado el ORDENADOR")
elif lista_obtenida == binomio1_1:
    print("Ha ganado el USUARIO")
elif lista_obtenida == binomio2:
    print("Ha ganado el USUARIO")
elif lista_obtenida == binomio2_2:
    print("Ha ganado el USUARIO")
elif lista_obtenida == binomio3:
    print("Ha ganado el ORDENADOR")
elif lista_obtenida == binomio3_3:
    print(eleccion_usuario)
else:
    print("Empate")