import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/debug")
def ver_coleccion():
    # 1. Conectamos con el archivo de la base de datos
    conexion = sqlite3.connect("coches.db")
    
    # 2. Configuramos la conexión para que devuelva diccionarios (más fácil para Jinja2)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    # 3. Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM LOGS;")
    
    # 4. Guardamos todos los resultados en una variable
    datos = cursor.fetchall()
    
    # 5. Cerramos la conexión
    conexion.close()
    
    # 6. Enviamos los datos reales a la plantilla
    return render_template("index.html", items=datos)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)

