# models/base_model.py
# ─────────────────────────────────────────────
# Clase PADRE de todos los models.
# Tiene la lógica común de conectarse a MySQL
# y ejecutar un Stored Procedure.
# Los models hijos la heredan y solo escriben
# el nombre del SP que necesitan llamar.
# ─────────────────────────────────────────────

from config.conexion import get_conexion

class BaseModel:

    def ejecutar_sp(self, nombre_sp, parametros=[]):
        """
        Llama a un Stored Procedure y retorna (exito, resultado).
        - nombre_sp  : nombre del SP en MySQL
        - parametros : lista de valores a pasar al SP
        """
        try:
            con = get_conexion()
            cur = con.cursor()
            cur.callproc(nombre_sp, parametros)
            con.commit()
            return True, "OK"
        except Exception as e:
            return False, str(e)
        finally:
            cur.close()
            con.close()

    def consultar_sp(self, nombre_sp, parametros=[]):
        """
        Llama a un SP que retorna filas (SELECT).
        Retorna (exito, lista_de_filas).
        """
        try:
            con = get_conexion()
            cur = con.cursor()
            cur.callproc(nombre_sp, parametros)
            filas = []
            for result in cur.stored_results():
                filas = result.fetchall()
            return True, filas
        except Exception as e:
            return False, str(e)
        finally:
            cur.close()
            con.close()
