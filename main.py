import tkinter as tk
from tkinter import messagebox
import sqlite3

class Coche:
    """
    Representa un coche disponible en el concesionario.
    """
    def __init__(self, marca, modelo, precio, CV, color, combustible, disponible=True):
        self.id = None
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.CV = CV
        self.color = color
        self.combustible = combustible
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        return f"{self.marca} {self.modelo} - {self.color} - {self.precio}€ - {self.CV}CV - {estado}"


class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Coches")
        self.ventana.geometry("850x500")
        self.ventana.configure(bg="#C8F7F0")

        # Base de datos
        self.conexion = sqlite3.connect("coches.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

        # Frames
        frame_form = tk.Frame(self.ventana, pady=10, bg="#C8F7F0")
        frame_botones = tk.Frame(self.ventana, pady=10, bg="#C8F7F0")
        frame_lista = tk.Frame(self.ventana, pady=10, bg="#C8F7F0")

        frame_form.pack()
        frame_botones.pack()
        frame_lista.pack()

        # Formulario
        tk.Label(frame_form, text="Marca:", bg="#C8F7F0").grid(row=0, column=0)
        self.marca = tk.Entry(frame_form)
        self.marca.grid(row=0, column=1)

        tk.Label(frame_form, text="Modelo:", bg="#C8F7F0").grid(row=1, column=0)
        self.modelo = tk.Entry(frame_form)
        self.modelo.grid(row=1, column=1)

        tk.Label(frame_form, text="Precio (€):", bg="#C8F7F0").grid(row=0, column=2)
        self.precio = tk.Entry(frame_form)
        self.precio.grid(row=0, column=3)

        tk.Label(frame_form, text="CV:", bg="#C8F7F0").grid(row=1, column=2)
        self.cv = tk.Entry(frame_form)
        self.cv.grid(row=1, column=3)

        tk.Label(frame_form, text="Color:", bg="#C8F7F0").grid(row=2, column=0)
        self.color = tk.Entry(frame_form)
        self.color.grid(row=2, column=1)

        tk.Label(frame_form, text="Combustible:", bg="#C8F7F0").grid(row=2, column=2)
        self.combustible = tk.Entry(frame_form)
        self.combustible.grid(row=2, column=3)

        # Botones
        tk.Button(frame_botones, text="Añadir Coche", bg="#71FF1F",
                  command=self.añadir).grid(row=0, column=0, padx=10)

        tk.Button(frame_botones, text="Modificar Coche", bg="#F7F436",
                  command=self.modificar).grid(row=0, column=1, padx=10)

        tk.Button(frame_botones, text="Eliminar Coche", bg="#F77036",
                  command=self.eliminar).grid(row=0, column=2, padx=10)

        tk.Button(frame_botones, text="Cambiar Disponibilidad", bg="#36A2F7",
                  command=self.cambiar_estado).grid(row=0, column=3, padx=10)

        # Lista
        tk.Label(frame_lista, text="Listado de Coches:", bg="#C8F7F0").pack()
        self.lista = tk.Listbox(frame_lista, width=100, height=14)
        self.lista.pack()
        self.lista.bind("<<ListboxSelect>>", self.cargar_coche)

        self.actualizar_lista()

    # Crear tabla SQL
    def crear_tabla(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Coche (
            id INTEGER PRIMARY KEY,
            marca TEXT,
            modelo TEXT,
            precio TEXT,
            cv TEXT,
            color TEXT,
            combustible TEXT,
            disponible INTEGER DEFAULT 1
        )
        """)
        self.conexion.commit()

    # VALIDACIÓN 
    def validar(self):
        if not all([self.marca.get(), self.modelo.get(), self.precio.get(), self.cv.get()]):
            messagebox.showerror("Error", "Todos los campos obligatorios deben estar completos.")
            return False

        if not self.precio.get().isdigit():
            messagebox.showerror("Error", "El precio debe ser un número.")
            return False

        if not self.cv.get().isdigit():
            messagebox.showerror("Error", "Los CV deben ser número entero.")
            return False

        return True

    # Actualizar lista
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM Coche")
        coches = self.cursor.fetchall()

        for c in coches:
            id_c, marca, modelo, precio, cv, color, combustible, disp = c
            estado = " Disponible" if disp else " No Disponible"
            texto = f"{id_c} - {marca} {modelo} | {precio}€ | {cv}CV | {color} | {combustible} | {estado}"
            self.lista.insert(tk.END, texto)

    # Añadir coche
    def añadir(self):
        if not self.validar():
            return

        datos = (
            self.marca.get(), self.modelo.get(), self.precio.get(),
            self.cv.get(), self.color.get(), self.combustible.get()
        )

        self.cursor.execute("""
        INSERT INTO Coche (marca, modelo, precio, cv, color, combustible)
        VALUES (?, ?, ?, ?, ?, ?)
        """, datos)

        self.conexion.commit()
        self.actualizar_lista()
        messagebox.showinfo("Éxito", "Coche añadido correctamente.") 
        self.limpiar()

    # Obtener ID
    def get_id(self):
        try:
            return int(self.lista.get(self.lista.curselection()).split(" - ")[0])
        except:
            return None

    # Cargar coche en formulario
    def cargar_coche(self, event):
        id_c = self.get_id()
        if id_c:
            self.cursor.execute("SELECT * FROM Coche WHERE id=?", (id_c,))
            datos = self.cursor.fetchone()

            _, marca, modelo, precio, cv, color, combustible, _ = datos

            self.marca.delete(0, tk.END)
            self.modelo.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.cv.delete(0, tk.END)
            self.color.delete(0, tk.END)
            self.combustible.delete(0, tk.END)

            self.marca.insert(0, marca)
            self.modelo.insert(0, modelo)
            self.precio.insert(0, precio)
            self.cv.insert(0, cv)
            self.color.insert(0, color)
            self.combustible.insert(0, combustible)

    # Modificar coche
    def modificar(self):
        id_c = self.get_id()
        if not id_c:
            messagebox.showerror("Error", "Selecciona un coche.")
            return

        if not self.validar():
            return

        datos = (
            self.marca.get(), self.modelo.get(), self.precio.get(),
            self.cv.get(), self.color.get(), self.combustible.get(), id_c
        )

        self.cursor.execute("""
        UPDATE Coche SET marca=?, modelo=?, precio=?, cv=?, color=?, combustible=?
        WHERE id=?
        """, datos)

        self.conexion.commit()
        self.actualizar_lista()
        messagebox.showinfo("Éxito", "Coche modificado correctamente.")

    # Eliminar coche
    def eliminar(self):
        id_c = self.get_id()
        if not id_c:
            messagebox.showerror("Error", "Selecciona un coche para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar este coche?"):
            self.cursor.execute("DELETE FROM Coche WHERE id=?", (id_c,))
            self.conexion.commit()
            self.actualizar_lista()
            self.limpiar()
            messagebox.showinfo("Éxito", "Coche eliminado correctamente.")

    # Cambiar disponibilidad
    def cambiar_estado(self):
        id_c = self.get_id()
        if not id_c:
            messagebox.showerror("Error", "Selecciona un coche.")
            return

        self.cursor.execute("SELECT disponible FROM Coche WHERE id=?", (id_c,))
        estado = self.cursor.fetchone()[0]
        nuevo = 0 if estado == 1 else 1

        self.cursor.execute("UPDATE Coche SET disponible=? WHERE id=?", (nuevo, id_c))
        self.conexion.commit()
        self.actualizar_lista()
        messagebox.showinfo("OK", "Disponibilidad actualizada.") 

    # Limpiar formulario
    def limpiar(self):
        self.marca.delete(0, tk.END)
        self.modelo.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.cv.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.combustible.delete(0, tk.END)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = App(ventana)
    ventana.mainloop()
