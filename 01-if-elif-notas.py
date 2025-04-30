nota = float(input("introduce tu nota: "))
if 0 <= nota and nota < 5:
    print("Suspenso")
elif 5 <= nota and nota < 7:
    print ("Aprobado")
elif 7 <= nota and nota < 9:
    print("Notable")
elif 9 <= nota and nota <= 10:
    print("Sobresaliente")
else:
    print("Fuera de rango")