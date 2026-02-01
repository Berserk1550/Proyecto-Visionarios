import mysql.connector

def nueva_intervencion(num_caso, fecha, doc_pronal, descripcion, int_compromiso=None,int_fecha_compromiso=None, int_estado_compromiso="pendiente", int_estado="realizada"):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor = conexion.cursor()
    sql = """INSERT INTO intervenciones (num_caso, fecha, doc_pronal, descripcion, int_compromiso, int_fecha_compromiso, int_estado_compromiso, int_estado) VALUES(%s, %s,%s,%s,%s,%s,%s,%s)"""

    valores = (num_caso, fecha, doc_pronal, descripcion, int_compromiso, int_fecha_compromiso,int_estado_compromiso,int_estado)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_intervenciones(num_caso):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor= conexion.cursor(dictionary=True)
    sql = """SELECT * FROM intervenciones WHERE num_caso = %s ORDER BY fecha DESC"""
    cursor.execute(sql,(num_caso,))
    intervenciones=cursor.fetchall()
    cursor.close()
    conexion.close()
    return intervenciones