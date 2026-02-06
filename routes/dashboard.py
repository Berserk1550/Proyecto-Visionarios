from flask import render_template
from programa import programa
from conexion import *

@programa.route("/dashboard")
def dashboard():
    rol = session.get("rol")
    if session.get("login"):
        return render_template(
            "dashboard.html",
            casos_activos=0,
            rol=rol
        )
    return redirect("/")

@programa.route("/cerrar_sesion")
def cerrarSesion():
    session.clear()
    
    return redirect("/")