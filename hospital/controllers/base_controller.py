# controllers/base_controller.py
# ─────────────────────────────────────────────
# Clase PADRE de todos los controllers.
# El controller es el intermediario entre
# la vista (lo que ve el usuario) y
# el model (lo que toca la base de datos).
# ─────────────────────────────────────────────

class BaseController:

    def __init__(self, model, view):
        """
        Recibe el model y la view del módulo.
        Los guarda para poder comunicarlos.
        """
        self.model = model
        self.view  = view

    def cargar_tabla(self):
        """
        Pide los datos al model y se los
        manda a la view para mostrarlos.
        """
        exito, filas = self.model.obtener_todos()
        if exito:
            self.view.llenar_tabla(filas)
        else:
            self.view.mostrar_error(filas)

    def eliminar(self, id_valor):
        """
        Le dice al model que elimine el registro
        con ese ID y recarga la tabla.
        """
        exito, msg = self.model.eliminar(id_valor)
        if exito:
            self.view.mostrar_exito("Registro eliminado")
            self.cargar_tabla()
        else:
            self.view.mostrar_error(msg)
