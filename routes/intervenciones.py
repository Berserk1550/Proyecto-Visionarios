from flask import request, redirect, url_for, render_template
from programa import programa
from models.mintervenciones import nueva_intervencion, obtener_intervenciones

@programa.route("/intervenciones", methods=["POST"])
def guardar_intervencion():
    num_caso =request.form["num_caso"]
    descripcion =request.form["int_descripcion"]
    fecha =request.form["int_fecha"]
    doc_pronal =request.form["doc_pronal"]
    int_compromiso =request.form["int_compromiso"]
    int_fecha_compromiso =request.form["int_fecha_compromiso"]
    int_estado_compromiso = request.form.get("int_estado_compromiso", "pendiente")

    nueva_intervencion(num_caso, fecha, doc_pronal, descripcion, int_compromiso, int_fecha_compromiso, int_estado_compromiso)
    return redirect(url_for("ver_caso", num_caso=num_caso))

@programa.route("/casos/<int:num_caso>/intervenciones", methods=["GET"])
def lista_intervenciones(num_caso):
    intervenciones = obtener_intervenciones(num_caso)
    return render_template("detalle_caso.html", caso_id=num_caso, intervenciones=intervenciones)

@programa.route("/intervenciones/nueva/<int:num_caso>")
def nueva_intervencion_form(num_caso):
    return render_template("intervenciones.html", num_caso=num_caso)