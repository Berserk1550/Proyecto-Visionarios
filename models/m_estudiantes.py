from conexion import *

class Estudiante:
    
    def consultarEstudiante(self):
        db = conexion()
        cursor = db.cursor() 
        sql = """SELECT documento, est_nombres, est_apellidos, est_fecha_nacimiento, est_grado, nombre_acudiente, apellido_acudiente, telefono_acudiente
                FROM estudiantes 
                WHERE est_estado = %s"""
        est_estado = "activo"
        cursor.execute(sql, (est_estado,))
        resultado = cursor.fetchall()
        return resultado


    def IngresarEstudiante(self, documento, est_nombres, est_apellidos, est_fecha_nacimiento,est_grado,nombre_acudiente, apellido_acudiente, telefono_acudiente):

        db = conexion()
        cursor = db.cursor()

        sql_verificar = "SELECT documento FROM estudiantes WHERE documento = %s"
        cursor.execute(sql_verificar, (documento,))
        existe = cursor.fetchone()

        if existe:
            return "existe" 


        sql_insert = """INSERT INTO estudiantes
        (documento, est_nombres, est_apellidos, est_fecha_nacimiento, est_grado,
        nombre_acudiente, apellido_acudiente, telefono_acudiente)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

        valores = (
            documento,
            est_nombres,
            est_apellidos,
            est_fecha_nacimiento,
            est_grado,
            nombre_acudiente,
            apellido_acudiente,
            telefono_acudiente
        )

        cursor.execute(sql_insert, valores)  # ← SIN doble paréntesis
        db.commit()

        return "ok"



    def consultarEstudiantePorDocumento(self, documento):
        db = conexion()
        cursor = db.cursor()
        sql = """
            SELECT est_nombres, est_apellidos, est_fecha_nacimiento, est_grado,
                nombre_acudiente, apellido_acudiente, telefono_acudiente
            FROM estudiantes
            WHERE documento = %s
        """
        cursor.execute(sql, (documento,))
        resultado = cursor.fetchone()
        return resultado


    def actualizarEstudiante(self, documento, est_nombres, est_apellidos, est_fecha_nacimiento,est_grado,nombre_acudiente, apellido_acudiente, telefono_acudiente):

        db = conexion()
        cursor = db.cursor()

        sql = """
            UPDATE estudiantes
            SET est_nombres=%s,
                est_apellidos=%s,
                est_fecha_nacimiento=%s,
                est_grado=%s,
                nombre_acudiente=%s,
                apellido_acudiente=%s,
                telefono_acudiente=%s
            WHERE documento=%s
        """

        valores = (est_nombres, est_apellidos, est_fecha_nacimiento,est_grado,nombre_acudiente, apellido_acudiente, telefono_acudiente,documento)

        cursor.execute(sql, valores)
        db.commit()
        return "ok"


    def eliminarEstudiante(self, documento):
        var_conexion = conexion()
        mi_db = conexion()
        sql = """UPDATE estudiantes
                SET est_estado = 'retirado'
                WHERE documento = %s"""
        var_conexion.execute(sql, (documento,))
        mi_db.commit()
        return "ok"


mi_estudiante = Estudiante()