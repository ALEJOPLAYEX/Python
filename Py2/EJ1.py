""" Escribir un programa que controle el estado del motor y lo apague si la temperatura supera
los 80 grados.
 """
estado = int(input("Ingrese la temperatura del motor: "))

if estado > 80:
    print("El motor se apagará")
else: 
    print("El motor está encendido")

