""" En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para
determinar si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe
marcar como rechazada y enviar una alerta al operador. Si la pieza cumple con los estándares
de calidad, se debe marcar como aprobada y continuar con la producción.
Realice un programa que lea una entrada binaria en la que los 1s significan estándares de
calidad cumplidos y los 0s significan estándares de calidad No cumplidos. El programa debe
rechazar la pieza ante cualquier estándar no cumplido.
 """
entrada_binaria = input("Ingrese la entrada binaria (0s y 1s): ")

def inspeccionar_pieza(entrada_binaria):
    if '0' in entrada_binaria:
        print("Pieza rechazada. No cumple con los estándares de calidad.")
    else:
        print("Pieza aprobada. Cumple con los estándares de calidad.")

inspeccionar_pieza(entrada_binaria)
