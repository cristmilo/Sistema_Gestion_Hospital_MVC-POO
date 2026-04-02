# controllers/paciente_controller.py
# ─────────────────────────────────────────────
# Hereda de BaseController.
# Recibe los datos de la view, los valida
# y le dice al model qué hacer.
# ─────────────────────────────────────────────

from controllers.base_controller import BaseController
from utils.validaciones import validar_entero, validar_texto, validar_email

class PacienteController(BaseController):

    def guardar(self, datos, foto_bytes):
        """
        datos = diccionario con los valores del formulario.
        Valida y llama al model para registrar.
        """
        if not self._validar(datos):
            return
        exito, msg = self.model.registrar(
            int(datos["id"]), datos["nombre"], datos["apellido"],
            datos["telefono"], datos["email"], foto_bytes
        )
        if exito:
            self.view.mostrar_exito("Paciente registrado correctamente")
            self.view.limpiar_form()
            self.cargar_tabla()
        else:
            self.view.mostrar_error(msg)

    def actualizar(self, datos, foto_bytes):
        if not self._validar(datos):
            return
        if not self.view.confirmar("¿Deseas actualizar este paciente?"):
            return
        exito, msg = self.model.actualizar(
            int(datos["id"]), datos["nombre"], datos["apellido"],
            datos["telefono"], datos["email"], foto_bytes
        )
        if exito:
            self.view.mostrar_exito("Paciente actualizado")
            self.view.limpiar_form()
            self.cargar_tabla()
        else:
            self.view.mostrar_error(msg)

    def eliminar(self, id_valor):
        if not validar_entero(id_valor, "ID"):
            return
        if not self.view.confirmar("¿Eliminar este paciente?"):
            return
        # Llama al método eliminar del BaseController
        super().eliminar(int(id_valor))

    def cargar_foto(self, id_valor):
        """Trae la foto del paciente desde la BD."""
        exito, filas = self.model.obtener_foto(int(id_valor))
        if exito and filas and filas[0][0]:
            return filas[0][0]
        return None

    def _validar(self, datos):
        """Valida todos los campos del formulario."""
        return (validar_entero(datos["id"], "ID") and
                validar_texto(datos["nombre"], "Nombre") and
                validar_texto(datos["apellido"], "Apellido") and
                validar_entero(datos["telefono"], "Teléfono") and
                validar_email(datos["email"]))
