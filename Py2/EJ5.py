#. Pide al usuario que ingrese las longitudes de los lados de un triángulo. Utiliza condicionales
#para determinar si el triángulo es equilátero, isósceles, escaleno o no válido.

lado1 = input("ingrese el 1er lado del triangulo: ")
lado2 = input("ingrese el 2do lado del triangulo: ")
lado3 = input("ingrese el 3er lado del triangulo: ")

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
   
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("El triángulo es isósceles.")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("El triángulo es escaleno.")
else:
    print("Los lados ingresados no forman un triángulo válido.")


