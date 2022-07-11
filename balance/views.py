from . import app


@app.route("/")
def inicio():
    return "Página de inicio"

@app.route("/nuevo", methods=["GET","POST"])
def nuevo():
    return "Crear movimiento"

@app.route("/modificar",methods=["GET","POST"])
def actualizar():
    return "Actualizar movimiento"

@app.route("/borrar",methods=["GET","POST"])
def eliminar():
    return "Eliminar movimiento"