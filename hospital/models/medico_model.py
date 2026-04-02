# models/medico_model.py
from models.base_model import BaseModel

class MedicoModel(BaseModel):

    def registrar(self, id, nombre, especialidad, email, foto):
        return self.ejecutar_sp("sp_registrar_medico",
                                [id, nombre, especialidad, email, foto])

    def actualizar(self, id, nombre, especialidad, email, foto):
        return self.ejecutar_sp("sp_actualizar_medico",
                                [id, nombre, especialidad, email, foto])

    def eliminar(self, id):
        return self.ejecutar_sp("sp_eliminar_medico", [id])

    def obtener_todos(self):
        return self.consultar_sp("sp_mostrar_medicos")

    def obtener_foto(self, id):
        return self.consultar_sp("sp_obtener_foto_medico", [id])
