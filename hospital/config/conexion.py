# config/conexion.py
# ─────────────────────────────────────────────
# Este archivo tiene UNA sola responsabilidad:
# abrir y retornar una conexión a MySQL.
# Todos los models lo importan para conectarse.
# ─────────────────────────────────────────────

import mysql.connector

def get_conexion():
    return mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "",
        database = "hospital"
    )
