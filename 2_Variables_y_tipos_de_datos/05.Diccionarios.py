#------------------DICCIONARIOS--------------------
#Son estructuras que se crean para poder guardar o almacenar algunas propiedades dentro de ellas
#Estructura de un diccionario es Clave y un Valor
usuario = {
    #Dentro de las {} se establecen las propiedades que tienen un diccionario
    "nombre": "Jhon",
    "apellido": "Doe",
    "edad": 36,
    "colores": ["Red", "Verde", "Azul"],
    #Creamos un diccionario dentro de otro diccionario
    "dictionary": {
        "key": "value1",
        "key2": "value2",
    }
}

print(type(usuario)) #Imprime el tipo de dato
print(usuario) #Imprime el usuario
print ("")
print(usuario["nombre"]) #Imprime el nombre del usuario
print(usuario["colores"]) #Imprime el color del usuario
print ("")
print (len(usuario)) #Vemos la longitud de nuestro dicionario
print (len(usuario["colores"])) #Vemos la longitud de los colores de usuario de nuestro diccionario

#OTRA FORMA DE CREAR DICCIONARIOS
jugador = dict(equipo = "X", salario = 30000, equipos = ["1", "2", "3"])
print(type(jugador)) #Imprime el tipo de dato
print(jugador) #Imprime el jugador