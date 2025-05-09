#-------------------------------Entrada de Usuario Interactivo-------------------------------
#Aqui creamos 2 variables nombre y apellido pero con las variables ya predeterminadas
name = "Saul"
lastname = "Machicado"

print (name + " " + lastname)

#Aqui solisitamos los datos al usuario
name = input("Ingrese su nombre por favor: ")
print (name)
lastname = input("Ingrese su apellido por favor: ")
print (lastname)
print (name + " " + lastname)
age = int(input("Ingrese su edad porfavor: "))
print (age)
print (name + " " + lastname + " " + str(age))
print ("Hola mi nombre es " + name + "mi apellido es " + lastname + " " + str(age))