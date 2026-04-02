# controllers/cita_controller.py
from controllers.base_controller import BaseController
from utils.validaciones import validar_entero

class CitaController(BaseController):

    def guardar(self, id_paciente, id_medico, fecha):
        if not validar_entero(id_paciente, "ID Paciente"): return
        if not validar_entero(id_medico, "ID Médico"): return
        exito, msg = self.model.registrar(
            int(id_paciente), int(id_medico), fecha)
        if exito:
            self.view.mostrar_exito("Cita agendada correctamente")
            self.view.limpiar_form(); self.cargar_tabla()
        else:
            self.view.mostrar_error(msg)

    def eliminar(self, id_cita):
        if not self.view.confirmar(f"¿Eliminar la cita #{id_cita}?"): return
        super().eliminar(id_cita)
