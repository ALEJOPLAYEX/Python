""" Pide al usuario que ingrese tres números y realiza las siguientes operaciones aritméticas con
ellos:
Suma de los tres números.
Resta del tercer número al resultado de la suma de los dos primeros.
Multiplicación de los tres números.
División del primer número entre la suma del segundo y tercer número. Imprime los
resultados.
 """


num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un 2do numero: "))
num3 = int(input("Ingrese un 3er numero: "))

Suma = num1 + num2 + num3
Resta = num3 - (num1 + num2)
Multiplicación = num1 * num2 *num3
Division = num1 / (num2 + num3)

print("Resultado Suma: ", Suma)
print("Resultado Resta: ", Resta)
print("Resultado Multiplicacion: ", Multiplicación)
print("Resultado Division: ", Division)