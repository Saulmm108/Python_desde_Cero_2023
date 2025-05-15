#--------------------Sets---------------
# Son parecidos a los diccionarios con la diferencia de que no tiene claves para poder crear claves dentro de si

names = {"Saul", "Alenka", "Doe", "Doe", True, 300, 1, 0, False} #Al colocar 2 Dos al imprimirlo solo mostrara 1 Doe no se pueden colocar valores repetidos tampoco el 1 y el False porque parentesco con true y false
print (type(names))
print (names)
print (" ")

frutas = set(("Manzana", "Pera", "Melocoton"))
print (type(frutas))
print (frutas)

texto = "Este es un ejemplo de texto para mostrar una caracteristica de los Set"
print (texto)
print(set(texto))