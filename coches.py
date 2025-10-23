class coches:
    """
    Representa un coche dsiponible en nuestra lista del concesionario 
    """
    def __init__(self, marca, precio, CV, color, combustible, disponible=True):
        """
        Constructor para crear nuevas caracterisiticas del coche 
        """
        self.id = None
        self.marca = marca
        self.precio = precio
        self.CV = CV
        self.color = color
        self.combustible = combustible
        self.disponible = disponible
        
    def __str__(self, marca, precio, CV, color, combustible, disponible=True):
            return f"marca: {self.marca}, precio: {self.precio} , CV: {self.CV} , color: {self.color} , combustible: {self.combustible} , disponible: {self.disponible}"

# --- CÓDIGO DE PRUEBA ---

#1.Creamos dos objetos de la clase coche
Coche1 = coches("Mercedes", "25.000€", "250CV","rojo","gasolina","disponible")
Coche2 = coches ("Audi", "22.000€", "210CV","azul","diesel","disponible")


#2.Mostramos los datos del primer coche con print()
print("--- Mercedes AMG 38 ---") 
print(f"precio: {Coche1.precio}")
print(f"CV: {Coche1.CV}")
print(f"color: {Coche1.color}")
print(f"combustible: {Coche1.combustible}")
print(f"ID (Coche1): {Coche1.id}")


#3.Hacemos lo mismo con el siguiente coche 
print("--- Audi A4 s-line ---") 
print(f"precio: {Coche2.precio}")
print(f"CV: {Coche2.CV}")
print(f"color: {Coche2.color}")
print(f"combustible: {Coche2.combustible}")
print(f"ID (Coche2): {Coche2.id}")

import tkinter as tk

# 1. Ventana principal
class App:
    def __init__(self, ventana)
     ventana = tk.Tk()
        ventana.title("Liste De Coches")
        ventana.geometry("820x400")  # Ancho x Alto
        ventana.configure(bg="#B5E8E5")

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

def añadir():
    
    print("as pulsado añadir")

boton_add = tk.Button(ventana, text="Añadir Coche", command= añadir)
boton_add.configure(bg="#7DF736")


def modificar():
    
    print("as pulsado modificar")

boton_update = tk.Button(ventana, text="Modificar Coche", command=modificar)
boton_update.configure(bg="#F7F436")

def eliminar():
    
    print("as pulsado eliminar")

boton_delete = tk.Button(ventana, text="Eliminar Coche", command=eliminar)
boton_delete.configure(bg="#F77036")

# --- Lista de Tareas ---
etiqueta_lista = tk.Label(ventana, text="Coches disponibles:")
lista_tareas = tk.Listbox(ventana, width=60, height=10)


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
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = App(ventana_principal)
     ventana.mainloop()
