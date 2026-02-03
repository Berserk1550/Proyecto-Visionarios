import mysql.connector
from datetime import datetime

# Guardar nueva intervención
def nueva_intervencion(num_caso, documento, doc_pronal, descripcion, compromiso):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor = conexion.cursor()
    sql = """INSERT INTO intervenciones
         (num_caso, doc_pronal, descripcion,
         int_compromiso, int_fecha_compromiso, int_estado_compromiso, int_estado, fecha, fecha_registro)
         VALUES (%s,%s,%s,%s,%s,%s,'activa',%s,%s)"""
    valores = ( num_caso, doc_pronal, descripcion, compromiso, datetime.now().strftime("%Y-%m-%d"),"Pendiente", datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_intervenciones(num_caso):
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="visionarios")
    cursor = conexion.cursor(dictionary=True)
    sql = """SELECT i.id_intervencion, i.fecha, i.doc_pronal, i.descripcion, i.int_compromiso, i.int_fecha_compromiso, i.int_estado_compromiso, i.int_estado, i.fecha_registro, e.documento FROM intervenciones i JOIN casos c ON i.num_caso = c.num_caso JOIN estudiantes e ON c.documento = e.documento WHERE i.num_caso = %s ORDER BY i.fecha DESC"""
    cursor.execute(sql, (num_caso,))
    intervenciones = cursor.fetchall()
    cursor.close()
    conexion.close()
    return intervenciones
