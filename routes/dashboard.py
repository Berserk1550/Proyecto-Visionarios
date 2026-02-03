from flask import render_template
from programa import programa

@programa.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", casos_activos=0)

