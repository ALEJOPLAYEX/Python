""" Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad. Si
el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la
matrícula. Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. Si el
estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la
edad es 18 años o mas, el descuento será del 5%.
Escribir el precio que deberá pagar un estudiante por su matrícula y el valor del descuento.
 """

estrato = int(input("Ingrese el estrato del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))

descuento = 0  

if estrato == 1:
    if edad < 18:
        descuento = 0.20
        print("El descuento es del 20%")
    else:
        descuento = 0.15
        print("El descuento es del 15%")
elif estrato == 2:
    if edad < 18:
        descuento = 0.10
        print("El descuento es del 10%")
    else:
        descuento = 0.05
        print("El descuento es del 5%")
else:
    print("No hay descuento para el estrato ingresado.")


valor_matricula = 1000  
descuento_aplicado = valor_matricula * descuento
precio_final = valor_matricula - descuento_aplicado


print("El valor del descuento es:", descuento_aplicado)
print("El precio final de la matrícula es:", precio_final)
