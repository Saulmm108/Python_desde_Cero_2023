#----------CONVERSIONES DE DATOS-------------------

#Conversion de tipos de datos

#Convertir de enteros a cadenas
number = 1000
number_float =12.25 
number_string = str(number) #utilizar str() convierte un dato numerico a string

print (type(number)) #imprime el dato entero
print (type(number_string)) #imprime un string
print (type(str(number))) #de este modo tambien se puede convertir un dato de tipo entero a un string

#cadena
print (" ")
var = "5000" #es una cadena por utilizar ""
print (type(var))
#print (number + var) da error por querer sumar un entero con una 
print (number + int(var)) # de este modo esta correcto convertimos la cadena var a entero utilizando int()

print (" ")
print (number) #Imprimira 1000
print (float(number)) #Imprimira 1000.0
print (int(number_float))

int_number =int (number_float)
print (int_number)