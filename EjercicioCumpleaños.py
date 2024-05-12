from os import system
system("cls") #system clear

from datetime import date

lista_alumnos = [['Josefina Alleges Gratadoux','josefinallegra@gmail.com','M1B',date(2005,8,9)],
['Alfonso Alvarez González','alfonsoalvarez1110@gmail.com','M1B',date(2004,10,11)],
['Félix Martín Álvarez Príncipe','felixmartinalvarez@gmail.com','M1B',date(2006,6,2)],
['Juan Ignacio Azpiroz Rodríguez','azpirozjuani@gmail.com','M1B',date(2005,5,31)],
['Gustavo Bachino Itté','gustibachino8@gmail.com','M1B',date(2006,3,30)],
['Maria Candelaria Bado Carrau','candebado1@gmail.com','M1B',date(2005,4,15)],
['Agustin Bica Der Gazarian','agus.bica.dergazarian@gmail.com','M1B',date(2000,7,26)],
['Agustín Bursztyn Wallerstein','agustinbursztyn005@gmail.com','M1B',date(2005,12,5)],
['Juan Manuel Cuitiño Ruiz','juancuitino37@gmail.com','M1B',date(2003,3,9)],
['Juan Pablo Curbelo Gallipoli','juanpablo.curbelo@gmail.com','M1B',date(2004,11,4)],
['Sergio Franco Dorrego Hernandez','sergiomas24@hotmail.com','M1B',date(1980,12,3)],
['Nicolás Franco Antelo','nfranco2005@gmail.com','M1B',date(2005,8,10)],
['Leandro Gayol Melognio','leitogayol@gmail.com','M1B',date(2006,3,14)],
['Josefina González Castro','sefigonzalezcastro@gmail.com','M1B',date(2003,7,20)],
['Raymond Guynot de Boismenu Miles','rgboismenu@gmail.com','M1B',date(2008,8,23)],
['Julieta Lemos Berriel','juli-lemosberriel@hotmail.com','M1B',date(2001,12,30)],
['Pedro Mendez Casariego','pedromendezcasariego@gmail.com','M1B',date(2005,6,22)],
['Felipe Mendez Rowland','mendezr.felipe@gmail.com','M1B',date(2004,6,16)],
['Daniela Andrea Muñoz Miranda','dmunozm@fen.uchile.cl','M1B',date(1997,2,3)],
['Juan Martin Navarro Etcheverry','juanmartinnavarro1670@gmail.com','M1B',date(2005,11,14)],
['Federico Nin Berti','fedenin34@gmail.com','M1B',date(2005,2,3)],
['Joaquin Revello Albernaz','joacoreve06@gmail.com','M1B',date(2006,3,8)],
['Matías Andrés Riani Blanco','matiandres04@gmail.com','M1B',date(2006,4,4)],
['Santiago Rivas Gallego','santiago.rivas0273@gmail.com','M1B',date(2000,3,27)],
['Pedro Manuel Saez Ortolani','saeped23@icloud.com','M1B',date(2005,7,7)],
['Juan Martín Sarries Olaso','Juanmartinsarries@gmail.com','M1B',date(2005,1,31)],
['Lucía Suárez Caballero','suarezlucia1313@gmail.com','M1B',date(2006,4,26)],
['Bruno Teicher Pallas','brunoteicher@gmail.com','M1B',date(2005,5,8)],
['Inés María Terra Rodriguez','inesmariaterra@gmail.com','M1B',date(2005,12,26)],
['Facundo Villarreal Bonilla','villarreal.facundo2005@gmail.com','M1B',date(2005,10,13)],
]

import random

for alumno in lista_alumnos:
    if alumno[3].month == 5 or alumno[3].month == 4:
        print(alumno[0],alumno[3])

sorteo = range.randint(0,len(lista_alumnos)-1)
print(lista_alumnos[sorteo])