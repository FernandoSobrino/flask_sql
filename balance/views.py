from datetime import date
from flask import render_template, request


from . import app
from .forms import MovimientosForm
from .models import DBManager

RUTA = 'data/balance.db'


@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return render_template("nuevo.html")


@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    if request.method == "GET":
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimientoPorId(id)

        movimiento["fecha"] = date.fromisoformat(movimiento["fecha"])

        formulario = MovimientosForm(data=movimiento)
        return render_template("form_movimiento.html", form=formulario, id=id)

    elif request.method == "POST":
        form = MovimientosForm(data=request.form)
        if form.validate():
            return "Guardo los datos"
        return "El formulario tiene errores"
        


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db = DBManager(RUTA)
    #esta_borrado = db.borrar(id)
    consulta = "DELETE FROM movimientos WHERE id=?"
    params = (id,)
    esta_borrado = db.consultaConParametros(consulta,params)
    return render_template("borrar.html", resultado=esta_borrado)
