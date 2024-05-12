from os import system
system("cls") #system clear

#Números aleatorios se hace con una librería
import random
numero_random_1 = random.randint(1,10)

#for con range
for i in range (1,9,1):
    print(i)

#El for recorre palabras también
palabra = str.lower(input("Ingrese su palabra por favor: "))
for e in palabra:
    print(e)

#Listas
mi_lista = ["Hola", "Mundo"]
print(mi_lista[1])

#Agregar elemento a Listas
mi_lista.append("Python")
print(mi_lista[2])

#Agregar elemento en una posición específica a Listas
mi_lista.insert(1,"Insertado")
print(mi_lista)

#Agregar elemento al inicio de Lista
mi_lista.insert(0,"Algo")
print(mi_lista)

#Reemplazar un elemento a Listas
mi_lista[2] = "Nuevo"
print(mi_lista)

#Elimino un elemento de la Lista por posición
del mi_lista[2]
print(mi_lista)

#Elimino un elemento de la Lista por elemento
mi_lista.remove("Mundo")
print(mi_lista)

#Largo de la Lista
lista_nuevo = ["Primero", "Segundo", "Tercero", "Cuarto", "Quinto"]
largo_lista = len(lista_nuevo)

#Recorro por posición
pos = 0
while pos < len(lista_nuevo):
    print(lista_nuevo[pos])
    pos += 1

for i in range (0,len(lista_nuevo)):
    print(lista_nuevo[i])

#Recorro por elemento
for elemento in lista_nuevo:
    print(elemento)