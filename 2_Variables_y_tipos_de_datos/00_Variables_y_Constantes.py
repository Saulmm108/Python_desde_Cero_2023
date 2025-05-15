#-------------------------Variables y Constantes----------------------------

# Variables  
# Las variables pueden cambiar en cualquier momento o instante del programa
name = "Saul"
print (name)

number1 = 300
number2 = number1

#Imprimimos las variables
print (number1)
print (number2)

#id nos permite verificar que tipo de identificador tiene y ver que espacio ocupa en la memoria y nos muestra el mismo espacio de memoria
#en este caso porque number2 = number1
print (id(number1))
print (id(number2))

# Constantes
# Las constantes no cambian en ningun momento del codigo

PI = 3.1416
SECONDS_HOUR = 3600
print (PI)
#Realizamos un cambio a PI
PI = 25287
print (PI)