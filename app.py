from flask import Flask, render_template
from databasemanager import DatabaseManager

app = Flask(__name__)


@app.route('/coleccion')
def ver_coleccion():
    """Lee coches desde la base de datos SQLite y los pasa a la plantilla.

    Abre la conexión con DatabaseManager, obtiene las filas y cierra la conexión.
    """
    db = DatabaseManager('coches.db')
    try:
        filas = db.obtener_coches()
        items = []
        for fila in filas:
            # filas: id, marca, modelo, precio, cv, color, combustible, imagen, fecha, disponible
            id_c, marca, modelo, precio, cv, color, combustible, imagen, fecha, disponible = fila
            items.append({
                'id': id_c,
                'nombre': f"{marca} {modelo}",
                'marca': marca,
                'modelo': modelo,
                'precio': precio,
                'cv': cv,
                'color': color,
                'combustible': combustible,
                'imagen': imagen,
                'fecha': fecha,
                'disponible': bool(disponible),
            })
        return render_template('grupalindex.html', items=items)
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)