from flask import request, render_template, redirect, url_for, session
from programa import programa
from models.casos import nuevo_caso, obtener_caso, caso_id, cerrar_caso


@programa.route("/casos/nuevo", methods=["GET"])
def mostrar_casos():
    return render_template("/casos.html")

@programa.route("/casos", methods=["POST"])
def guardar_caso():
    documento = request.form["documento"]
    caso_tipo = request.form["caso_tipo"]
    caso_descripcion = request.form["caso_descripcion"]
    caso_fecha_apertura = request.form["caso_fecha_apertura"]
    doc_pronal = request.form["doc_pronal"]

    nuevo_caso(documento, caso_tipo, caso_descripcion, caso_fecha_apertura, doc_pronal)
    return redirect(url_for("lista_casos"))

@programa.route("/casos", methods=["GET"])
def lista_casos():
    documento = request.args.get("documento")
    if documento:
        casos = obtener_caso_por_documento(documento)
    else:
        casos = obtener_caso()
    
    return render_template("listar_casos.html", casos=casos)

@programa.route("/casos/<int:num_caso>/cerrar", methods=["POST"])
def ver_caso(num_caso):
    caso=caso_id(num_caso)
    return render_template("detalle_caso.html", caso=caso)

@programa.route("/casos", methods=["POST"])
def r_cerrar_caso(num_caso):
    if session["rol"] != "administrador":
        return render_template("casos.html", msg ="No tienes permisos para cerrar casos.")
    fecha_cierre = request.form["caso_fecha_cierre"]
    cerrar_caso(num_caso, fecha_cierre)
    return redirect(url_for("listar_casos"))