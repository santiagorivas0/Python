from os import system
system("cls") #system clear

#Ejercicio 1. Usando una estructura de iteración while, retornar el resultado de sumar los números del 1 al 10.
suma = 0
contador = 1
while contador <= 10:
    suma = suma + contador
    contador = contador + 1
print("La suma de los números del 1 al 10 es:", suma)
