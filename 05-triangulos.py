# DADO UN NUMERO GENERAR UN PATRON DE TRIANGULOS
numero = int(input("Escribe un numero: "))
for i in range(1, numero + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()

# OTRA SOLUCION COMO NO EMPIEZA DESDE EL 1 AÑADE EL 0
print()
print("Solucion añadiendo el 0")
for i in range(numero+1):
    fila = list(range(i+1))
    print(*fila)

# TRIANGULO CON *
print()
print("Solucion con asteriscos")
for i in range(1, numero + 1):
   print("*" * i)

