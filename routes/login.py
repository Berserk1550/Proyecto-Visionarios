from flask import render_template, request, redirect, session, url_for
from programa import programa
import hashlib
from models.mlogin import MLogin
from conexion import conexion, cursor

@programa.route("/login", methods=["GET", "POST"])
def login():
    print("si entro aqui")
    if request.method == "POST":
        documento = request.form["documento"]
        password = request.form["contrasena"]
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        print(password_hash)

        usuario_model = MLogin()
        resultado = usuario_model.loguear(documento)
        print(resultado)

        if len(resultado) == 0:
            return render_template("iniciar_sesion.html", msg="El documento ingresado se encuentra sin registrar.")
        else:
            usuario = resultado[0]
            print("si valido")
            print(usuario["user_password_hash"])
            if usuario["user_password_hash"] == password_hash:
                print("todo esta correcto papu")
                session["login"] = True
                session["doc_pronal"] = usuario["doc_pronal"]
                session["nombres"] = usuario["prof_nombres"]
                session["apellidos"] = usuario["prof_apellidos"]
                session["rol"] = usuario["user_rol"]
                print(session["rol"])
                session["estado"] = usuario["prof_estado"]

                # 🔹 Redirigir al dashboard sin importar el rol
                return redirect(url_for("dashboard"))

            else:
                print("entre aqui por accidente")
                return render_template("iniciar_sesion.html", msg="Contraseña incorrecta.")
    else:
        print("ups")
        return render_template("iniciar_sesion.html")
