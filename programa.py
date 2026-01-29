from flask import Flask
programa = Flask(__name__)
programa.secret_key = "super_segura"

#se genera el archivo programa.py porque al añadir mas archivos .py a parte de iniciar sesion, se genero una dependencia circular, por lo que separar la instancia flask era necesario para romper el ciclo
#programa.py ahora es la instancia. 