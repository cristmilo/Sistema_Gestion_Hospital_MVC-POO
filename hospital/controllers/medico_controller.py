# controllers/medico_controller.py
from controllers.base_controller import BaseController
from utils.validaciones import validar_entero, validar_texto, validar_email

class MedicoController(BaseController):

    def guardar(self, datos, foto_bytes):
        if not self._validar(datos): return
        exito, msg = self.model.registrar(
            int(datos["id"]), datos["nombre"],
            datos["especialidad"], datos["email"], foto_bytes)
        if exito:
            self.view.mostrar_exito("Médico registrado")
            self.view.limpiar_form(); self.cargar_tabla()
        else:
            self.view.mostrar_error(msg)

    def actualizar(self, datos, foto_bytes):
        if not self._validar(datos): return
        if not self.view.confirmar("¿Actualizar este médico?"): return
        exito, msg = self.model.actualizar(
            int(datos["id"]), datos["nombre"],
            datos["especialidad"], datos["email"], foto_bytes)
        if exito:
            self.view.mostrar_exito("Médico actualizado")
            self.view.limpiar_form(); self.cargar_tabla()
        else:
            self.view.mostrar_error(msg)

    def eliminar(self, id_valor):
        if not validar_entero(id_valor, "ID"): return
        if not self.view.confirmar("¿Eliminar este médico?"): return
        super().eliminar(int(id_valor))

    def cargar_foto(self, id_valor):
        exito, filas = self.model.obtener_foto(int(id_valor))
        if exito and filas and filas[0][0]:
            return filas[0][0]
        return None

    def _validar(self, datos):
        return (validar_entero(datos["id"], "ID") and
                validar_texto(datos["nombre"], "Nombre") and
                validar_texto(datos["especialidad"], "Especialidad") and
                validar_email(datos["email"]))
