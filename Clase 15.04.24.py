from os import system
system("cls") #system clear

#Variables acumuladoras y contadoras

contador = 1
suma = 0
while contador <= 10:
    #print(contador)
    contador = contador + 1 #contador +=1
    suma = suma + contador #suma += contador
    print(suma)