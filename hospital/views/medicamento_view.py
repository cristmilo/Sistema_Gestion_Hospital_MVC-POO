# views/medicamento_view.py
import tkinter as tk
from tkinter import filedialog
from views.base_view import BaseView, TEMA
from utils.imagenes import imagen_a_bytes, bytes_a_imagetk
from utils.exportar import exportar_excel, exportar_pdf

class MedicamentoView(BaseView):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.foto_bytes = None
        self._construir_ui()

    def set_controller(self, controller):
        self.controller = controller

    def _construir_ui(self):
        tk.Label(self, text="💊  GESTIÓN DE MEDICAMENTOS",
                 font=("Arial", 16, "bold"),
                 fg=TEMA["header_fg"], bg=TEMA["bg"]).pack(pady=15)

        contenedor = tk.Frame(self, bg=TEMA["bg"])
        contenedor.pack(fill="both", expand=True, padx=20)

        form = tk.LabelFrame(contenedor, text="Datos del Medicamento",
                             bg=TEMA["bg"], fg=TEMA["fg"], font=("Arial", 11))
        form.pack(side="left", fill="y", padx=10, pady=5)

        campos = [("ID:", "id"), ("Nombre:", "nombre"),
                  ("Categoría:", "categoria"), ("Stock:", "stock")]
        self.entradas = {}
        for i, (label, key) in enumerate(campos):
            tk.Label(form, text=label, bg=TEMA["bg"], fg=TEMA["fg"],
                     font=("Arial", 11)).grid(row=i, column=0, sticky="w", padx=10, pady=6)
            entry = tk.Entry(form, width=25, bg=TEMA["entry_bg"], fg=TEMA["fg"])
            entry.grid(row=i, column=1, padx=10, pady=6)
            self.entradas[key] = entry

        tk.Label(form, text="Foto:", bg=TEMA["bg"], fg=TEMA["fg"],
                 font=("Arial", 11)).grid(row=4, column=0, sticky="w", padx=10)
        self.lbl_foto = tk.Label(form, text="Sin imagen",
                                 bg=TEMA["entry_bg"], width=15, height=5)
        self.lbl_foto.grid(row=4, column=1, padx=10, pady=6)
        tk.Button(form, text="📷 Foto", bg=TEMA["btn_bg"], fg=TEMA["btn_fg"],
                  command=self._seleccionar_foto).grid(row=5, column=1, pady=4)

        # Filtro por categoría
        filtro = tk.Frame(form, bg=TEMA["bg"])
        filtro.grid(row=6, column=0, columnspan=2, pady=6)
        tk.Label(filtro, text="Filtrar:", bg=TEMA["bg"], fg=TEMA["fg"]).pack(side="left")
        self.filtro_cat = tk.Entry(filtro, width=14, bg=TEMA["entry_bg"], fg=TEMA["fg"])
        self.filtro_cat.pack(side="left", padx=4)
        tk.Button(filtro, text="🔍", bg=TEMA["btn_bg"], fg=TEMA["btn_fg"],
                  command=self._filtrar).pack(side="left")

        btn_frame = tk.Frame(form, bg=TEMA["bg"])
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)
        for texto, cmd in [
            ("💾 Guardar",    lambda: self.controller.guardar(self._get_datos(), self.foto_bytes)),
            ("✏️ Actualizar", lambda: self.controller.actualizar(self._get_datos(), self.foto_bytes)),
            ("🗑️ Eliminar",   lambda: self.controller.eliminar(self.entradas["id"].get())),
            ("🧹 Limpiar",    self.limpiar_form),
        ]:
            tk.Button(btn_frame, text=texto, bg=TEMA["btn_bg"],
                      fg=TEMA["btn_fg"], width=13,
                      command=cmd).pack(side="left", padx=4)

        tabla_frame = tk.Frame(contenedor, bg=TEMA["bg"])
        tabla_frame.pack(side="left", fill="both", expand=True, padx=10)
        self.tabla = self.crear_tabla(tabla_frame, ("ID","Nombre","Categoría","Stock"))
        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_fila)

        exp = tk.Frame(self, bg=TEMA["bg"])
        exp.pack(pady=8)
        tk.Button(exp, text="📊 Excel", bg="#388E3C", fg="white",
                  command=lambda: exportar_excel("Medicamentos", ["ID","Nombre","Categoría","Stock"],
                  [self.tabla.item(r)["values"] for r in self.tabla.get_children()])).pack(side="left", padx=6)
        tk.Button(exp, text="📄 PDF", bg="#D32F2F", fg="white",
                  command=lambda: exportar_pdf("Medicamentos", ["ID","Nombre","Categoría","Stock"],
                  [self.tabla.item(r)["values"] for r in self.tabla.get_children()])).pack(side="left", padx=6)

    def _get_datos(self):
        return {k: e.get() for k, e in self.entradas.items()}

    def _seleccionar_foto(self):
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.gif")])
        if ruta:
            self.foto_bytes = imagen_a_bytes(ruta)
            img_tk = bytes_a_imagetk(self.foto_bytes)
            self.lbl_foto.config(image=img_tk, text="")
            self.lbl_foto.image = img_tk

    def _seleccionar_fila(self, event):
        sel = self.tabla.selection()
        if not sel: return
        valores = self.tabla.item(sel[0])["values"]
        for i, k in enumerate(["id", "nombre", "categoria", "stock"]):
            self.entradas[k].delete(0, tk.END)
            self.entradas[k].insert(0, valores[i])
        foto = self.controller.cargar_foto(valores[0])
        if foto:
            self.foto_bytes = foto
            img_tk = bytes_a_imagetk(foto)
            self.lbl_foto.config(image=img_tk, text="")
            self.lbl_foto.image = img_tk
        else:
            self.foto_bytes = None
            self.lbl_foto.config(image="", text="Sin imagen")

    def _filtrar(self):
        cat = self.filtro_cat.get().lower()
        for row in self.tabla.get_children():
            vals = self.tabla.item(row)["values"]
            if cat in str(vals[2]).lower():
                self.tabla.reattach(row, "", "end")
            else:
                self.tabla.detach(row)

    def limpiar_form(self):
        for entry in self.entradas.values(): entry.delete(0, tk.END)
        self.foto_bytes = None
        self.lbl_foto.config(image="", text="Sin imagen")
