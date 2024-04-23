#Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha
#calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres
#calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del
#examen final. 15% de la calificación de un trabajo final.
parcial1 = int(input("ingrese la nota del 1er parcial:"))
parcial2 = int(input("ingrese la nota del 2do parcial:"))
parcial3 = int(input("ingrese la nota del 3er parcial:"))
examen_final = int(input("ingrese la nota del examen final:"))
trabajo_final = int(input("ingrese la nota del trabajo final:"))

promedio = ((parcial1+parcial2+parcial3)/ 3)


notfinal = ((promedio * 0.55)+(examen_final*0.30)+(trabajo_final*0.15))

print("Nota Final:", notfinal)
