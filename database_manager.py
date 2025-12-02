import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conexion = sqlite3.connect("db_path")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

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

    def añadir(self, marca, modelo, precio, cv, color, combustible):
        self.cursor.execute ("INSERT INTO COCHES (marca, modelo,precio,cv,color,combustible) VALUES (?,?,?)",(marca, modelo, precio, cv, color, combustible, ))
            

        self.conexion.commit()

    def actualizar_lista(self):
        self.cursor.execute("SELECT id , marca,modelo,precio,cv,color,combustible")
        coches = self.cursor.fetchall()
        return coches


    def modificar(self, marca, modelo, precio, cv, color, combustible, id_c):
             self.cursor.execute("UPDATE Coche SET marca=?, modelo=?, precio=?, cv=?, color=?, combustible=? WHERE id=?",(marca, modelo, precio, cv, color, combustible, id_c)
        )
             self.conexion.commit()

    def eliminar(self, id_c): 
        
            self.cursor.execute("DELETE FROM Coche WHERE id=?", (id_c,))

            self.conexion.commit()
            
    def cambiar_estado(self, id_c):
        

        self.cursor.execute("SELECT disponible FROM Coche WHERE id=?", (id_c,))
        estado = self.cursor.fetchone()[0]
        nuevo = 0 if estado == 1 else 1

        self.cursor.execute("UPDATE Coche SET disponible=? WHERE id=?", (nuevo, id_c))
        self.conexion.commit()
    

  



