from flask import request, redirect, url_for, render_template
from programa import programa
from models.mintervenciones import nueva_intervencion, obtener_intervenciones
from models.casos import obtener_caso
from datetime import datetime

@programa.route("/casos/<int:num_caso>/intervenciones", methods=["POST"])
def guardar_intervencion(num_caso):
    documento = request.form["documento"]
    descripcion = request.form["descripcion"]
    compromiso = request.form["compromiso"]
    doc_pronal = session.get("usuario")
    nueva_intervencion(num_caso, documento, doc_pronal, descripcion, compromiso)
    return redirect(url_for("ver_caso", num_caso=num_caso))

@programa.route("/casos/<int:num_caso>/intervenciones", methods=["GET"])
def lista_intervenciones(num_caso):
    caso= obtener_caso(num_caso)
    intervenciones = obtener_intervenciones(num_caso)
    return render_template("detalle_caso.html", caso_id=num_caso, intervenciones=intervenciones)

@programa.route("/casos/<int:num_caso>/intervenciones/nueva/")
def nueva_intervencion_form(num_caso):
    caso = obtener_caso(num_caso)
    if caso["caso_estado"] == "cerrado":
        return render_template("listar_casos.html", caso=caso, intervenciones=obtener_intervenciones(num_caso), msg="El caso se encuentra cerrado. No puedes añadir intervenciones.")
    return render_template("intervenciones.html", caso=caso)