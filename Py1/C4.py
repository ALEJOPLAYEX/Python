#Pide al usuario que ingrese tres números. Utiliza solo operadores lógicos y relacionales para
#verificar si al menos dos de los números ingresados son iguales entre sí. Imprime un mensaje
#indicando el resultado de la verificación, por ejemplo: "Al menos dos de los números son
#iguales:" False

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un 2do numero: "))
num3 = int(input("Ingrese un 3er numero: "))

Igual = (num1 == num2) or (num1 == num3) or (num2 == num3) 
print(f"Al menos dos de los números son iguales:" [Igual])

