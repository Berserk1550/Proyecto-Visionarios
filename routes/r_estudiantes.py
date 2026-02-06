from conexion import *
from programa import programa
from models.m_estudiantes import mi_estudiante


# ================================
# LISTAR ESTUDIANTES
# ================================
@programa.route("/admin/consultar_estudiante")
def consultarEstudiantes():

    rol = session.get("rol")
    
    respuesta = mi_estudiante.consultarEstudiante()
    return render_template("listar_estudiantes.html", estudiantes=respuesta, rol = rol)


# ================================
# CREAR ESTUDIANTE
# ================================
@programa.route('/admin/agregar_estudiante', methods=['GET', 'POST'])
def crearEstudiante():
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    if request.method == 'POST':
        documento = request.form['documento_estud']
        nombres = request.form['nombre_estud']
        apellidos = request.form['apellido_estud']
        fecha_nacimiento = request.form['fecha_nacimiento_estud']
        grado = request.form['grado_estud']
        nombre_acudiente = request.form['nombre_acudiente']
        apellido_acudiente = request.form['apellido_acudiente']
        telefono_acudiente = request.form['telefono_acudiente']

        respuesta = mi_estudiante.IngresarEstudiante(
            documento, nombres, apellidos, fecha_nacimiento,
            grado, nombre_acudiente, apellido_acudiente, telefono_acudiente
        )

        if respuesta == "existe":
            flash("El Estudiente ya existe", "error")
            return redirect(url_for("crearEstudiante"))

        flash("Estudiente registrado correctamente", "success")
        return redirect(url_for("crearEstudiante"))

    return render_template("registrar_estudiante.html")



# ================================
# MOSTRAR FORMULARIO PARA EDITAR
# ================================
@programa.route("/admin/modificar_estudiante/<documento>", methods=["GET"])
def cargarModificarEstudiante(documento):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    estudiante = mi_estudiante.consultarEstudiantePorDocumento(documento)

    if not estudiante:
        return redirect("/admin/consultar_estudiante")

    return render_template(
        "modificar_estudiante.html",
        estudiante=estudiante,
        documento=documento
    )

@programa.route("/admin/modificar_estudiante/<documento>", methods=["POST"])
def actualizarEstudiante(documento):

    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    nombres = request.form['nombre_estud']
    apellidos = request.form['apellido_estud']
    fecha_nacimiento = request.form['fecha_nacimiento_estud']
    grado = request.form['grado_estud']
    nombre_acudiente = request.form['nombre_acudiente']
    apellido_acudiente = request.form['apellido_acudiente']
    telefono_acudiente = request.form['telefono_acudiente']

    resultado = mi_estudiante.actualizarEstudiante(
        documento,
        nombres,
        apellidos,
        fecha_nacimiento,
        grado,
        nombre_acudiente,
        apellido_acudiente,
        telefono_acudiente
    )

    if resultado == "sin_cambios":
        flash("No se realizó ningún cambio", "info")
    else:
        flash("Estudiante actualizado correctamente", "success")

    return redirect(url_for("actualizarEstudiante", documento=documento))




# ================================
# ELIMINAR (RETIRAR) ESTUDIANTE
# ================================
@programa.route("/admin/eliminar_estudiante/<documento>", methods=["POST"])
def eliminarEstudiante(documento):
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    mi_estudiante.eliminarEstudiante(documento)
    return redirect("/admin/consultar_estudiante")