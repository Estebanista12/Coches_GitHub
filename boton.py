import tkinter as tk

# --- 1. Definimos la función que se ejecutará ---
def saludar():
    """Esta función se llamará al hacer clic en el botón."""
    print("¡Hola, has hecho clic en el botón!")

# Creamos la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Evento")

# --- 2. Asociamos la función al botón con 'command' ---
# Nota: Pasamos el nombre de la función SIN paréntesis.
boton_saludo = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton_saludo.pack(padx=20, pady=20) # Usamos pack() para un ejemplo simple

ventana.mainloop()

