

#Solicite al usuario que ingrese dos numeros enteros, intercambie los valores de las variable sin usar una variable temporal e imprima los valores intercambiados.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un 2do numero: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Primer numero Intercambiado: ", num1)
print("Segundo numero Intercambiado: ", num2)


