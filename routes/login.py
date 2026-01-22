from flask import Flask, render_template, request, redirect, session
import re, hashlib
from conexion import conexion, cursor

app = Flask(__name__)
app.secret_key = "super_segura"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        documento = request.form["usuario"]
        password = request.form["password"]

        if len(documento) >25:
            return render_template("iniciar_sesion.html", msg="Formato de Documento Invalido")

        password_hash = hashlib.sha125(password.enconde()).hexdigest()
        var_conexion = conexion()
        var_cursor = cursor(var_conexion)
        sql = """SELECT usuarios.doc_pronal, prof_nombres, prof_apellidos, user_rol, prof_estado, user_passford_hash FROM usuarios INNER JOIN profesionales ON usuarios.doc_pronal = profesionales.doc_pronal WHERE usuarios.doc_pronal = %s AND prof_estado = 'activo'"""
        var_cursor.execute(sql,(documento))
        resultado = var_cursor.fetchall()
        var_cursor.close()
        var_conexion.close()

        if len(resultado)==0:
            return render_template("iniciar_sesion.html", msg="Documento Sin Registrar")
        else:
            usuario = resultado[0]
            if usuario[user_passford_hash]==password_hash:
                session[login]