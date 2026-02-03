from programa import programa
from flask import Flask, render_template, redirect, session
from conexion import *
from routes import login, casos, intervenciones, dashboard, r_estudiantes, r_usuarios



@programa.route("/")
def raiz():
    return render_template("iniciar_sesion.html")

if __name__ == "__main__":
    programa.run(debug=True, port=5080)
