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
            id_c, marca, modelo, precio, cv, color, combustible, fecha, disponible = fila
            items.append({
                'id': id_c,
                'nombre': f"{marca} {modelo}",
                'marca': marca,
                'modelo': modelo,
                'precio': precio,
                'cv': cv,
                'color': color,
                'combustible': combustible,
                'fecha': fecha,
                'disponible': bool(disponible),
                
            })
        return render_template('grupalindex.html', items=items)
    finally:
        db.close()


@app.route('/detalle/<int:id_item>')
def ver_detalle(id_item):
    """Muestra el detalle de un coche identificado por id_item."""
    db = DatabaseManager('coches.db')
    try:
        fila = db.obtener_coche_por_id(id_item)
        if not fila:
            # Renderizar una página simple de no encontrado
            return render_template('detalle.html', item=None, id_item=id_item), 404

        id_c, marca, modelo, precio, cv, color, combustible, fecha, disponible = fila
        item = {
            'id': id_c,
            'marca': marca,
            'modelo': modelo,
            'precio': precio,
            'cv': cv,
            'color': color,
            'combustible': combustible,
            'fecha': fecha,
            'disponible': bool(disponible),
        }
        return render_template('detalle.html', item=item)
    finally:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)