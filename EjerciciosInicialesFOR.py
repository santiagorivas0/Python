#Ejercicio 1. Imprimir en pantalla los números del 1 al 10
for i in range(1,11,1):
    print(i)

#Ejercicio 2. Imprimir en pantalla los números del 10 al 1
for a in range (11,0,-1):
    print(a)

#Ejercicio 3. Pedir al usuario que ingrese un número e imprimir en pantalla todos los números desde el cero hasta el número ingresado
num = int(input("Ingrese su número por favor: "))
for b in range (1,num+1,1):
    print(b)

#Ejercicio 4. Imprimir en pantalla todos los números del 10 al 50
for c in range(10,50,1):
    print(c)

#Ejercicio 5. Escribir en pantalla todos los números pares del 0 al 100
for d in range(0,101,2):
    print(d)

#Ejercicio 6. Pedir al usuario que ingrese una palabra y mostrar en pantalla las letras de esa palabra
palabra = str.lower(input("Ingrese su palabra por favor: "))
for e in palabra:
    print(e)

#Ejercicio 7. Dada una lista: lista_frutas = [“Manzana”, “Sandía”, “Frutilla”, “Banana”, Mandarina”], recorrer la lista e imprimirla en pantalla 
lista_frutas = ["Manzana", "Sandía", "Frutilla", "Banana", "Mandarina"]
for fruta in lista_frutas:
    print(fruta)

#Ejercicio 8.  Dada la lista de usuarios: lista_usuarios = [“Maria”, “Juan”, “Ana], buscar a un usuario en la lista (recorro por elemento)
lista_usuarios =  ["Maria", "Juan", "Ana"]
usu = str.capitalize(input("Ingrese nombre que está buscando: "))
existe = False
for nombre in lista_usuarios:
    if nombre == usu:
        print("Existe el usuario.")
        existe = True
if not existe:
    print("El usuario no existe")
    
#Ejercicio 9. Dada la lista: lista_frutas = [“Manzana”, “Sandía”, “Frutilla”, “Banana”, Mandarina”], recorrer la lista por índice e imprimir en pantalla cada una de las frutas
lista_frutas2 = ["Manzana", "Sandía", "Frutilla", "Banana", "Mandarina"]
for posicion in range(0,len(lista_frutas2)):
    print(lista_frutas[posicion])

#Ejercicio 10. Crear una lista que contenga los números del 0 al 50
numeros = []
for i in range(0,51,1):
    numeros.append(i)
print(numeros)