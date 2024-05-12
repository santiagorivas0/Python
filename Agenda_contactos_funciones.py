from os import system
system ("clear")
lista_contactos = [["JUAN", "PÉREZ", "BVAR ESPAÑA", "JUAN@PEREZ.COM", 123456]]

def mostrar_contactos():
    #Mostrar contactos
        for contacto in lista_contactos:
            print(contacto[0], contacto[1], contacto[2], contacto[3], contacto[4])

def agregar_contacto():
    #Agregar contacto
    nombre = str.upper(input("Ingrese nombre: "))
    apellido = str.upper(input("Ingrese apellido: "))
    direccion = str.upper(input("Ingrese dirección: "))
    mail = str.upper(input("Ingrese mail: "))
    telefono = int(input("Ingrese número de teléfono: "))

    nuevo_contacto = [nombre,apellido,direccion,mail,telefono]
    lista_contactos.append(nuevo_contacto)

    print("El contacto se agregó correctamente")
    mostrar_contactos()

def mostrar_telefono():
    #Mostrar teléfono
    nombre = str.upper(input("Ingrese nombre: "))
    apellido = str.upper(input("Ingrese apellido: "))

    for contacto in lista_contactos:
        if contacto[0]==nombre and contacto[1]==apellido:
            print("El teléfono es", contacto[4])

def modificar_telefono():
    #Modificar teléfono
        nombre = str.upper(input("Ingrese nombre: "))
        apellido = str.upper(input("Ingrese apellido: "))

        for contacto in lista_contactos:
            if contacto[0]==nombre and contacto[1]==apellido:
                numero_nuevo = int(input("Ingrese teléfono nuevo: "))
                contacto[4] = numero_nuevo #Cambio el número de teléfono
                print("El nuevo teléfono de",contacto[0], contacto[1], "es", contacto[4])

def borrar_contacto():
     #Borrar contacto
        nombre = str.upper(input("Ingrese nombre: "))
        apellido = str.upper(input("Ingrese apellido: "))

        for contacto in lista_contactos:
            if contacto[0]==nombre and contacto[1]==apellido:
                lista_contactos.remove(contacto)
        
        mostrar_contactos()

def mostrar_menu():
    #Diseñar el Menú
    print("Menú")
    print("1. Agregar nuevo contacto")
    print("2. Mostrar todos los contactos")
    print("3. Mostrar teléfono de contacto")
    print("4. Modificar teléfono de un contacto")
    print("5. Borrar contacto")
    print("0. Salir")

def seleccionar_opcion():
    opcion = int(input("Ingrese una opción: "))
    while opcion not in [0,1,2,3,4,5]:
        print("La opción ingresada no es válida")
        opcion = int(input("Seleccione otra opción: "))
    return opcion

mostrar_menu()
opcion = seleccionar_opcion()


while opcion != 0:
    if opcion == 1:
        agregar_contacto()
    
    elif opcion == 2:
        mostrar_contactos()
        
    elif opcion == 3:
        mostrar_telefono()

    elif opcion == 4:
        modificar_telefono()

    elif opcion == 5:
         borrar_contacto()
        
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))