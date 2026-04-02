# utils/imagenes.py
# ─────────────────────────────────────────────
# Funciones para manejar imágenes con Pillow.
# Se usan en las views que tienen campo de foto.
# ─────────────────────────────────────────────

from PIL import Image, ImageTk
from io import BytesIO

def imagen_a_bytes(ruta):
    """
    Abre una imagen, la redimensiona a 150x150
    y la convierte a bytes para guardar en MySQL.
    """
    img = Image.open(ruta).convert("RGB")
    img = img.resize((150, 150))
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    return buffer.getvalue()

def bytes_a_imagetk(datos, size=(80, 80)):
    """
    Convierte bytes de MySQL a imagen
    que Tkinter puede mostrar en pantalla.
    """
    img = Image.open(BytesIO(datos)).resize(size)
    return ImageTk.PhotoImage(img)
