import tkinter as tk

def pulsaBoton():
    print("Hola que tal, como estas")
    resultado.config(text="prueba superada") # Del resultado, configuro que su texto es X o lo que yo quiera ej: "prueba superada"

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto
etiqueta.pack(padx=20,pady=20)

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)
boton.pack(padx=20,pady=20)

resultado = tk.Label(raiz, text="x", font=("Arial", 24))
resultado.pack(padx=20,pady=20)

raiz.mainloop() # no te salgas del bucle