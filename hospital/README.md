# 🏥 Sistema Hospital

Sistema de gestión hospitalaria desarrollado en Python con arquitectura MVC, interfaz gráfica Tkinter y base de datos MySQL.

---

## 📋 Requisitos previos

- Python 3.8 o superior
- MySQL Server corriendo en `localhost`
- Git (opcional, para clonar el repositorio)

---

## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/sistema-hospital.git
cd sistema-hospital
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:
```
mysql-connector-python
pillow
tkcalendar
openpyxl
fpdf2
```

### 3. Configurar la base de datos
Abre MySQL Workbench y ejecuta el script completo:
```bash
mysql -u root -p < sql/hospital.sql
```
O abre el archivo `sql/hospital.sql` manualmente desde MySQL Workbench y ejecútalo.

### 4. Configurar la conexión
Si tu MySQL usa una contraseña diferente, edita `config/conexion.py`:
```python
def get_conexion():
    return mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "TU_CONTRASEÑA",  # <- cambia aquí
        database = "hospital"
    )
```

### 5. (Opcional) Agregar favicon
Descarga un ícono `.ico` desde https://www.favicon-generator.org/, nómbralo `favicon.ico` y colócalo en `assets/images/`.

### 6. Ejecutar la aplicación
```bash
python main.py
```

---

## 🗂️ Estructura del proyecto

```
sistema-hospital/
│
├── assets/
│   └── images/              # Favicon e imágenes de la app
│
├── config/
│   └── conexion.py          # Conexión a MySQL
│
├── controllers/
│   ├── base_controller.py   # Clase padre de todos los controllers
│   ├── paciente_controller.py
│   ├── medico_controller.py
│   ├── cita_controller.py
│   └── medicamento_controller.py
│
├── models/
│   ├── base_model.py        # Clase padre de todos los models
│   ├── paciente_model.py
│   ├── medico_model.py
│   ├── cita_model.py
│   └── medicamento_model.py
│
├── utils/
│   ├── validaciones.py      # Validación de campos
│   ├── exportar.py          # Exportar a Excel y PDF
│   └── imagenes.py          # Manejo de imágenes con Pillow
│
├── views/
│   ├── base_view.py         # Clase padre de todas las views
│   ├── paciente_view.py
│   ├── medico_view.py
│   ├── cita_view.py
│   └── medicamento_view.py
│
├── sql/
│   └── hospital.sql         # Script con tablas y Stored Procedures
│
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

---

## 🏗️ Arquitectura MVC

El proyecto sigue el patrón **Modelo - Vista - Controlador**:

| Capa | Carpeta | Responsabilidad |
|---|---|---|
| **Model** | `models/` | Llama los Stored Procedures de MySQL |
| **View** | `views/` | Construye la interfaz gráfica con Tkinter |
| **Controller** | `controllers/` | Valida datos y comunica Model con View |

El flujo de una operación es siempre:
```
View → Controller → Model → MySQL
```
Cada capa solo habla con la que tiene al lado, nunca se saltan capas.

---

## 🧩 Módulos del sistema

| Módulo | Descripción |
|---|---|
| 👤 Pacientes | Registro, edición y eliminación de pacientes con foto |
| 🩺 Médicos | Gestión de médicos con especialidad y foto |
| 📅 Citas | Agendamiento de citas con selector de calendario |
| 💊 Medicamentos | Inventario de medicamentos con filtro por categoría |

---

## ✅ Funcionalidades

- **CRUD completo** en los 4 módulos conectado a Stored Procedures de MySQL
- **Exportar a Excel** (.xlsx) usando openpyxl
- **Exportar a PDF** con formato de tabla usando fpdf2
- **Filtro por fechas** en exportación de citas
- **Filtro por categoría** en medicamentos
- **Validación de campos**: numéricos, texto y email con mensajes de error claros
- **Selector de fecha** con calendario flotante (tkcalendar)
- **Gestión de imágenes** con Pillow: JPG, PNG, GIF (redimensión automática a 150x150)
- **Diálogos de confirmación** antes de eliminar o actualizar
- **Herencia entre clases**: BaseModel, BaseController y BaseView como clases padre

---

## 🗄️ Base de datos

El script `sql/hospital.sql` crea automáticamente:

**Tablas:**
- `pacientes` — id, nombre, apellido, telefono, email, foto
- `medicos` — id, nombre, especialidad, email, foto
- `citas` — id, id_paciente, id_medico, fecha
- `medicamentos` — id, nombre, categoria, stock, foto

**Stored Procedures (16 en total):**
- `sp_registrar_*`, `sp_actualizar_*`, `sp_eliminar_*`, `sp_mostrar_*` para cada módulo
- `sp_obtener_foto_*` para pacientes, médicos y medicamentos

---

## 📦 Dependencias

| Librería | Uso |
|---|---|
| `mysql-connector-python` | Conexión a MySQL |
| `pillow` | Manejo de imágenes |
| `tkcalendar` | Selector de fechas con calendario |
| `openpyxl` | Exportar a Excel |
| `fpdf2` | Exportar a PDF |

---

## 👤 Autor

Desarrollado como proyecto académico.
