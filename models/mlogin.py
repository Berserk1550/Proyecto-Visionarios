from conexion import conexion, cursor
class MLogin:
    def loguear(self,documento):
        var_conexion = conexion()
        var_cursor = cursor(var_conexion)
        sql= """SELECT doc_pronal, prof_nombres, prof_apellidos, prof_estado, user_rol, user_password_hash
                 FROM usuarios
                 WHERE doc_pronal=%s AND prof_estado = 'activo'"""
        var_cursor.execute(sql,(documento,))
        resultado = var_cursor.fetchall()

        var_cursor.close()
        var_conexion.close()
        return resultado