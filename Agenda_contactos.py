from os import system
system("cls") #system clear

#1
lista_contactos = [["JUAN","PÉREZ","BVAR. ESPAÑA","JUAN@PEREZ.COM",123456]]

#2
print("Menú")
print("1. Agregar nuevo contacto")
print("2. Mostrar todos los contactos")
print("3. Mostrar teléfono de contacto")
print("4. Modificar teléfono de un contacto")
print("5. Borrar contacto")
print("0. Salir")

opcion = int(input("Ingrese una opción: "))

while opcion != 0:
    if opcion == 1:
        #Agregar contacto
        nombre = str.upper(input("Ingrese nomnbre: "))
        apellido = str.upper(input("Ingrese apellido: "))
        direccion = str.upper(input("Ingrese dirección: "))
        mail = str.upper(input("ingrese mail: "))
        telefono = int(input("Ingrese número de teléfono: "))
        nuevo_contacto = [nombre,apellido,direccion,mail,telefono]
        lista_contactos.append(nuevo_contacto)
        print("El contacto se agregó correctamente")
    elif opcion == 2:
        #Mostar contactos
        for contacto in lista_contactos:
            print(contacto[0],contacto[1],contacto[2],contacto[3],contacto[4])
    elif opcion == 3:
        #Mostrar teléfono
        nombre = str.upper(input("Ingrese nomnbre: "))
        apellido = str.upper(input("Ingrese apellido: "))
        for contacto in lista_contactos:
            if contacto[0] == nombre and contacto[1] == apellido:
                print("El teléfono es:",contacto[4])
    elif opcion == 4:
        #Modificar teléfono
        nombre = str.upper(input("Ingrese nomnbre: "))
        apellido = str.upper(input("Ingrese apellido: "))
        for contacto in lista_contactos:
            if contacto[0] == nombre and contacto[1] == apellido:
                numero_nuevo = int(input("Ingrese teléfono nuevo: "))
                contacto[4] = numero_nuevo
                print("El nuevo teléfono de",contacto[0],contacto[1],"es:",contacto[4])
    elif opcion == 5:
        #Borrar contacto
        nombre = str.upper(input("Ingrese nomnbre: "))
        apellido = str.upper(input("Ingrese apellido: "))
        for contacto in lista_contactos:
            if contacto[0] == nombre and contacto[1] == apellido:
                lista_contactos.remove(contacto)
    print("Menú")
    print("1. Agregar nuevo contacto")
    print("2. Mostrar todos los contactos")
    print("3. Mostrar teléfono de contacto")
    print("4. Modificar teléfono de un contacto")
    print("5. Borrar contacto")
    print("0. Salir")           
    opcion = int(input("Ingrese una opción: "))