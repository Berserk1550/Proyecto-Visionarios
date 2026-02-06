from conexion import *

class Usuario:

    def consultarUsuarios(self):
        db = conexion()
        cursor = db.cursor() 
        sql = """SELECT doc_pronal, prof_nombres, prof_apellidos, prof_telefono, prof_email, user_rol
                 FROM usuarios
                 WHERE prof_estado = %s"""
        cursor.execute(sql, ("activo",))
        return cursor.fetchall()


    def ingresarUsuario(self, doc_pronal, prof_nombres, prof_apellidos, password_hash,
                        prof_telefono, prof_email, user_rol):

        db = conexion()
        cursor = db.cursor()

        #Verificar si ya existe el usuario
        sql_verificar = "SELECT doc_pronal FROM usuarios WHERE doc_pronal = %s"
        cursor.execute(sql_verificar, (doc_pronal,))
        existe = cursor.fetchone()

        if existe:
            return "existe"

        sql_insert = """INSERT INTO usuarios
                        (doc_pronal, prof_nombres, prof_apellidos, user_password_hash,
                         prof_telefono, prof_email, user_rol)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        valores = (doc_pronal, prof_nombres, prof_apellidos, password_hash,
                   prof_telefono, prof_email, user_rol)

        cursor.execute(sql_insert, valores)
        db.commit()
        return "ok"


    def consultarUsuarioPorDocumento(self, doc_pronal):
        db = conexion()
        cursor = db.cursor()
        sql = """SELECT prof_nombres, prof_apellidos, prof_telefono, prof_email, user_rol, prof_estado
                 FROM usuarios
                 WHERE doc_pronal = %s"""
        cursor.execute(sql, (doc_pronal,))
        return cursor.fetchone()


    def actualizarUsuario(self, doc_pronal, prof_nombres, prof_apellidos,
                        prof_telefono, prof_email, user_rol):

        db = conexion()
        cursor = db.cursor()

        sql = """UPDATE usuarios
                SET prof_nombres=%s,
                    prof_apellidos=%s,
                    prof_telefono=%s,
                    prof_email=%s,
                    user_rol=%s
                WHERE doc_pronal=%s"""

        valores = (
            prof_nombres,
            prof_apellidos,
            prof_telefono,
            prof_email,
            user_rol,
            doc_pronal
        )

        cursor.execute(sql, valores)
        db.commit()

        
        if cursor.rowcount == 0:
            return "sin_cambios"

        return "ok"



    def cambiarPassword(self, doc_pronal, nuevo_password_hash):
        db = conexion()
        cursor = db.cursor()

        sql = "UPDATE usuarios SET user_password_hash=%s WHERE doc_pronal=%s"
        cursor.execute(sql, (nuevo_password_hash, doc_pronal))
        db.commit()
        return "ok"


    def desactivarUsuario(self, doc_pronal):
        db = conexion()
        cursor = db.cursor()

        sql = "UPDATE usuarios SET prof_estado='inactivo' WHERE doc_pronal=%s"
        cursor.execute(sql, (doc_pronal,))
        db.commit()
        return "ok"


mi_usuario = Usuario()