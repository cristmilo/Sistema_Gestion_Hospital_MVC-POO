# models/cita_model.py
from models.base_model import BaseModel

class CitaModel(BaseModel):

    def registrar(self, id_paciente, id_medico, fecha):
        return self.ejecutar_sp("sp_registrar_cita",
                                [id_paciente, id_medico, fecha])

    def eliminar(self, id):
        return self.ejecutar_sp("sp_eliminar_cita", [id])

    def obtener_todos(self):
        return self.consultar_sp("sp_mostrar_citas")
