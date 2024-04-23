#Debera solicitarle al usuario el monto de 5 transacciones todas con valores reales, además
#calcular el valor total de lo que se perdio en el redondeo en todas las transacciones y
#presentar este valor con un redondeo de hasta 3 decimales. Debes mostrar cada monto
#original y el valor redondeado, la suma de todas las transacciones redondeadas y el valor que
#se perdio del redonde




transaccion1 = float(input("Ingrese el monto de la transacción 1: "))
transaccion2 = float(input("Ingrese el monto de la transacción 2: "))
transaccion3 = float(input("Ingrese el monto de la transacción 3: "))
transaccion4 = float(input("Ingrese el monto de la transacción 4: "))
transaccion5 = float(input("Ingrese el monto de la transacción 5: "))

transaccion1_redondeada = round(transaccion1)
transaccion2_redondeada = round(transaccion2)
transaccion3_redondeada = round(transaccion3)
transaccion4_redondeada = round(transaccion4)
transaccion5_redondeada = round(transaccion5)

perdida1 = transaccion1 - transaccion1_redondeada
perdida2 = transaccion2 - transaccion2_redondeada
perdida3 = transaccion3 - transaccion3_redondeada
perdida4 = transaccion4 - transaccion4_redondeada
perdida5 = transaccion5 - transaccion5_redondeada

suma_transacciones_redondeadas = (transaccion1_redondeada +
                                  transaccion2_redondeada +
                                  transaccion3_redondeada +
                                  transaccion4_redondeada +
                                  transaccion5_redondeada)

perdida_total = perdida1 + perdida2 + perdida3 + perdida4 + perdida5

print("Transacción 1 - Monto original:", transaccion1, "Monto redondeado:", transaccion1_redondeada)
print("Transacción 2 - Monto original:", transaccion2, "Monto redondeado:", transaccion2_redondeada)
print("Transacción 3 - Monto original:", transaccion3, "Monto redondeado:", transaccion3_redondeada)
print("Transacción 4 - Monto original:", transaccion4, "Monto redondeado:", transaccion4_redondeada)
print("Transacción 5 - Monto original:", transaccion5, "Monto redondeado:", transaccion5_redondeada)


print("Suma de todas las transacciones redondeadas:", suma_transacciones_redondeadas)


print("Valor total perdido por redondeo:", round(perdida_total, 3))
