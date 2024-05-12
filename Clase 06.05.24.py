from os import system
system ("clear")

#Funciones

temperatura = int(input("Ingrese la temperatura: "))
print("Usted ingresó: " + str(temperatura))

#Palabra clave: def y return (necesaria únicamente cuando la función retorna un valor)

def suma(num_1,num_2):
    la_suma = num_1 + num_2
    return la_suma

a = int(input("Ingrese su primer número: "))
b = int(input("Ingrese su segundo número: "))
la_suma = suma(a,b)
print("La suma de sus dos números es:",la_suma)

#Ejercicios iniciales con funciones

#1
def saludar(nombre):
    print("Hola",nombre,"¿cómo estás?")
#Invoco la función    
nombre = input("Ingrese su nombre: ")
saludar(nombre)

#2
def mayor_de_dos(num1,num2):
    mayor = 0
    if num1 > num2:
        mayor = num1
        print("El mayor es:",mayor)
    elif num1 == num2:
        mayor = num1
        print("Son iguales")
    else:
        mayor = num2
        print("El mayor es:",mayor)

num1 = int(input("Ingrese su primer núemro: "))
num2 = int(input("Ingrese su segundo núemro: "))
mayor_de_dos(50,63)

#3
def mayor_de_dos(num1,num2):
    mayor = 0
    if num1 > num2:
        mayor = num1
    else: 
        mayor = num2
    return mayor

def mayor_de_4(num1,num2,num3,num4):
    mayor1 = 0
    mayor2 = 0
    mayor_total = 0
    
    mayor1 = mayor_de_dos(num1,num2)
    mayor2 = mayor_de_dos(num3,num4)
    mayor_total = mayor_de_dos(mayor1,mayor2)
    return mayor_total
    
#Torneo de Fútbol Playa Mixto

#Defino mis estructuras
lista_participantes = [["Juan Perez", 25, "Nacional"],["Ana Gomez", 20, "Defensor Sporting"]]
lista_equipos = [["Nacional","A"],["Defensor Sporting", "A"]]
costo_inscripcion = 100

def mostrar_menu():
    print("Menú")
    print("1. Registrar participante")
    print("2. Mostrar cantidad de equipos")
    print("3. Mostrar equipos con jugadores")
    print("4. Total recaudado por inscripción")
    print("0. Salir")

def seleccionar_opcion():
    opcion = int(input("Ingrese una opción: "))
    while opcion not in [0,1,2,3,4]:
        print("La opción ingresada no es válida")
        opcion = int(input("Seleccione otra opción: "))
    return opcion

def registrar_participante():
    nombre_completo = str.capitalize(input("Ingrese nombre y apellido: "))
    edad = int(input("Ingrese la edad: "))
    nombre_equipo = str.capitalize(input("Ingrese nombre del equipo: "))
    existe = False
    for eq in lista_equipos:
        if eq[0] == nombre_equipo:
            existe = True
    if not existe:
        categoria = str.upper(input("Ingrese la categoría: "))
        nuevo_equipo = [nombre_equipo,categoria]
        lista_equipos.append(nuevo_equipo)
    nuevo_participante = [nombre_completo,edad,nombre_equipo]
    lista_participantes.append(nuevo_participante)
    print("El participante se registró correctamente")

def mostrar_cantidad_equipos():
    cantidad_equipos = len(lista_equipos)
    print("La cantidad de equipos es",cantidad_equipos)

mostrar_menu()
opcion = seleccionar_opcion()

while opcion != 0:
    if opcion == 1:
        registrar_participante()
    
    elif opcion == 2:
        mostrar_cantidad_equipos()
        
    elif opcion == 3:
        mostrar_equipos_con_jugadores()

    elif opcion == 4:
        total_recaudado()
        
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))