#------------------Listas------------------

# Array o Lista se declara de la siguiente manera

#Creamos una lista de Strings
frutas = ["manzana", "pera", "uva"] #creamos y declaramos nuestra variable
print (type(frutas)) # imprimer que tipo de dato es
print (frutas) #Imprime el contenido de la lista
print (" ")

#Creamos una lista de numeros
numeros = [1, 2, 3, 4, 50] 
print (type(numeros))
print (numeros)
print (" ")

#Creamos una lista de DISTINTOS tipos de datos en una lista
varios = [True, "Manzan", 20, 33.33, -300]
print (type(varios))
print (varios)
print (" ")

#Se puede acceder a cualquier item de una lista usando un indice de la siguiente manera utilizaremos la lista de frutas
print (frutas[0])
print (frutas[1])
print (frutas[2])
print (" ")

#Se puede acceder de otra manera que es la siguiente manera
print (frutas[-1]) #comenzaria el contador de derecha a izquierda por usar el -1
print (" ")

#Seleccionar de un rango de items de una lista
frutas = ["manzana", "pera", "uva", "melocoton"]
frutas2 = frutas[1:3]  #Establecemos el rango el 1 seria la pera y hasta el 3 seria la uva porque toma hasta un numero antes del numero establecido
print (frutas2)
print (" ")

#Sumas dentro de los array
numeros = [1, 2, 3]
print (frutas + numeros)

#Guardamos la suma de 2 listas en otra lista
new_list = frutas + numeros
print (new_list)
print (" ")

#Realizar un cambio en una lista
frutas = ["manzana", "pa", "uva", "melocoton"] #Suponiendo que el item 1 esta mal escrito "pa" en lugar de "pera" el cambio se realiza de la siguiente manera
print (frutas) #Imprimimos para poder ver el error
frutas[1] = "pera" #realizamos el cambio
print (frutas) #Imprimimos el valor de frutas con el cambio 
print (" ")

#Pealizar una modificacion de un rango
frutas = ["manzana", "pa", "uva", "melocoton", "banana"]
frutas[1:4] = ["Uno", "Dos", "Tres"]
print (frutas) #Imprime la nueva lista con los cambios
print (" ")

numeros = frutas[1:4]
print (numeros) #mostrara solo los cambios de la lista Uno, Dos, Tres
print (frutas) #Imprime la lista con los cambios

#Añadir valores a una lista
frutas = ["manzana", "pera", "uva", "melocoton", "sandia"]
frutas.append("coco")
print (frutas)
print (" ")

#Para saber cuantos items tiene nuestra lista
print(len(frutas)) #nos indica la longitud de un tipo de dato especifico

#Hacer una suma de 2 listas
new_list = [frutas, numeros]
print (new_list) #imprimimos la lista que contiene 2 listas
print (new_list[0]) #imprimimos lalista que contiene la primera lisat ingresada
print (new_list[1]) #imprimimos lalista que contiene la segunda lisat ingresada

#Hacer a un item de una lista dentro de otra lista
frutas = ["manzana", "pera", "uva", "melocoton", "sandia", "coco"]
numeros = [1, 2, 3]
print(new_list[0][3]) #Selecciona el melocoton
print(new_list[1][2]) #Seleeciona el Tres
print (" ")

#para eliminar un item de una lista se hace de la siguiente manera
frutas = ["manzana", "pera", "uva", "melocoton", "sandia"]
del frutas[1]
print (frutas)
