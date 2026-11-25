'''
    objetivo es enseñarte a crear una ventana y colocar elementos utilizando el sistema de cuadrícula de Tkinter.
'''
import tkinter as tk                                       # Importa la biblioteca tkinter, que permite crear interfaces gráficas con Python.

ventana = tk.Tk()                                          # Crea la ventana principal de la aplicación.

tk.Label(ventana, text="Insertar").grid(row=0,column=0)    # Esta línea hace dos cosas: crea una etiqueta y la coloca dentro de la ventana.

tk.Label(ventana, text="Leer").grid(row=0,column=1)        # Hace exactamente lo mismo que la línea anterior, pero con dos diferencias: - El texto será "Leer". - Se coloca en la columna 1.

ventana.mainloop()                                         # Inicia el bucle principal de eventos de la aplicación.