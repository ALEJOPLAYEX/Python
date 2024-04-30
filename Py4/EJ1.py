""" . Pregunte al usuario cuántos elementos desea ingresar en una lista, luego solicite cada uno de ellos y presente el contenido de la lista y su
contenido invertido. """

elementos = int(input("¿Cuántos elementos desea ingresar en la lista? "))
elementos_num = (elementos)
lista = []
for i in range(0, elementos_num):
    elemento = input("Ingrese un elemento: ")
    lista.append(elemento)  
print("Lista original: ", lista)
lista.reverse()
print("Lista invertida: ", lista)
