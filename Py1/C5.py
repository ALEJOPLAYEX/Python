#Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad
#de frutos recolectados y la cantidad de frutos producidos en total.
cantidad_de_frutos_recolectados = int(input("ingrese el 1er numero: "))
cantidad_de_frutos_producido = int(input("ingrese el 2do numero: "))

indice_de_cosecha = (cantidad_de_frutos_recolectados / cantidad_de_frutos_producido) * 100

print("Cantidad total: ", indice_de_cosecha)
