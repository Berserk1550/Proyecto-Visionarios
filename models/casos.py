import mysql.connector

def nuevo_caso(documento, caso_tipo, caso_descripcion, caso_fecha_apertura, doc_pronal):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor = conexion.cursor()
    sql = """INSERT INTO casos(documento, caso_tipo, caso_descripcion, caso_fecha_apertura, doc_pronal, caso_estado) VALUES (%s,%s,%s,%s,%s,'abierto')"""

    valores = (documento, caso_tipo, caso_descripcion, caso_fecha_apertura, doc_pronal)

    cursor.execute(sql,valores)
    conexion.commit()
    cursor.close()
    conexion.close()

#esta funcion le pertenece al boton ver detalle en listar casos.
def obtener_caso(num_caso,):
    conexion = mysql.connector.connect( host="localhost", user="root", password="", database="visionarios" )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM casos WHERE num_caso = %s", (num_caso,))
    caso = cursor.fetchone()
    cursor.close()
    conexion.close()
    return caso

#esta funcion le pertenece al boton cerrar caso en listar casos
def cerrar_caso(num_caso, fecha_cierre):
    conexion = mysql.connector.connect( host="localhost", user="root", password="", database="visionarios" )
    cursor = conexion.cursor()
    sql = """UPDATE casos  SET caso_estado = 'cerrado', caso_fecha_cierre = %s WHERE num_caso = %s"""
    valores = (fecha_cierre, num_caso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def estudiante_activo(documento):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor = conexion.cursor()
    sql = "SELECT est_estado FROM estudiantes WHERE documento = %s"
    cursor.execute(sql, (documento,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    if resultado and resultado[0] == "activo":
        return True
    else:
        return False


#con esta funcion visualizamos todos los casos de entrada al html.
def todos_casos_listados():
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor=conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM casos")
    casos=cursor.fetchall()
    cursor.close()
    conexion.close()
    return casos

#esta funcion le pertenece al boton buscar de la barra en listar casos.
def obtener_caso_doc(documento):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor=conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM casos WHERE documento =%s",(documento,))
    casos=cursor.fetchall()
    cursor.close()
    conexion.close()
    return casos


def eliminar_caso(num_caso):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor=conexion.cursor(dictionary=True)
    sql="DELETE FROM casos WHERE num_caso=%s"
    cursor.execute(sql,(num_caso,))
    conexion.commit()
    cursor.close()
    conexion.close()