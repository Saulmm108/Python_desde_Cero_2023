# -------------------OPERADODES MATEMATICOS LOGIVOS Y RELACIONALES-------------------------
#Strings
#Imprimimos nuestro nombre
name = "Saúl"
print (name)

#Concadenamos nuestro apellido
print (name + "Machicado")

#Poner nuestro apellido dentro de la variable es un acumulador (+=)
name += " Machicado"
print (name)

#Numeros
#Imprimimos un numero
numer1 = 30
print (numer1)

#Concatenamos un numero mas
print (numer1+3)

#Utilizando el acumulador
numer1 +=3
print (numer1)

#Utilizamos el reductor
numer1 -=3
print (numer1)

#Utilizamos la division
numer1 = 15
print (numer1 / 3)

#Para resvir un valor entero al dividir
print (numer1 // 3)

#Para resivir el residuo
print (numer1 % 4)

#Para multiplicar
print (numer1 * 4)

#Variable tipo String y variable matemática
print (name * 2) #Esta es la unica manerda de conbinar un String con una variable

#Potencias
numer1 = 5
print (numer1 ** 2)

#"cls" es un comando de Windows que limpia la pantalla de la consola (Command Prompt).
#import os
#os.system("cls")

#Comparativos
print (2 < 5)
print (2 <= 2)
print (5 >= 2)
print (5 >= 10)
print ("Saul" == "Saul")
print ( 5 == 5)
print (5 != 5) #ara identificar si 2 variables son distintas
print (5 != 6)

#Validar &&
numer1 = 2
numer2 = 2
status = True
print (numer1 == numer2)

#Uso del and y or
#and
print (numer1 == numer2 and status == True)
#or
print (numer1 == numer2 or status == True)