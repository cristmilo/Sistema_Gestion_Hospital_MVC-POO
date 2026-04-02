# views/base_view.py
# ─────────────────────────────────────────────
# Clase PADRE de todas las views.
# Tiene los métodos comunes que todas las
# pantallas usan: mostrar errores, mostrar
# mensajes de éxito y llenar la tabla.
# ─────────────────────────────────────────────

import tkinter as tk
from tkinter import ttk, messagebox

# Colores del tema claro (por defecto)
TEMA = {
    "bg"       : "#F5F5F5",
    "fg"       : "#212121",
    "btn_bg"   : "#1976D2",
    "btn_fg"   : "#FFFFFF",
    "entry_bg" : "#FFFFFF",
    "header_fg": "#1565C0",
}

class BaseView(tk.Frame):

    def __init__(self, parent):
        """
        Inicializa el Frame con el color de fondo del tema.
        Todos los módulos heredan este Frame como base.
        """
        super().__init__(parent, bg=TEMA["bg"])

    def mostrar_error(self, mensaje):
        """Muestra una ventana de error."""
        messagebox.showerror("Error", mensaje)

    def mostrar_exito(self, mensaje):
        """Muestra una ventana de éxito."""
        messagebox.showinfo("Éxito", mensaje)

    def confirmar(self, mensaje):
        """
        Muestra un diálogo de confirmación.
        Retorna True si el usuario acepta.
        """
        return messagebox.askyesno("Confirmar", mensaje)

    def llenar_tabla(self, filas):
        """
        Limpia la tabla y la rellena con las filas recibidas.
        La tabla debe llamarse self.tabla en la view hija.
        """
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for fila in filas:
            self.tabla.insert("", "end", values=fila)

    def crear_tabla(self, parent, columnas, alto=15):
        """
        Crea y retorna un Treeview (tabla visual)
        con las columnas indicadas.
        """
        tabla = ttk.Treeview(parent, columns=columnas,
                             show="headings", height=alto)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=120)
        tabla.pack(fill="both", expand=True)
        return tabla

    def crear_botones(self, parent, botones):
        """
        Crea una fila de botones.
        botones = lista de (texto, comando)
        """
        frame = tk.Frame(parent, bg=TEMA["bg"])
        frame.pack(pady=8)
        for texto, cmd in botones:
            tk.Button(frame, text=texto,
                      bg=TEMA["btn_bg"], fg=TEMA["btn_fg"],
                      width=14, command=cmd).pack(side="left", padx=4)
        return frame
