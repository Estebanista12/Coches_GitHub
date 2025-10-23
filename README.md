# Prueba_GitHub
Este es un repositirorio de prueba para ver como funicona github



import tkinter as tk

# 1. Ventana principal
ventana = tk.Tk()
ventana.title("Liste De Coches")
ventana.geometry("820x400")  # Ancho x Alto

# Aquí irán los pasos 2 y 3...



# ... (código del paso 1)

# 2. Creación de Widgets
# --- Formulario de Entrada ---
etiqueta_desc = tk.Label(ventana, text="Modelo:")
campo_desc = tk.Entry(ventana, width=40)

etiqueta_fecha = tk.Label(ventana, text="Precio:")
campo_fecha = tk.Entry(ventana)

etiqueta_fecha_1 = tk.Label(ventana, text="Color:")
campo_fecha_1 = tk.Entry(ventana)

etiqueta_prio = tk.Label(ventana, text="CV:")
campo_prio = tk.Entry(ventana)

etiqueta_marca = tk.Label(ventana, text="Marca:")
campo_Marca = tk.Entry(ventana)

# --- Botones ---
boton_add = tk.Button(ventana, text="Añadir Tarea")
boton_update = tk.Button(ventana, text="Modificar Tarea")
boton_delete = tk.Button(ventana, text="Eliminar Tarea")

# --- Lista de Tareas ---
etiqueta_lista = tk.Label(ventana, text="Tareas Pendientes:")
lista_tareas = tk.Listbox(ventana, width=60, height=10)

# ... (código del paso 4)

#Paso 3: Posicionar los Widgets con grid()

#Este es el paso clave. Usamos grid() para colocar cada widget en su fila y columna, usando las opciones que aprendimos para que quede ordenado.


# ... (después de crear los widgets)

# 3. Posicionamiento con Grid
# --- Formulario de Entrada ---
etiqueta_desc.grid(row=0, column=0, padx=10, pady=5, sticky="w")
campo_desc.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="ew")

etiqueta_fecha.grid(row=1, column=0, padx=10, pady=5, sticky="w")
campo_fecha.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

etiqueta_fecha_1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
campo_fecha_1.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

etiqueta_prio.grid(row=1, column=2, padx=10, pady=5, sticky="w")
campo_prio.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

etiqueta_marca.grid(row=2, column=2, padx=10, pady=5, sticky="w")
campo_Marca.grid(row=2, column=3, padx=10, pady=5, sticky="ew")

# --- Botones ---
boton_add.grid(row=3, column=1, padx=10, pady=10)
boton_update.grid(row=3, column=2, padx=10, pady=10)
boton_delete.grid(row=3, column=3, padx=10, pady=10)

# --- Lista de Tareas ---
etiqueta_lista.grid(row=4, column=0, padx=10, pady=5, sticky="w")
lista_tareas.grid(row=5, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

# 4. Iniciar el bucle de la aplicación
ventana.mainloop()


