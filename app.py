from flask import Flask
from conexion import conexion, cursor

# Instancia principal de Flask
app = Flask(__name__)
app.secret_key = "super_segura"

# Ruta inicial (home)
@app.route("/")
def index():
    return "Sistema Visionarios activo"

if __name__ == "__main__":
    app.run(debug=True)
