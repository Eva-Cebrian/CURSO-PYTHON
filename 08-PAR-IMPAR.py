# numero = int(input("Escribe un numero: "))
# if numero % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")
import random
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')



# # print(random.randint(1,10))

# suerte = random.randint(1,2)

# if suerte == 1:
#     print("Cara")
# else:
#     print("Cruz")

# lista = ["Eva", "Cebrian", "Perez"]
# print(lista)
# lista.append("Minaya")
# print("")
# print(lista)
# lista.extend(["Josefina", "Perez", "Arpa"])
# print("")
# print(lista)
amigos = ["Pepe", "Jacinto", "Maria", "Eva", "Carlos"]
numero = len(amigos)
resultado = random.randint(0,4)
print(resultado)
print("")
print(f"El amigo que tiene que pagar es:  {amigos[resultado]}")
print("")
print(f"El amigo que tiene que pagar es: {random.choice(amigos)}")




