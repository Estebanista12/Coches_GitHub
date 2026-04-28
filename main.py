import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import datetime
import json
from databasemanager import DatabaseManager


class Coche:
    def __init__(self, marca, modelo, precio, CV, color, combustible, disponible=True, imagen=None):
        self.id = None
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.CV = CV
        self.color = color
        self.combustible = combustible
        self.disponible = disponible
        self.imagen = imagen

    def __str__(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        return f"{self.marca} {self.modelo} - {self.color} - {self.precio}€ - {self.CV}CV - {estado}"


class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Coches")
        self.ventana.geometry("950x600")
        self.ventana.configure(bg="#C8F7F0")

        # Base de datos
        self.db = DatabaseManager('coches.db')
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_app)

        # Estilo ttk
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # MENÚ
        self.barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_menu)

        menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Exportar JSON", command=self.exportar_json)  # <-- SOLO en menú
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.destroy)

        menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_acerca_de)

        # FRAMES
        frame_form = tk.Frame(self.ventana, pady=10, bg="#C8F7F0")
        frame_botones = tk.Frame(self.ventana, pady=10, bg="#C8F7F0")
        frame_form.pack()
        frame_botones.pack()

        # --- Frame de Búsqueda ---
        frame_busqueda = tk.Frame(self.ventana, bg="#C8F7F0")
        frame_busqueda.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(frame_busqueda, text="Buscar:", bg="#C8F7F0").pack(side=tk.LEFT, padx=5)
        self.campo_busqueda = tk.Entry(frame_busqueda)
        self.campo_busqueda.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(frame_busqueda, text="Buscar", command=self.buscar_coches).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_busqueda, text="Limpiar", command=self.limpiar_busqueda).pack(side=tk.LEFT, padx=5)

        # FRAME LISTA
        frame_lista = tk.Frame(self.ventana, pady=10, bg="#C8F7F0")
        frame_lista.pack()

        # FORMULARIO
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
        self.combustible = ttk.Combobox(frame_form, values=["Gasolina", "Diésel"], state="readonly")
        self.combustible.grid(row=2, column=3)
        self.combustible.current(0)

        tk.Label(frame_form, text="Fecha (AAAA-MM-DD):", bg="#C8F7F0").grid(row=3, column=0)
        self.fecha = tk.Entry(frame_form)
        self.fecha.grid(row=3, column=1)

        # BOTONES 
        tk.Button(frame_botones, text="Añadir Coche", bg="#71FF1F", command=self.añadir).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Modificar Coche", bg="#F7F436", command=self.modificar).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Eliminar Coche", bg="#F77036", command=self.eliminar).grid(row=0, column=2, padx=10)
        tk.Button(frame_botones, text="Cambiar Disponibilidad", bg="#36A2F7", command=self.cambiar_estado).grid(row=0, column=3, padx=10)

        # LISTA
        tk.Label(frame_lista, text="Listado de Coches:", bg="#C8F7F0").pack()
        self.lista = tk.Listbox(frame_lista, width=120, height=16)
        self.lista.pack()
        self.lista.bind("<<ListboxSelect>>", self.cargar_coche)

        self.actualizar_lista()

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
        fecha = self.fecha.get()
        if fecha:
            try:
                datetime.datetime.strptime(fecha, '%Y-%m-%d')
            except ValueError:
                messagebox.showwarning("Formato Incorrecto", "La fecha debe ser AAAA-MM-DD")
                return False
        return True

    # CRUD
    def actualizar_lista(self, termino_busqueda=None):
        self.lista.delete(0, tk.END)
        coches = self.db.obtener_coches(termino_busqueda)
        for c in coches:
            id_c, marca, modelo, precio, cv, color, combustible, fecha, disp = c
            estado = "Disponible" if disp else "No Disponible"
            texto = f"{id_c} - {marca} {modelo} | {precio}€ | {cv}CV | {color} | {combustible} | {fecha} | {estado}"
            self.lista.insert(tk.END, texto)

    def get_id(self):
        try:
            return int(self.lista.get(self.lista.curselection()).split(" - ")[0])
        except:
            return None

    def añadir(self):
        if not self.validar(): return
        if self.db.existe_coche(self.marca.get(), self.modelo.get()):
            messagebox.showwarning("Duplicado", "El coche ya existe en la base de datos")
            return
        self.db.añadir(self.marca.get(), self.modelo.get(), self.precio.get(), self.cv.get(),
                        self.color.get(), self.combustible.get(), self.fecha.get())
        self.actualizar_lista()
        self.limpiar()

    def modificar(self):
        id_c = self.get_id()
        if not id_c or not self.validar(): return
        self.db.modificar(self.marca.get(), self.modelo.get(), self.precio.get(), self.cv.get(),
                          self.color.get(), self.combustible.get(), self.fecha.get(), id_c)
        self.actualizar_lista()

    def eliminar(self):
        id_c = self.get_id()
        if id_c:
            self.db.eliminar(id_c)
            self.actualizar_lista()

    def cambiar_estado(self):
        id_c = self.get_id()
        if id_c:
            self.db.cambiar_estado(id_c)
            self.actualizar_lista()

    def cargar_coche(self, event):
        id_c = self.get_id()
        if id_c:
            coches = self.db.obtener_coches()
            datos = [c for c in coches if c[0] == id_c][0]
            _, marca, modelo, precio, cv, color, combustible, fecha, _ = datos
            self.marca.delete(0, tk.END)
            self.modelo.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.cv.delete(0, tk.END)
            self.color.delete(0, tk.END)
            self.fecha.delete(0, tk.END)
            self.marca.insert(0, marca)
            self.modelo.insert(0, modelo)
            self.precio.insert(0, precio)
            self.cv.insert(0, cv)
            self.color.insert(0, color)
            self.fecha.insert(0, fecha)
            self.combustible.set(combustible)

    def limpiar(self):
        self.marca.delete(0, tk.END)
        self.modelo.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.cv.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.fecha.delete(0, tk.END)

    # BÚSQUEDA
    def buscar_coches(self):
        self.actualizar_lista(self.campo_busqueda.get())

    def limpiar_busqueda(self):
        self.campo_busqueda.delete(0, tk.END)
        self.actualizar_lista()

    # EXPORTAR JSON (solo desde menú Archivo)
    def exportar_json(self):
        archivo = filedialog.asksaveasfilename(title="Guardar archivo JSON", defaultextension=".json",
                                               filetypes=[("JSON","*.json")])
        if not archivo: return
        try:
            coches = self.db.obtener_coches()
            lista = []
            for c in coches:
                _, marca, modelo, precio, cv, color, combustible, fecha, _ = c
                lista.append({'marca':marca,'modelo':modelo,'precio':precio,'cv':cv,'color':color,
                              'combustible':combustible,'fecha':fecha})
            with open(archivo,'w',encoding='utf-8') as f:
                json.dump(lista,f,indent=4)
            messagebox.showinfo("Exportación", "Datos exportados correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ACERCA DE
    def mostrar_acerca_de(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Acerca de")
        ventana.geometry("300x200")
        ventana.grab_set()
        ventana.transient(self.ventana)
        tk.Label(ventana, text="Gestor de Coches v1.0").pack(pady=20)
        tk.Label(ventana, text="Hecho por Noel Fran y Esteban").pack(pady=5)
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=20)

    # CERRAR APP
    def cerrar_app(self):
        self.db.close()
        self.ventana.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = App(ventana)
    ventana.mainloop()