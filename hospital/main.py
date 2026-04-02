# main.py
# ─────────────────────────────────────────────
# Punto de entrada de la aplicación.
# Aquí se conectan los models, controllers
# y views de cada módulo, y se construye
# la ventana principal con las pestañas.
# ─────────────────────────────────────────────

import tkinter as tk
from tkinter import ttk

# Models
from models.paciente_model     import PacienteModel
from models.medico_model       import MedicoModel
from models.cita_model         import CitaModel
from models.medicamento_model  import MedicamentoModel

# Views
from views.paciente_view       import PacienteView
from views.medico_view         import MedicoView
from views.cita_view           import CitaView
from views.medicamento_view    import MedicamentoView

# Controllers
from controllers.paciente_controller    import PacienteController
from controllers.medico_controller      import MedicoController
from controllers.cita_controller        import CitaController
from controllers.medicamento_controller import MedicamentoController


def main():
    root = tk.Tk()
    root.title("🏥  SISTEMA HOSPITAL")
    root.geometry("1100x650")
    root.configure(bg="#F5F5F5")

    # Favicon (coloca favicon.ico en assets/images/)
    try:
        root.iconbitmap("assets/images/favicon.ico")
    except Exception:
        pass

    # ── Notebook con pestañas ──────────────────────────
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # ── Módulo Pacientes ───────────────────────────────
    # 1. Crear view y agregarla al notebook
    paciente_view = PacienteView(notebook)
    notebook.add(paciente_view, text="👤 Pacientes")
    # 2. Crear model
    paciente_model = PacienteModel()
    # 3. Crear controller pasándole model y view
    paciente_ctrl = PacienteController(paciente_model, paciente_view)
    # 4. Conectar la view con su controller
    paciente_view.set_controller(paciente_ctrl)
    # 5. Cargar datos iniciales en la tabla
    paciente_ctrl.cargar_tabla()

    # ── Módulo Médicos ─────────────────────────────────
    medico_view  = MedicoView(notebook)
    notebook.add(medico_view, text="🩺 Médicos")
    medico_model = MedicoModel()
    medico_ctrl  = MedicoController(medico_model, medico_view)
    medico_view.set_controller(medico_ctrl)
    medico_ctrl.cargar_tabla()

    # ── Módulo Citas ───────────────────────────────────
    cita_view  = CitaView(notebook)
    notebook.add(cita_view, text="📅 Citas")
    cita_model = CitaModel()
    cita_ctrl  = CitaController(cita_model, cita_view)
    cita_view.set_controller(cita_ctrl)
    cita_ctrl.cargar_tabla()

    # ── Módulo Medicamentos ────────────────────────────
    med_view  = MedicamentoView(notebook)
    notebook.add(med_view, text="💊 Medicamentos")
    med_model = MedicamentoModel()
    med_ctrl  = MedicamentoController(med_model, med_view)
    med_view.set_controller(med_ctrl)
    med_ctrl.cargar_tabla()

    root.mainloop()


if __name__ == "__main__":
    main()
