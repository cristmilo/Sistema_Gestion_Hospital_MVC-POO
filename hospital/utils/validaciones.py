# utils/validaciones.py
# ─────────────────────────────────────────────
# Funciones de validación reutilizables.
# Se importan en los controllers para verificar
# los datos antes de mandarlos a la BD.
# ─────────────────────────────────────────────

import re
from tkinter import messagebox

def validar_entero(valor, nombre):
    """El valor debe ser un número entero positivo."""
    if not str(valor).strip().isdigit():
        messagebox.showerror("Validación", f"{nombre} solo acepta números enteros.")
        return False
    return True

def validar_texto(valor, nombre, minimo=2, maximo=50):
    """El valor debe tener longitud entre minimo y maximo."""
    if len(str(valor).strip()) < minimo:
        messagebox.showerror("Validación", f"{nombre} debe tener al menos {minimo} caracteres.")
        return False
    if len(str(valor).strip()) > maximo:
        messagebox.showerror("Validación", f"{nombre} no puede superar {maximo} caracteres.")
        return False
    return True

def validar_email(valor):
    """El valor debe tener formato de email válido."""
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if not re.match(patron, str(valor).strip()):
        messagebox.showerror("Validación", "El formato del email no es válido.")
        return False
    return True
