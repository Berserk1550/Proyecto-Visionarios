from conexion import *
from models.m_usuarios import *
from programa import *

@programa.route("/admin/consultar_usuario")
def consultarUsuario():
    
    
    respuesta = mi_usuario.consultarUsuarios()
    
    return render_template("listar_usuarios.html", usuarios = respuesta)

@programa.route('/admin/agregar_usuario', methods=['GET', 'POST'])
def crear_usuario():
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    if request.method == 'POST':
        doc_pronal = request.form['cedula']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form.get('telefono')
        email = request.form.get('correo')
        rol = request.form['rol']
        password = request.form['contrasena']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        respuesta = mi_usuario.ingresarUsuario(
            doc_pronal, nombres, apellidos, password_hash, telefono, email, rol
        )

        if respuesta == "existe":
            flash("El usuario ya existe", "error")
            return redirect(url_for("crear_usuario"))

        flash("Usuario registrado correctamente", "success")
        return redirect(url_for("crear_usuario"))

    return render_template("registrar_profesional.html")


@programa.route("/admin/modificar_usuario/<doc_pronal>", methods=["GET"])
def mostrar_modificar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    usuario = mi_usuario.consultarUsuarioPorDocumento(doc_pronal)

    if not usuario:
        flash("Usuario no encontrado", "error")
        return redirect(url_for("consultarUsuario"))

    return render_template(
        "modificar_profesional.html",
        usuario=usuario,
        doc_pronal=doc_pronal
    )


@programa.route("/admin/modificar_usuario/<doc_pronal>", methods=["POST"])
def actualizar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    rol = request.form['rol']

    resultado = mi_usuario.actualizarUsuario(
        doc_pronal,
        nombres,
        apellidos,
        telefono,
        correo,
        rol
    )

    if resultado == "no_existe":
        flash("El usuario no existe", "error")

    elif resultado == "sin_cambios":
        flash("No realizaste ningún cambio", "info")

    else:
        flash("Usuario actualizado correctamente", "success")

    return redirect(url_for("mostrar_modificar_usuario", doc_pronal=doc_pronal))





@programa.route("/admin/eliminar_usuario/<doc_pronal>", methods=["POST"])
def eliminar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    mi_usuario.desactivarUsuario(doc_pronal)

    return redirect(url_for("consultarUsuario"))