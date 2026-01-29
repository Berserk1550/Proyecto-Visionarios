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

def obtener_caso():
    conexion = mysql.connector.connect( host="localhost", user="root", password="", database="visionarios" )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM casos")
    casos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return casos

def caso_id(num_caso,):
    conexion = mysql.connector.connect( host="localhost", user="root", password="", database="visionarios" )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM casos WHERE num_caso = %s", (num_caso,))
    caso = cursor.fetchone()
    cursor.close()
    conexion.close()
    return caso

def cerrar_caso(num_caso, fecha_cierre):
    conexion = mysql.connector.connect( host="localhost", user="root", password="", database="visionarios" )
    cursor = conexion.cursor()
    sql = """UPDATE casos  SET caso_estado = 'cerrado', caso_fecha_cierre = %s WHERE num_caso = %s"""
    valores = (fecha_cierre, num_caso)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

