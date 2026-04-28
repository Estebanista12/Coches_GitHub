import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()
        self.verificar_columnas()

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
            disponible INTEGER DEFAULT 1,
            imagen TEXT
        )
        """)
        self.conexion.commit()

    def verificar_columnas(self):
        self.cursor.execute("PRAGMA table_info(Coche)")
        columnas = [col[1] for col in self.cursor.fetchall()]
        if 'fecha' not in columnas:
            self.cursor.execute("ALTER TABLE Coche ADD COLUMN fecha TEXT")
            self.conexion.commit()

    def añadir(self, marca, modelo, precio, cv, color, combustible, fecha):
        self.cursor.execute("""
        INSERT INTO Coche (marca, modelo, precio, cv, color, combustible, fecha)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (marca, modelo, precio, cv, color, combustible, fecha))
        self.conexion.commit()

    def obtener_coches(self, termino_busqueda=None):
        if termino_busqueda:
            termino = f"%{termino_busqueda}%"
            self.cursor.execute("""
            SELECT id, marca, modelo, precio, cv, color, combustible, fecha, disponible
            FROM Coche
            WHERE marca LIKE ? OR modelo LIKE ? OR color LIKE ?
            """, (termino, termino, termino))
        else:
            self.cursor.execute("""
            SELECT id, marca, modelo, precio, cv, color, combustible, fecha, disponible
            FROM Coche
            """)
        return self.cursor.fetchall()

    def modificar(self, marca, modelo, precio, cv, color, combustible, fecha, id_c):
        self.cursor.execute("""
        UPDATE Coche 
        SET marca=?, modelo=?, precio=?, cv=?, color=?, combustible=?, fecha=?
        WHERE id=?
        """, (marca, modelo, precio, cv, color, combustible, fecha, id_c))
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

    def existe_coche(self, marca, modelo):
        self.cursor.execute("SELECT id FROM Coche WHERE marca=? AND modelo=?", (marca, modelo))
        return self.cursor.fetchone() is not None

    def close(self):
        self.conexion.commit()
        self.conexion.close()