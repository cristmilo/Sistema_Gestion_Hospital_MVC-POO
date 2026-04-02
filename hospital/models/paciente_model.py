# models/paciente_model.py
# ─────────────────────────────────────────────
# Hereda de BaseModel.
# Solo se encarga de llamar los SPs
# relacionados con pacientes.
# NO tiene lógica de negocio ni de interfaz.
# ─────────────────────────────────────────────

from models.base_model import BaseModel

class PacienteModel(BaseModel):

    def registrar(self, id, nombre, apellido, telefono, email, foto):
        return self.ejecutar_sp("sp_registrar_paciente",
                                [id, nombre, apellido, telefono, email, foto])

    def actualizar(self, id, nombre, apellido, telefono, email, foto):
        return self.ejecutar_sp("sp_actualizar_paciente",
                                [id, nombre, apellido, telefono, email, foto])

    def eliminar(self, id):
        return self.ejecutar_sp("sp_eliminar_paciente", [id])

    def obtener_todos(self):
        return self.consultar_sp("sp_mostrar_pacientes")

    def obtener_foto(self, id):
        return self.consultar_sp("sp_obtener_foto_paciente", [id])
