from os import system
system("cls") #system clear

#Ejercicio 1. Escribir “Hola Mundo” por consola.
print("Hello World")

#Ejercicio 2. Leer por consola el nombre y apellido de una persona y devolver un saludo en el estilo “Hola nombre apellido” .
nombre_apellido = input("Dime tu nombre y apellido: ")
print("Hola",nombre_apellido )

#Ejercico 3. Leer por consola dos valores y mostrar el resultado de la suma.
mi_numero = int (input("Ingrese un numero: "))
mi_palabra = (input("Ingrese una palabra: "))
print(mi_numero,mi_palabra)

#Ejercicio 4. Leer tres valores y mostrar el promedio.
mi_numero = int (input("Ingrese primer numero: "))
mi_numero2 = int (input("Ingrese segundo numero: "))
mi_numero3 = int (input("Ingrese tercer numero: "))
print((mi_numero + mi_numero2+ mi_numero3)/3)

#Ejercicio 5. Ingresar por consola un valor en pesos uruguayos y un tipo de cambio para el Dólar y devolver la equivalencia en dólares.
pesos_uruguayos = float(input("Ingrese su valor en UYU: "))
tipo_cambio = pesos_uruguayos/40
print ("El valor en USD son:",float(tipo_cambio))

#Ejercicio 6. Para un equipo de fútbol el cálculo de los puntos obtenidos en el campeonato seasigna de la siguiente manera:
#1) Tres puntos por cada partido ganado. 2) Un punto por cada partido empatado. 3) Ningún punto por partido perdido.
#Solicitar el ingreso de partidos ganados, empatados y perdidos y calcular el total depuntos obtenidos por ese equipo.
partidos_ganados = int(input("Ingrese cantidad de partidos ganados: "))
partidos_ganados1 = partidos_ganados*3
partidos_empatados = int(input("Ingrese cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese cantidad de partidos perdidos: "))
partidos_perdidos1 = partidos_perdidos*0
print("La cantidad de puntos obtenidos en el campeonato son:",partidos_ganados1+partidos_empatados+partidos_perdidos1)

#Ejercicio 7. Ingresar un número entero e indicar si es positivo o negativo.
numero1 = int(input("Por favor ingrese su numero: " ))
if numero1 >= 0:
    print("Su numero es positivo")
else:
    print ("Su numero es negativo")

#Ejercicio 8. Ingresar dos valores numéricos y una operación ( “S” para suma, “R” para resta, “M” para multiplicaciòn, “D” para división y “P” para potencia). Dependiendo de la operación ingresada hacer el cálculo correspondiente y mostrar el resultado.
valor1 = int(input("Por favor ingrese su primer numero: " ))
valor2 = int(input("Por favor ingrese su segundo numero: " ))
operación = str.upper(input("Ingrese su tipo de operación S-Suma / R-Resta / M-Multiplicación / D-División / P-Potencia "))
if operación == "S":
    print(valor1+valor2)
else:
    if operación == "R":
        print(valor1-valor2)
    else:
        if operación == "M":
            print(valor1*valor2)
        else:
            if operación == "D":
                print(valor1/valor2)
            else:
                if operación == "P":
                    print(valor1**valor2)
                else:
                    print("Ingreso de manera incorrecta la operación")

# Ejercicio 9. Ingresar tres números y mostrarlos ordenados, de izquierda a derecha en forma creciente.
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
if n1<n2 and n1<n3:
    if n2<n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif n2<n1 and n2<n3:
    if n1<n3:
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
elif n3<n1 and n3<n2:
    if n1<n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)
 

# Ejercicio 10. . Escribir una aplicación que convierta temperatura de Fahrenheit a Celsius yviceversa. Se deberá pedir el valor de la temperatura y la unidad ( F o C) y calcular resultado. La fórmula de conversión es: C/5 =(F-32)/9
valor_temperatura = float(input("Ingresar el valor de la temperatura: "))
unidad = str.upper(input("Ingresar la unidad (C o F): ")) 
if unidad == "C":
    print("La temperatura en F es de:",((valor_temperatura*1.8)+32))
if unidad == "F":
    print("La temperatura en C es de:", (((valor_temperatura*5)-160)/9))
else:
    print("Usted ingresó la unidad incorrectamente")

# Ejercicio 11. Escribir un programa que genere la suma de dos números enteros al azar entre 1 y 10. Si la suma está entre 15 y 20 (incluyendo los límites), debe mostrar “en rango”.
import random
numero_random_1 = random.randint(1,10)
numero_random_2 = random.randint(1,10)
if 15 <= numero_random_1+numero_random_2 <= 20:
    print("En Rango")
else:
    print(numero_random_1+numero_random_2)

# Ejercicio 12. Escribir un programa en el cual se ingresan tres valores que representan el largo de los lados de un triángulo e indique si es un triángulo equilátero, isósceles o escaleno.
valor_triangulo1 = int(input("Ingresar el primer lado del triángulo: "))
valor_triangulo2 = int(input("Ingresar el segundo lado del triángulo: "))
valor_triangulo3 = int(input("Ingresar el tercer lado del triángulo: "))
if valor_triangulo1 == valor_triangulo2 and valor_triangulo2 == valor_triangulo3:
    print("Tu triángulo es de tipo equilatero por lo que tiene todos sus lados iguales")
elif valor_triangulo1 == valor_triangulo2 or valor_triangulo2 == valor_triangulo3 or valor_triangulo1 == valor_triangulo3: 
    print ("Tu triángulo es de tipo isósceles por lo que tiene dos lados iguales")
else: 
    print("Tu triángulo es de tipo escaleno por lo que tiene todos sus lados diferentes")

# Ejercicio 13. . Ingresar un número e indicar si es múltiplo de 7 y 3 simultáneamente.
ingresar_numero = int(input("Por favor ingresa tu número: "))
if (ingresar_numero % 7)*(ingresar_numero%3) == 0:
    print("Tu número es múltiplo de 3 y 7 simultáneamente")
else:
    print("Tu número no es múltiplo de 3 y 7 simultáneamente")

# Ejercicio 14. Crear una aplicación para ayudar a un usuario a tomar decisiones antes delevantarse. Se ingresa la temperatura exterior y el día de la semana y la aplicación deberá aconsejarle según las siguientes reglas:
#1) Los días domingo el usuario no trabaja y puede quedarse en casa.
#2) El resto de los días debe ir a trabajar.
#3) Si la temperatura está por debajo de los 10 grados el usuario debe “abrigarse mucho”, si la temperatura está por encima de los 20 grados el usuario deberá ponerse “ropa cómoda” y para casos intermedios deberá usar “abrigo moderado”.
temperatura_exterior = float(input("Ingresar la temperatura exterior: "))
dia_semana = input("Ingresar el día de la semana (nombre completo): ").upper()

if (dia_semana == "LUNES" or dia_semana == "MARTES" or dia_semana == "MIERCOLES" or 
    dia_semana == "JUEVES" or dia_semana == "VIERNES" or dia_semana == "SABADO"):
    if temperatura_exterior < 10:
        print("Levantarse. \nAbrigarse mucho. \nDebes ir al trabajo.")
    elif temperatura_exterior > 20:
        print("Levantarse. \nPonerse ropa cómoda. \nDebes ir al trabajo.")
    else:  # Asume que la temperatura está entre 10 y 20 grados
        print("Levantarse. \nPonerse abrigo moderado. \nDebes ir al trabajo.")
else:  # Asume que el día de la semana es Domingo
    if temperatura_exterior < 10:
        print("Levantarse. \nAbrigarse mucho. \nQuédese en casa, hoy no trabaja.")
    elif temperatura_exterior > 20:
        print("Levantarse. \nPonerse ropa cómoda. \nQuédese en casa, hoy no trabaja.")
    else:  # Asume que la temperatura está entre 10 y 20 grados
        print("Levantarse. \nPonerse abrigo moderado. \nQuédese en casa, hoy no trabaja.")

# Ejercicio 15. Se ingresan notas de curso de un grupo de estudiantes. Luego de cada ingreso mostrar la información actualizada indicando cuántos pasan a exámen ( nota < 70 ), cuántos exoneran el exámen ( nota > = 70 ) y cuántos sacaron una muy buena nota ( > 90 ). A su vez indicar cuál fue el promedio de notas, la nota máxima y la mínima. El programa finaliza cuando se ingresa una nota menor que cero.
a_examen = 0
exoneraron = 0
destacados = 0
total_estudiantes = 0
suma_notas = 0
nota_min = 101
nota_max = 0
nota = int(input("Ingrese su nota: "))
while nota > 0:
    total_estudiantes = total_estudiantes + 1
    suma_notas = nota + 1
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota
    if nota < 70:
        a_examen = a_examen + 1
    elif nota >= 70 and nota <= 90:
        exoneraron = exoneraron + 1
    else:
        destacados = destacados + 1
    print("Se fueron a exámen:",a_examen)
    print("Destacados:",destacados)
    print("Exoneraron:",exoneraron)
    print("El promedio de notas:",suma_notas/total_estudiantes)
    print("Nota mínima:",nota_min)
    print("Nota máxima:",nota_max)
    nota = int(input("Si desea salir ingrese númnero menor a cero. Sino ingrese su nota: "))
print("RESÚMEN DE NOTAS FINALES")
print("Se fueron a exámen:",a_examen)
print("Destacados:",destacados)
print("Exoneraron:",exoneraron)
print("El promedio de notas:",suma_notas/total_estudiantes)
print("Nota mínima:",nota_min)
print("Nota máxima:",nota_max)

# Ejercicio 16. Crear una aplicación que solicite la edad de un perro y la calcule en “años-perro”:
#1 - Para los primeros dos años, un año-perro equivale a 10.5 años de humano.
#2 - Después de esos dos años, cada año siguiente equivale a 4 años humanos. 
años_perro = int(input("Por favor ingrese la edad de su perro: "))
if años_perro <= 2: 
    print("La edad de su perro en años humanos es:",años_perro*10.5)
elif años_perro > 2:
        print("La edad de su perro en años humanos es:",21+años_perro*4)

# Ejercicio 17. Ingresar cinco números, indicar cuántos son múltiplos de 5, cuántos son mayores a 20 y cuantos cumplieron ambas condiciones en simultáneo.
multiplos_de_5 = 0
mayores_a_20 = 0
multiplos_de_5_y_mayores_a_20 = 0
for i in range (1,6):
    numero = int(input(f"Ingrese su número {i}: "))
    es_multiplo_de_5 = numero % 5 == 0
    es_mayor_a_20 = numero > 20
    if es_multiplo_de_5:
        multiplos_de_5 = multiplos_de_5 + 1
    if es_mayor_a_20:
        mayores_a_20 = mayores_a_20 + 1
    if es_multiplo_de_5 and es_mayor_a_20:
        multiplos_de_5_y_mayores_a_20 = multiplos_de_5_y_mayores_a_20 + 1
print(f"Números múltiplos de 5: {multiplos_de_5}")
print(f"Números mayores a 20: {mayores_a_20}")
print(f"Números que son múltiplos de 5 y mayores a 20: {multiplos_de_5_y_mayores_a_20}")

#Ejercicio 17. Otra forma de hacerlo
cumplen_ambas_condiciones = 0
multiplos_5 = 0
mayor_20 = 0
ingreso_de_numero = 0
while ingreso_de_numero < 5:
    num = int(input("Ingrese su número: "))
    if num % 5 == 0 and num > 20:
        cumplen_ambas_condiciones = cumplen_ambas_condiciones + 1
    elif num % 5 == 0:
        multiplos_5 = multiplos_5 + 1
    elif num > 20:
        mayor_20 = mayor_20 + 1
    ingreso_de_numero = ingreso_de_numero + 1
print("La cantidad que cumplen ambas condiciones es:",cumplen_ambas_condiciones)
print("Solo múltiplos de cinco",multiplos_5)
print("Solo mayores a veinte",mayor_20)

# Ejercicio 18. Crear una aplicación que nos genere una sugerencia de números para el Cinco de Oro. Mostrar los números en una fila, separados por comas.
import random
n1_random = random.randint(1,48)
n2_random = random.randint(1,48)
while n1_random == n2_random:
    n2_random = random.randint(1,48)
n3_random = random.randint(1,48)
while n2_random == n1_random or n2_random == n3_random:
    n3_random = random.randint(1,48)
n4_random = random.randint(1,48)
while n3_random == n4_random or n2_random == n4_random or n1_random == n4_random:
    n4_random = random.randint(1,48)
n5_random = random.randint(1,48)
while n4_random == n5_random or n3_random == n5_random or n2_random == n5_random or n1_random == n5_random:
    n5_random = random.randint(1,48)
print("Tus números para el 5 del oro son: ")
print(n1_random,n2_random,n3_random,n4_random,n5_random)

# Ejercicio 19. Escribir un programa para crear la tabla de multiplicación de un número entrado por consola. Por ejemplo, si se ingresa el número 6
num_tabla = int(input("Ingrese su número: "))
for multiplicación in range(1,11,1):
    print(num_tabla,"x",multiplicación, "=",num_tabla*multiplicación)

# Ejercicio 20. Ingresar un código de departamento y mostrar el nombre del departamento al que pertenece.
departamentos = {"A":"Canelones","B":"Maldonado","C":"Rocha","D":"Treinta y Tres","E":"Cerro Largo","F":"Rivera","G":"Artigas","H":"Salto","I":"Paysandú","J":"Río Negro","K":"Soriano","L":"Colonia","M":"San José","N":"Flores","O":"Florida","P":"Lavalleja","Q":"Durazno","R":"Tacuarembó","S":"Montevideo"}
print(departamentos["A"])
print(departamentos["S"])