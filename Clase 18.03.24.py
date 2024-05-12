from os import system
system("cls") #system clear

#Imprimir Hola Mundo
print ("Hola Mundo")

#Defino un nombre
un_nombre = "Juan"

#Imprimir Hola + un_nombre con espacio
print ("Hola " + un_nombre)
print ("Hola" + "" + un_nombre)

#Imprimir Hola Ana y Juan
otro_nombre = "Ana"
print ("Hola " + un_nombre + " y " + otro_nombre)
print ("Hola", un_nombre,"y", otro_nombre)

#Imprimir 1+2
print (1+2)
print ("1"+"2")

un_numero = 1
otro_numero = "2"
print(un_numero + int(otro_numero)) #Convierto todo a número
print(str(un_numero) + otro_numero) #Convierto todo a texto

#Ingreso de Nombre
mi_usuario = input ("Ingrese su nombre de usuario: ")
mi_numero = int (input("Ingrese un numero: "))
print ("Bienvenido al programa", mi_usuario)
print (mi_numero)


print("------------------------------------")
#Quiero hacer café
cafetera_enchufada = True
if cafetera_enchufada == True :
    print("Prender Cafetera")
else:
    print("Enchufar Cafetera")