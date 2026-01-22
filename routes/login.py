from flask import render_template, request, redirect, session
from app import programa
import hashlib
from models.mlogin import MLogin
from conexion import conexion, cursor

@programa.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        documento = request.form["documento"]
        password = request.form["contrasena"]
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        usuario_model = MLogin()
        resultado = usuario_model.loguear(documento)

        if len(resultado)==0:
            return render_template("iniciar_sesion.html", msg="El documento ingresado se encuentra sin registrar.")
        else:
            usuario = resultado[0]
            if usuario[user_password_hash] == password_hash:
                session["login"]= True
                session["doc_pronal"]= usuario["doc_pronal"]
                session["nombres"]= usuario["prof_nombres"]
                session["apellidos"]= usuario["prof_apellidos"]
                session["rol"]= usuario["user_rol"]
                session["estado"]= usuario["prof_estado"]

                if usuario["user_rol"] == "administrador":
                    return redirect("/admin")
                else:
                    return redirect("/panel")
            else:
                return render_template("iniciar_sesion.html", msg="Contraseña incorrecta.")