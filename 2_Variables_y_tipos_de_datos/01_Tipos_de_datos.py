#---------------------TIPOS DE DATOS-------------------

# NÚMERICO
# Existen 3 clases de tipos de datos numericos:
# int (enteros) => 10, 200, 10000, -300
# float (punto flotante - decimales) => 2.1, -4.5, -500.5, 1000.33
# complex (complejos) => 2 + 1j, 1

print ("NUMERICOS")
number1 = 300
number2 = -300
number3 = 2.5
number4 = 2 + 1j
millon = 1e6
print ("Ver los valores de int") #Imprimimos los tipos de datos
print (number1)
print (number2)
print (number3)
print (number4)
print (millon)
print ("Imprimir el tipo de dato que tiene") #Se utiliza type
print (type(number1))
print (type(number2))
print (type(number3))
print (type(number4))
print (type(millon))

# STRINGS
# str (string) => "EDteam"
print (" ")
print ("STRINGS")

# Manejo de las " "
name = "EDteam dasssssssssssssssssssssssssssssdddddddddddddd dddddddddddddddddefesfav asdav fa" \
"dsadasdasdadeada"
# Manejo de """ """ para multineas
text = """ este es un texto de ejemplo para
saber como funciona la multilinea en las cadenas
de pyton""" #Se usa para documentacion tambien se conocen como docstrings
print ("Uso de String con 2 comillas")
print (" ")
print (name)
print (" ")
print ("Uso de Strings con 6 casillas para el doc strings")
print (" ")
print (text)

#Para mostrar en pantalla las comiilas dobles o comillas simples se realiza lo siguiente
print (" ")
print ('para mostrar las comillas dobles " " se crean comillas simples y dentro las comillas dobles')
print ("para mostrar las comillas simples ' ' se crean comillas dobles y dentro las comillas simples")

#Elegir una letra de una palabra
print (" ")
name = "Saul"
print (name[2])
# BOOL
# bool (booleano) => True, False

#En este caso veremos si la variable nombre tiene 
print (" ")
name = "Saul"
print (bool(name)) #Verificamos si tiene contenido
name1 = ""
print (bool(name1)) #Verificamos si tiene contenido

numberx = 1000
print (bool(name)) #Verificamos si tiene contenido
numeberz = 0
print (bool(name)) #Verificamos si tiene contenido

