# Te muestro un mensaje
print("Te calculo el doble de la edad")

# Te pido que introduzcas un ato por la terminal
edad = input("Ihntroduce tu edad:") # el tipo de entrada siempre es string

# Ahora te confirmo que he recibido el dato
print("Ok, tu edad es de",edad,"años")

# como lo que recojo es un string, lo conveirto a un entero
edadentera = int(edad)

# Ahora sí, calculo el doble
doble = edadentera * 2

# Por ultimo,imprimo en pantalla
print("Ok, el doble de tu edad es",edad,"años")