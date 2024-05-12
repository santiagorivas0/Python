from os import system
system("cls") #system clear

#Encender/Enchufar la Cafetera
cartera_enchufa = True
if cartera_enchufa: 
    print ("Encenderla")
#else : 
    print ("Enchufarla")

#Identación
temperatura = 18
if (temperatura > 25):
    print ("Hace Calor")
else:
    if (temperatura < 15):
        print ("Hace Frío")
    else:
        if (temperatura < 20):
            print ("Está Fresco")
        else:
            print ("Está Agradable")

#Estructuras Repetitivas
numero = 1
while (numero <= 10):
    print(numero)
    numero = numero + 1

#Anidación Estructuras Repetitivas
contador = 1
while(contador <= 3):
    contador2 = 1
    while (contador2 <= 2):
        print ("Hip!")
        contador2 = contador2 + 1
    print ("Hurra!")
    contador = contador + 1

#Imprimir nombre de la persona
mi_nombre = input("Ingrese su Nombre: ") #input deja el espacio para que el usuario escriba
print ("Hola", mi_nombre)

cantidad = 4
print (f"Hay {cantidad} vasos en la mesa")