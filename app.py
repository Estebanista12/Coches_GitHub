from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"nombre": "Mercedes AMG", "motivo": "ESTEBAN"},
        {"nombre": "AUDI", "motivo": "CABALLO"},
        {"nombre": "LAMBORGINI", "motivo": "PESCADO"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'items'
    return render_template("grupalindex.html", items=mis_favoritos)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)