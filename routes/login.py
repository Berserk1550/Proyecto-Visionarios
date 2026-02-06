from flask import render_template, request, redirect, session, url_for
from programa import programa
import hashlib
from models.mlogin import MLogin
from conexion import *

from flask import flash

from flask import request, render_template, redirect, url_for, session, flash

@programa.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        documento = request.form["documento"]
        password = request.form["contrasena"]
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        usuario_model = MLogin()
        resultado = usuario_model.loguear(documento)

        if len(resultado) == 0:
            flash("El documento ingresado no se encuentra registrado.", "error")
            return redirect(url_for("login"))  # 🔹 Redirige después de POST
        else:
            usuario = resultado[0]
            if usuario["user_password_hash"] == password_hash:
                session["login"] = True
                session["doc_pronal"] = usuario["doc_pronal"]
                session["nombres"] = usuario["prof_nombres"]
                session["apellidos"] = usuario["prof_apellidos"]
                session["rol"] = usuario["user_rol"]
                session["estado"] = usuario["prof_estado"]
                return redirect(url_for("dashboard"))
            else:
                flash("Contraseña incorrecta.", "error")
                return redirect(url_for("login"))  # 🔹 Redirige después de POST
    else:
        return render_template("iniciar_sesion.html")


