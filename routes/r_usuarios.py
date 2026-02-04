from conexion import *
from models.m_usuarios import *
from programa import *

@programa.route("/admin/consultar_usuario")
def consultarUsuario():
    
    
    respuesta = mi_usuario.consultarUsuarios()
    
    return render_template("listar_usuarios.html", usuarios = respuesta)

@programa.route('/admin/agregar_usuario', methods=['GET', 'POST'])
def crear_usuario():
    if not session.get("login") or session.get("rol") != "administrador":
        return redirect('/')

    if request.method == 'POST':
        doc_pronal = request.form['documento']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        rol = request.form['rol']
        password = request.form['password']  # luego la encriptamos si quieres

        respuesta = mi_usuario.crearUsuario(
            doc_pronal, nombres, apellidos, password, telefono, email, rol
        )

        if respuesta == "existe":
            return render_template("admin/agregar_usuario.html", error="El usuario ya existe")

        return redirect("/admin/usuarios")

    return render_template("admin/agregar_usuario.html")

@programa.route("/admin/modificar_usuario/<doc_pronal>", methods=["GET"])
def modificar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") != "administrador":
        return redirect('/')

    usuario = mi_usuario.consultarUsuarioPorDocumento(doc_pronal)

    return render_template("admin/modificar_usuario.html", usuario=usuario)

@programa.route("/admin/modificar_usuario/<doc_pronal>", methods=["POST"])
def actualizar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") != "administrador":
        return redirect('/')

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    rol = request.form['rol']

    mi_usuario.actualizarUsuario(doc_pronal, nombres, apellidos, telefono, email, rol)

    return redirect("/admin/usuarios")

@programa.route("/admin/eliminar_usuario/<doc_pronal>", methods=["POST"])
def eliminar_usuario(doc_pronal):

    if not session.get("login") or session.get("rol") != "administrador":
        return redirect('/')

    mi_usuario.eliminarUsuario(doc_pronal)

    return redirect("/admin/usuarios")