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
            return render_template("registrar_profesional.html", error="El usuario ya existe")

        return redirect("listar_profesional.html")

    return render_template("registrar_profesional.html")

@programa.route("/admin/modificar_usuario/<doc_pronal>", methods=["GET"])
def modificar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    usuario = mi_usuario.consultarUsuarioPorDocumento(doc_pronal)

    return render_template("modificar_profesional.html", usuario=usuario)

@programa.route("/admin/modificar_usuario/<doc_pronal>", methods=["POST"])
def actualizar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    rol = request.form['rol']

    mi_usuario.actualizarUsuario(doc_pronal, nombres, apellidos, telefono, email, rol)

    return redirect("/admin/usuarios")

@programa.route("/admin/eliminar_usuario/<doc_pronal>", methods=["POST"])
def eliminar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    mi_usuario.eliminarUsuario(doc_pronal)

    return redirect("/admin/usuarios")