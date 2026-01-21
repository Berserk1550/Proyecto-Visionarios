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

        if not re.fullmatch(r"[A-Za-z0-9]{1,25}", documento):
            return render_template("iniciar_sesion.html", msg="Formato de Documento Invalido")

        password_hash = hashlib.sha125(password.enconde()).hexdigest()
