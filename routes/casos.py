from flask import request, render_template, redirect, url_for, session
from programa import programa
from datetime import datetime
import mysql.connector
from models.casos import nuevo_caso, obtener_caso, cerrar_caso, existe_estudiante, todos_casos_listados, obtener_caso_doc


@programa.route("/casos/nuevo", methods=["GET"])
def mostrar_casos():
    return render_template("/casos.html")

@programa.route("/casos", methods=["POST"])
def guardar_caso():
    documento = request.form["documento"]
    caso_tipo = request.form["caso_tipo"]
    caso_descripcion = request.form["caso_descripcion"]
    caso_fecha_apertura = datetime.now().strftime("%Y-%m-%d")
    doc_pronal = request.form["doc_pronal"]

    if not existe_estudiante(documento):
        return render_template("casos.html", msg="Verifica que el documento de identidad del estudiante sea el correcto. Inténtalo de nuevo.", document=documento, caso_tipo=caso_tipo, caso_descripcion=caso_descripcion)

    nuevo_caso(documento, caso_tipo, caso_descripcion, caso_fecha_apertura, doc_pronal)
    return redirect(url_for("mostrar_casos", msg="Caso registrado con éxito."))

#esta ruta le pertenece a listar casos html, con esta listamos los casos
@programa.route("/casos", methods=["GET"])
def lista_casos():
    documento = request.args.get("documento")
    if documento:
        casos = obtener_caso_doc(documento)
    else:
        casos = todos_casos_listados()
    
    return render_template("listar_casos.html", casos=casos)

#con esta ruta manipulamos la visualizacion de los detalles del caso, redirige a itervenciones.html
@programa.route("/casos/<int:num_caso>", methods=["GET"])
def ver_caso(num_caso):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM casos WHERE num_caso = %s", (num_caso,))
    caso=cursor.fetchone()

    cursor.execute("SELECT * FROM intervenciones WHERE num_caso = %s ORDER BY fecha DESC", (num_caso,) )
    intervenciones=cursor.fetchall()

    cursor.close()
    conexion.close()
    return render_template("detalle_caso.html", caso=caso, intervenciones=intervenciones)

#esta ruta cierra el caso
@programa.route("/casos/<int:num_caso>/cerrar", methods=["POST"])
def r_cerrar_caso(num_caso):
    if session["rol"] != "administrador":
        return render_template("casos.html", msg ="No tienes permisos para cerrar casos.")
    fecha_cierre = datetime.now().strftime("%Y-%m-%d")
    cerrar_caso(num_caso, fecha_cierre)
    return redirect(url_for("listar_casos"))