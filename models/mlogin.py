from conexion import conexion, cursor
class MLogin:
    def loguear(self,documento):
        var_conexion = conexion()
        var_cursor = cursor(var_conexion)
        sql = """SELECT usuarios.doc_pronal, profesionales.prof_nombres, profesionales.prof_apellidos, usuarios.user_rol, usuarios.user_password_hash FROM usuarios INNER JOIN profesionales ON usuarios.doc_pronal = profesionales.doc_pronal WHERE usuarios.doc_pronal=%s AND profesionales.prof_estado = 'activo'"""
        var_cursor.execute(sql,(documento,))
        resultado = var_cursor.fetchall()

        var_cursor.close()
        var_conexion.close()
        return resultado