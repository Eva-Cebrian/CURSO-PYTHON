numero = int(input("Escribe un numero para saber si es un numero primo: "))
i = 2
while numero % i != 0: 
    # mientras numero no sea divisible entre i, sigue buscando el siguiente numero
    i = i + 1
    # el bucle avanza
if i == numero:
    print("El numero " + str(numero) + " es primo")
else:
    print("El numero " + str(numero) + " NO es primo")