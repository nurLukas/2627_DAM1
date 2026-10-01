import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

ARCHIVO = "agenda.csv"


class AgendaApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agenda de contactos")
        self.ventana.geometry("950x600")
        self.ventana.minsize(850, 520)

        self.contacto_seleccionado = None

        # -----------------------------
        # ESTILOS
        # -----------------------------
        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "TFrame",
            background="#f4f6f8"
        )

        estilo.configure(
            "Card.TFrame",
            background="white"
        )

        estilo.configure(
            "Titulo.TLabel",
            font=("Segoe UI", 22, "bold"),
            background="#f4f6f8",
            foreground="#202124"
        )

        estilo.configure(
            "Subtitulo.TLabel",
            font=("Segoe UI", 11),
            background="#f4f6f8",
            foreground="#6b7280"
        )

        estilo.configure(
            "CardTitle.TLabel",
            font=("Segoe UI", 14, "bold"),
            background="white",
            foreground="#202124"
        )

        estilo.configure(
            "Campo.TLabel",
            font=("Segoe UI", 10),
            background="white",
            foreground="#374151"
        )

        estilo.configure(
            "TEntry",
            padding=8,
            font=("Segoe UI", 10)
        )

        estilo.configure(
            "Guardar.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(15, 10)
        )

        estilo.configure(
            "Accion.TButton",
            font=("Segoe UI", 10),
            padding=(12, 8)
        )

        estilo.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=35,
            background="white",
            fieldbackground="white"
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )

        estilo.map(
            "Treeview",
            background=[("selected", "#dbeafe")],
            foreground=[("selected", "#1e3a8a")]
        )

        # -----------------------------
        # CONTENEDOR PRINCIPAL
        # -----------------------------
        principal = ttk.Frame(ventana, padding=25)
        principal.pack(fill="both", expand=True)

        principal.columnconfigure(1, weight=1)
        principal.rowconfigure(1, weight=1)

        # -----------------------------
        # ENCABEZADO
        # -----------------------------
        encabezado = ttk.Frame(principal)
        encabezado.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 20)
        )

        ttk.Label(
            encabezado,
            text="Agenda de contactos",
            style="Titulo.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            encabezado,
            text="Administra tus contactos de forma rápida y sencilla",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(3, 0))

        # -----------------------------
        # PANEL IZQUIERDO
        # -----------------------------
        formulario = ttk.Frame(
            principal,
            padding=20,
            style="Card.TFrame"
        )

        formulario.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(0, 20)
        )

        ttk.Label(
            formulario,
            text="Nuevo contacto",
            style="CardTitle.TLabel"
        ).pack(anchor="w", pady=(0, 20))

        # Nombre
        ttk.Label(
            formulario,
            text="Nombre",
            style="Campo.TLabel"
        ).pack(anchor="w")

        self.nombre = ttk.Entry(formulario, width=32)
        self.nombre.pack(fill="x", pady=(5, 15))

        # Apellidos
        ttk.Label(
            formulario,
            text="Apellidos",
            style="Campo.TLabel"
        ).pack(anchor="w")

        self.apellidos = ttk.Entry(formulario)
        self.apellidos.pack(fill="x", pady=(5, 15))

        # Email
        ttk.Label(
            formulario,
            text="Email",
            style="Campo.TLabel"
        ).pack(anchor="w")

        self.email = ttk.Entry(formulario)
        self.email.pack(fill="x", pady=(5, 20))

        self.boton_guardar = ttk.Button(
            formulario,
            text="Guardar contacto",
            style="Guardar.TButton",
            command=self.guardar
        )

        self.boton_guardar.pack(fill="x")

        ttk.Button(
            formulario,
            text="Limpiar formulario",
            style="Accion.TButton",
            command=self.limpiar_formulario
        ).pack(fill="x", pady=(10, 0))

        # -----------------------------
        # PANEL DERECHO
        # -----------------------------
        panel_contactos = ttk.Frame(
            principal,
            padding=20,
            style="Card.TFrame"
        )

        panel_contactos.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        panel_contactos.columnconfigure(0, weight=1)
        panel_contactos.rowconfigure(2, weight=1)

        # Título
        ttk.Label(
            panel_contactos,
            text="Mis contactos",
            style="CardTitle.TLabel"
        ).grid(row=0, column=0, sticky="w")

        # -----------------------------
        # BUSCADOR
        # -----------------------------
        zona_busqueda = ttk.Frame(
            panel_contactos,
            style="Card.TFrame"
        )

        zona_busqueda.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(15, 15)
        )

        zona_busqueda.columnconfigure(0, weight=1)

        self.busqueda = ttk.Entry(zona_busqueda)
        self.busqueda.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10)
        )

        self.busqueda.insert(0, "Buscar contacto...")

        self.busqueda.bind(
            "<FocusIn>",
            self.quitar_placeholder
        )

        self.busqueda.bind(
            "<KeyRelease>",
            self.buscar
        )

        ttk.Button(
            zona_busqueda,
            text="Actualizar",
            command=self.cargar_contactos
        ).grid(row=0, column=1)

        # -----------------------------
        # TABLA
        # -----------------------------
        tabla_frame = ttk.Frame(
            panel_contactos,
            style="Card.TFrame"
        )

        tabla_frame.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        tabla_frame.rowconfigure(0, weight=1)
        tabla_frame.columnconfigure(0, weight=1)

        columnas = ("nombre", "apellidos", "email")

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellidos", text="Apellidos")
        self.tabla.heading("email", text="Email")

        self.tabla.column("nombre", width=140)
        self.tabla.column("apellidos", width=180)
        self.tabla.column("email", width=240)

        self.tabla.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_contacto
        )

        # -----------------------------
        # BOTONES DE ACCIONES
        # -----------------------------
        acciones = ttk.Frame(
            panel_contactos,
            style="Card.TFrame"
        )

        acciones.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(15, 0)
        )

        ttk.Button(
            acciones,
            text="Editar",
            style="Accion.TButton",
            command=self.preparar_edicion
        ).pack(side="left")

        ttk.Button(
            acciones,
            text="Eliminar",
            style="Accion.TButton",
            command=self.eliminar
        ).pack(side="left", padx=(10, 0))

        # -----------------------------
        # BARRA INFERIOR
        # -----------------------------
        self.estado = ttk.Label(
            principal,
            text="",
            style="Subtitulo.TLabel"
        )

        self.estado.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(15, 0)
        )

        # Enter guarda
        self.email.bind(
            "<Return>",
            lambda event: self.guardar()
        )

        self.cargar_contactos()
        self.nombre.focus()


    # ==================================================
    # FUNCIONES
    # ==================================================

    def guardar(self):
        nombre = self.nombre.get().strip()
        apellidos = self.apellidos.get().strip()
        email = self.email.get().strip()

        # Validación
        if not nombre:
            messagebox.showwarning(
                "Datos incompletos",
                "Introduce el nombre del contacto."
            )
            self.nombre.focus()
            return

        if not apellidos:
            messagebox.showwarning(
                "Datos incompletos",
                "Introduce los apellidos."
            )
            self.apellidos.focus()
            return

        if not self.email_valido(email):
            messagebox.showwarning(
                "Email incorrecto",
                "Introduce una dirección de email válida."
            )
            self.email.focus()
            return

        # Si estamos editando
        if self.contacto_seleccionado is not None:
            self.guardar_edicion(
                nombre,
                apellidos,
                email
            )
            return

        # Comprobar duplicados
        if self.email_existe(email):
            messagebox.showwarning(
                "Contacto existente",
                "Ya existe un contacto con ese email."
            )
            return

        # Guardar usando módulo csv
        with open(
            ARCHIVO,
            "a",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow(
                [nombre, apellidos, email]
            )

        self.estado.config(
            text=f"✓ Contacto '{nombre}' guardado correctamente"
        )

        self.limpiar_formulario()
        self.cargar_contactos()


    def cargar_contactos(self):
        self.limpiar_tabla()

        if not os.path.exists(ARCHIVO):
            self.estado.config(
                text="Todavía no hay contactos guardados."
            )
            return

        contactos = self.obtener_contactos()

        for indice, contacto in enumerate(contactos):
            if len(contacto) >= 3:
                self.tabla.insert(
                    "",
                    "end",
                    iid=str(indice),
                    values=(
                        contacto[0],
                        contacto[1],
                        contacto[2]
                    )
                )

        cantidad = len(contactos)

        if cantidad == 1:
            texto = "1 contacto"
        else:
            texto = f"{cantidad} contactos"

        self.estado.config(
            text=f"{texto} guardados"
        )


    def obtener_contactos(self):
        contactos = []

        if not os.path.exists(ARCHIVO):
            return contactos

        with open(
            ARCHIVO,
            "r",
            newline="",
            encoding="utf-8"
        ) as archivo:

            lector = csv.reader(archivo)

            for fila in lector:
                if len(fila) >= 3:
                    contactos.append(fila)

        return contactos


    def seleccionar_contacto(self, event=None):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        self.contacto_seleccionado = {
            "indice": int(seleccion[0]),
            "datos": valores
        }


    def preparar_edicion(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo(
                "Editar contacto",
                "Selecciona primero un contacto."
            )
            return

        item = seleccion[0]

        valores = self.tabla.item(
            item,
            "values"
        )

        self.nombre.delete(0, tk.END)
        self.apellidos.delete(0, tk.END)
        self.email.delete(0, tk.END)

        self.nombre.insert(0, valores[0])
        self.apellidos.insert(0, valores[1])
        self.email.insert(0, valores[2])

        self.contacto_seleccionado = {
            "indice": int(item),
            "datos": valores
        }

        self.boton_guardar.config(
            text="Guardar cambios"
        )

        self.nombre.focus()


    def guardar_edicion(
        self,
        nombre,
        apellidos,
        email
    ):
        contactos = self.obtener_contactos()

        indice = self.contacto_seleccionado["indice"]

        if indice >= len(contactos):
            return

        # Evitar emails duplicados
        for i, contacto in enumerate(contactos):

            if i != indice:
                if contacto[2].lower() == email.lower():

                    messagebox.showwarning(
                        "Email duplicado",
                        "Otro contacto ya utiliza ese email."
                    )
                    return

        contactos[indice] = [
            nombre,
            apellidos,
            email
        ]

        self.guardar_todos(contactos)

        self.estado.config(
            text=f"✓ Contacto '{nombre}' actualizado"
        )

        self.limpiar_formulario()
        self.cargar_contactos()


    def eliminar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo(
                "Eliminar contacto",
                "Selecciona primero un contacto."
            )
            return

        item = seleccion[0]

        valores = self.tabla.item(
            item,
            "values"
        )

        confirmar = messagebox.askyesno(
            "Eliminar contacto",
            f"¿Seguro que quieres eliminar a "
            f"{valores[0]} {valores[1]}?"
        )

        if not confirmar:
            return

        contactos = self.obtener_contactos()

        indice = int(item)

        if indice < len(contactos):
            contactos.pop(indice)

        self.guardar_todos(contactos)

        self.limpiar_formulario()
        self.cargar_contactos()

        self.estado.config(
            text="✓ Contacto eliminado"
        )


    def guardar_todos(self, contactos):
        with open(
            ARCHIVO,
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)
            escritor.writerows(contactos)


    def buscar(self, event=None):
        texto = self.busqueda.get().strip().lower()

        if texto == "buscar contacto...":
            return

        self.limpiar_tabla()

        contactos = self.obtener_contactos()

        contador = 0

        for indice, contacto in enumerate(contactos):

            contenido = " ".join(contacto).lower()

            if texto in contenido:

                self.tabla.insert(
                    "",
                    "end",
                    iid=str(indice),
                    values=(
                        contacto[0],
                        contacto[1],
                        contacto[2]
                    )
                )

                contador += 1

        self.estado.config(
            text=f"{contador} resultados encontrados"
        )


    def quitar_placeholder(self, event=None):
        if self.busqueda.get() == "Buscar contacto...":
            self.busqueda.delete(0, tk.END)


    def limpiar_tabla(self):
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)


    def limpiar_formulario(self):
        self.nombre.delete(0, tk.END)
        self.apellidos.delete(0, tk.END)
        self.email.delete(0, tk.END)

        self.contacto_seleccionado = None

        self.boton_guardar.config(
            text="Guardar contacto"
        )

        self.nombre.focus()


    def email_valido(self, email):
        return (
            "@" in email
            and "." in email.split("@")[-1]
            and " " not in email
        )


    def email_existe(self, email):
        for contacto in self.obtener_contactos():

            if contacto[2].lower() == email.lower():
                return True

        return False


# -----------------------------
# INICIAR APLICACIÓN
# -----------------------------
if __name__ == "__main__":

    ventana = tk.Tk()

    app = AgendaApp(ventana)

    ventana.mainloop()