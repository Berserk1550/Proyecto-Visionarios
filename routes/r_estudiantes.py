from conexion import *
from programa import programa
from models.m_estudiantes import mi_estudiante


# ================================
# LISTAR ESTUDIANTES
# ================================
@programa.route("/admin/consultar_estudiante")
def consultarEstudiantes():

    respuesta = mi_estudiante.consultarEstudiante()
    return render_template("listar_estudiantes.html", estudiantes=respuesta)


# ================================
# CREAR ESTUDIANTE
# ================================
@programa.route('/admin/agregar_estudiante', methods=['GET', 'POST'])
def crearEstudiante():
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    if request.method == 'POST':
        documento = request.form['documento_estud']
        nombres = request.form['nombres_estud']
        apellidos = request.form['apellidos_estud']
        fecha_nacimiento = request.form['fecha_nacimiento_estud']
        grado = request.form['grado']
        nombre_acudiente = request.form['nombre_acudiente']
        apellido_acudiente = request.form['apellido_acudiente']
        telefono_acudiente = request.form['telefono_acudiente']

        respuesta = mi_estudiante.IngresarEstudiante(
            documento, nombres, apellidos, fecha_nacimiento,
            grado, nombre_acudiente, apellido_acudiente, telefono_acudiente
        )

        if respuesta == "existe":
            return render_template("registrar_estudiante.html", error="El estudiante ya existe")
        else:
            return redirect("/admin/consultar_estudiante")

    # ✅ ESTE RETURN FALTABA
    return render_template("registrar_estudiante.html")



# ================================
# MOSTRAR FORMULARIO PARA EDITAR
# ================================
@programa.route("/admin/modificar_estudiante/<documento>", methods=["GET"])
def modificarEstudiante(documento):
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    estudiante = mi_estudiante.consultarEstudiantePorDocumento(documento)
    return render_template("modificar_estudiante.html", estudiante=estudiante, documento=documento)


# ================================
# GUARDAR CAMBIOS DEL ESTUDIANTE
# ================================
@programa.route("/admin/actualizar_estudiante/<documento>", methods=["POST"])
def actualizarEstudiante(documento):
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    fecha_nacimiento = request.form['fecha_nacimiento']
    grado = request.form['grado']
    nombre_acudiente = request.form['nombre_acudiente']
    apellido_acudiente = request.form['apellido_acudiente']
    telefono_acudiente = request.form['telefono_acudiente']

    mi_estudiante.actualizarEstudiante(
        documento, nombres, apellidos, fecha_nacimiento,
        grado, nombre_acudiente, apellido_acudiente, telefono_acudiente
    )

    return redirect("/admin/consultar_estudiante")


# ================================
# ELIMINAR (RETIRAR) ESTUDIANTE
# ================================
@programa.route("/admin/eliminar_estudiante/<documento>", methods=["POST"])
def eliminarEstudiante(documento):
    if not session.get("login") or session.get("rol") not in ("administrador", "directivo"):
        return redirect("/")

    mi_estudiante.eliminarEstudiante(documento)
    return redirect("/admin/consultar_estudiante")