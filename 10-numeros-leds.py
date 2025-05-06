# Lista de patrones para los dígitos del 0 al 9
led_digits = [
    ["###", "# #", "# #", "# #", "###"],  # 0
    ["  #", "  #", "  #", "  #", "  #"],  # 1
    ["###", "  #", "###", "#  ", "###"],  # 2
    ["###", "  #", "###", "  #", "###"],  # 3
    ["# #", "# #", "###", "  #", "  #"],  # 4
    ["###", "#  ", "###", "  #", "###"],  # 5
    ["###", "#  ", "###", "# #", "###"],  # 6
    ["###", "  #", "  #", "  #", "  #"],  # 7
    ["###", "# #", "###", "# #", "###"],  # 8
    ["###", "# #", "###", "  #", "###"],  # 9
]

#pide numero a usuario, por ejemplo 123
numero_usuario=input("Escribe un numero: ")

#transforma la cadena en una lista -> [1, 2, 3]
numero_usuario_transf_lista_int = [int(digito) for digito in numero_usuario]

# Generamos la salida línea por línea
# for fila in range(5):
#     linea = ""
#     for indice in indices:
#         linea += led_digits[indice][fila] + "     "
#     print(linea)

for fila in range(5):
    linea = ""
    for i in numero_usuario_transf_lista_int:
        linea = linea + led_digits[i][fila] + " "
    print(linea)


