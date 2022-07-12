from flask import render_template

from . import app
from .models import DBManager

RUTA = 'data/balance.db'

@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs = movimientos)

@app.route("/nuevo", methods=["GET","POST"])
def nuevo():
    return render_template("nuevo.html")

@app.route("/modificar/<int:id>",methods=["GET","POST"])
def actualizar(id):
    return f"Actualizar el movimiento con ID = {id}"


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    return render_template("borrar.html",resultado=True)