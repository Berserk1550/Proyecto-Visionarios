import mysql.connector

# Función para obtener conexión a la BD
def conexion():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        database="visionarios"
    )

# Función para obtener cursor con resultados en formato diccionario
def cursor(conn):
    return conn.cursor(dictionary=True)
