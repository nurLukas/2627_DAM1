print("Programa agenda v0.1 Lucas Andrés Griego")
while True:
	nombre = input("Introduce un nuevo nombre en tu agenda: ")	
	archivo = open("agenda.txt",'a')
	archivo.write(nombre+"\n")
	archivo.close()