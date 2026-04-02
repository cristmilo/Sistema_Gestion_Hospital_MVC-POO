# views/cita_view.py
import tkinter as tk
from views.base_view import BaseView, TEMA
from utils.exportar import exportar_excel, exportar_pdf
from tkcalendar import DateEntry

class CitaView(BaseView):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self._construir_ui()

    def set_controller(self, controller):
        self.controller = controller

    def _construir_ui(self):
        tk.Label(self, text="📅  GESTIÓN DE CITAS",
                 font=("Arial", 16, "bold"),
                 fg=TEMA["header_fg"], bg=TEMA["bg"]).pack(pady=15)

        contenedor = tk.Frame(self, bg=TEMA["bg"])
        contenedor.pack(fill="both", expand=True, padx=20)

        form = tk.LabelFrame(contenedor, text="Datos de la Cita",
                             bg=TEMA["bg"], fg=TEMA["fg"], font=("Arial", 11))
        form.pack(side="left", fill="y", padx=10, pady=5)

        tk.Label(form, text="ID Paciente:", bg=TEMA["bg"], fg=TEMA["fg"],
                 font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.id_paciente = tk.Entry(form, width=25, bg=TEMA["entry_bg"], fg=TEMA["fg"])
        self.id_paciente.grid(row=0, column=1, padx=10)

        tk.Label(form, text="ID Médico:", bg=TEMA["bg"], fg=TEMA["fg"],
                 font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=10, pady=8)
        self.id_medico = tk.Entry(form, width=25, bg=TEMA["entry_bg"], fg=TEMA["fg"])
        self.id_medico.grid(row=1, column=1, padx=10)

        tk.Label(form, text="Fecha:", bg=TEMA["bg"], fg=TEMA["fg"],
                 font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=10, pady=8)
        self.fecha = DateEntry(form, width=23, background="#1976D2",
                               foreground="white", date_pattern="yyyy-mm-dd")
        self.fecha.grid(row=2, column=1, padx=10)

        # Filtro para exportar por rango de fechas
        tk.Label(form, text="── Filtro exportación ──",
                 bg=TEMA["bg"], fg=TEMA["fg"],
                 font=("Arial", 9)).grid(row=3, column=0, columnspan=2, pady=(10,2))
        tk.Label(form, text="Desde:", bg=TEMA["bg"], fg=TEMA["fg"]).grid(row=4, column=0, sticky="w", padx=10)
        self.fecha_desde = DateEntry(form, width=23, date_pattern="yyyy-mm-dd")
        self.fecha_desde.grid(row=4, column=1, padx=10, pady=4)
        tk.Label(form, text="Hasta:", bg=TEMA["bg"], fg=TEMA["fg"]).grid(row=5, column=0, sticky="w", padx=10)
        self.fecha_hasta = DateEntry(form, width=23, date_pattern="yyyy-mm-dd")
        self.fecha_hasta.grid(row=5, column=1, padx=10, pady=4)

        btn_frame = tk.Frame(form, bg=TEMA["bg"])
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)
        for texto, cmd in [
            ("💾 Agendar",  lambda: self.controller.guardar(self.id_paciente.get(), self.id_medico.get(), self.fecha.get())),
            ("🗑️ Eliminar", self._eliminar_seleccionada),
            ("🧹 Limpiar",  self.limpiar_form),
        ]:
            tk.Button(btn_frame, text=texto, bg=TEMA["btn_bg"],
                      fg=TEMA["btn_fg"], width=13,
                      command=cmd).pack(side="left", padx=4)

        tabla_frame = tk.Frame(contenedor, bg=TEMA["bg"])
        tabla_frame.pack(side="left", fill="both", expand=True, padx=10)
        self.tabla = self.crear_tabla(tabla_frame,
                     ("ID Cita", "Paciente", "Apellido", "Médico", "Fecha"))

        exp = tk.Frame(self, bg=TEMA["bg"])
        exp.pack(pady=8)
        tk.Button(exp, text="📊 Excel (filtro fecha)", bg="#388E3C", fg="white",
                  command=self._exportar_excel).pack(side="left", padx=6)
        tk.Button(exp, text="📄 PDF (filtro fecha)", bg="#D32F2F", fg="white",
                  command=self._exportar_pdf).pack(side="left", padx=6)

    def _eliminar_seleccionada(self):
        sel = self.tabla.selection()
        if not sel:
            self.mostrar_error("Selecciona una cita de la tabla")
            return
        id_cita = self.tabla.item(sel[0])["values"][0]
        self.controller.eliminar(id_cita)

    def limpiar_form(self):
        self.id_paciente.delete(0, tk.END)
        self.id_medico.delete(0, tk.END)

    def _filas_filtradas(self):
        desde = self.fecha_desde.get()
        hasta = self.fecha_hasta.get()
        return [self.tabla.item(r)["values"]
                for r in self.tabla.get_children()
                if desde <= str(self.tabla.item(r)["values"][4]) <= hasta]

    def _exportar_excel(self):
        exportar_excel("Citas", ["ID Cita","Paciente","Apellido","Médico","Fecha"],
                       self._filas_filtradas())

    def _exportar_pdf(self):
        exportar_pdf("Listado de Citas", ["ID Cita","Paciente","Apellido","Médico","Fecha"],
                     self._filas_filtradas())
