# models/medicamento_model.py
from models.base_model import BaseModel

class MedicamentoModel(BaseModel):

    def registrar(self, id, nombre, categoria, stock, foto):
        return self.ejecutar_sp("sp_registrar_medicamento",
                                [id, nombre, categoria, stock, foto])

    def actualizar(self, id, nombre, categoria, stock, foto):
        return self.ejecutar_sp("sp_actualizar_medicamento",
                                [id, nombre, categoria, stock, foto])

    def eliminar(self, id):
        return self.ejecutar_sp("sp_eliminar_medicamento", [id])

    def obtener_todos(self):
        return self.consultar_sp("sp_mostrar_medicamentos")

    def obtener_foto(self, id):
        return self.consultar_sp("sp_obtener_foto_medicamento", [id])
