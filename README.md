# TurnoFácil API

Microservicio sencillo para registrar y consultar reservas de atención. Este repositorio se utiliza para practicar control de versiones con Git, trabajo colaborativo mediante GitHub y automatización de pruebas con GitHub Actions.

## Integrantes

- Maximiliano Rodriguez Gamboa
- Benjamín Dattoli Peña


## Tecnologías

- Python 3.13
- FastAPI
- pytest
- Git y GitHub
- GitHub Actions

## Funciones de la API

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/health` | Comprueba que la API está funcionando |
| `POST` | `/reservas` | Registra una reserva |
| `GET` | `/reservas` | Lista todas las reservas |
| `GET` | `/reservas/{id}` | Busca una reserva por su identificador |

Los datos se guardan en memoria y se borran al detener la aplicación.

## Instalación en IntelliJ IDEA

1. Abrir la carpeta del proyecto en IntelliJ IDEA.
2. Comprobar que el complemento **Python** esté instalado.
3. Seleccionar Python 3.13 como intérprete del proyecto.
4. Abrir la terminal de IntelliJ y ejecutar:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell no permite activar el entorno, se pueden ejecutar los comandos directamente con su intérprete:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Ejecución

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Después se puede abrir:

- API: http://localhost:8000
- Documentación Swagger: http://localhost:8000/docs
- Estado del servicio: http://localhost:8000/health

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Modelos de trabajo revisados

| Modelo | Ramas | Aplicación |
| --- | --- | --- |
| GitFlow | `main`, `develop`, `feature/*`, `release/*` y `hotfix/*` | Entregas planificadas que necesitan mayor control |
| Trunk-Based Development | `main` y ramas de corta duración | Integraciones pequeñas y frecuentes |

La pauta solicita `main`, `develop`, `feature/*` y `hotfix/*`; por eso el repositorio utiliza una estructura GitFlow simplificada. Las reglas están documentadas en [CONTRIBUTING.md](CONTRIBUTING.md).

## Integración continua

El archivo `.github/workflows/ci.yml` define un workflow básico. GitHub Actions instala las dependencias y ejecuta las pruebas:

- cuando se hace `push` a `develop`;
- cuando se abre o actualiza un pull request hacia `main`.

## Estructura

```text
turnofacil-api/
|-- .github/workflows/ci.yml
|-- app/
|   |-- __init__.py
|   |-- main.py
|   `-- models.py
|-- docs/
|   `-- DECLARACION_IA.md
|-- tests/
|   `-- test_api.py
|-- CONTRIBUTING.md
|-- pytest.ini
|-- requirements.txt
`-- README.md
```
