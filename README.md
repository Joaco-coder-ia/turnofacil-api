# TurnoFácil API

Microservicio sencillo para registrar y consultar reservas de atención. Este repositorio se utiliza para practicar control de versiones con Git, trabajo colaborativo mediante GitHub y automatización de pruebas con GitHub Actions.

## Integrantes

- Joaquín Alberto González Sánchez

## Tecnologías

- Python 3.13
- FastAPI
- pytest
- Git y GitHub
- GitHub Actions
- Docker

## Funciones de la API

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/health` | Comprueba que la API está funcionando |
| `POST` | `/reservas` | Registra una reserva |
| `GET` | `/reservas` | Lista reservas; admite el filtro opcional `?estado=` |
| `GET` | `/reservas/{id}` | Busca una reserva por su identificador |
| `PATCH` | `/reservas/{id}` | Actualiza el estado de una reserva |
| `DELETE` | `/reservas/{id}` | Elimina una reserva existente |

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

## Ejecución con Docker

```powershell
docker build -t turnofacil-api .
docker run --rm -p 8000:8000 turnofacil-api
```

La imagen ejecuta la API sin modo de recarga y expone el puerto 8000.

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Modelos de ramificación revisados

| Modelo | Estructura | Aplicación colaborativa | Ventaja | Consideración |
| --- | --- | --- | --- | --- |
| GitFlow | `main`, `develop`, `feature/*`, `release/*` y `hotfix/*` | Proyectos con versiones planificadas que separan desarrollo y producción | Trazabilidad clara para cada tipo de cambio | Exige mantener y sincronizar más ramas |
| GitHub Flow | `main` y ramas breves integradas mediante pull requests | Servicios con entregas frecuentes y una rama principal estable | Flujo simple con revisión continua | Depende de pruebas automáticas confiables |
| Trunk-Based Development | Rama principal y ramas de vida muy corta | Equipos que integran cambios pequeños varias veces al día | Reduce divergencias y conflictos | Exige disciplina y automatización madura |

### Estrategia del equipo

El repositorio aplica una versión simplificada de GitFlow con `main`, `develop`, `feature/*` y `hotfix/*`. Las reglas operativas se encuentran en [CONTRIBUTING.md](CONTRIBUTING.md).

> **Pendiente del equipo:** redactar aquí, con palabras propias y sin apoyo de IA, la justificación técnica de la elección. Debe explicar el propósito de `develop`, el origen de features y hotfix y cómo la estrategia facilita el trabajo de cinco integrantes.

## Integración continua

El archivo `.github/workflows/ci.yml` define un workflow básico. GitHub Actions instala las dependencias y ejecuta las pruebas:

- cuando se hace `push` a `develop`;
- cuando se abre o actualiza un pull request hacia `main`.

El workflow se ejecuta en un runner remoto de GitHub: descarga el repositorio, configura Python 3.13, instala y verifica las dependencias, ejecuta pytest, compila el código y construye la imagen Docker. Si un paso falla, el workflow queda fallido y el cambio no debe fusionarse. Esto detecta errores antes de integrar código y representa el entorno cloud simulado solicitado por la evaluación.

## Evidencias de evaluación

- [Trazabilidad de features y hotfix](docs/TRAZABILIDAD.md)
- [Conclusiones individuales](docs/CONCLUSIONES.md)
- [Declaración de uso de IA](docs/DECLARACION_IA.md)
- [Guía de contribución](CONTRIBUTING.md)
- [Checklist final](docs/CHECKLIST_ENTREGA.md)
- [Plan de colaboración](docs/PLAN_COLABORACION.md)
- [Estado de entrega y pendientes](docs/ESTADO_ENTREGA.md)

## Estructura

```text
turnofacil-api/
|-- .github/workflows/ci.yml
|-- app/
|   |-- __init__.py
|   |-- main.py
|   `-- models.py
|-- docs/
|   |-- CHECKLIST_ENTREGA.md
|   |-- CONCLUSIONES.md
|   |-- DECLARACION_IA.md
|   |-- ESTADO_ENTREGA.md
|   |-- PLAN_COLABORACION.md
|   `-- TRAZABILIDAD.md
|-- tests/
|   `-- test_api.py
|-- CONTRIBUTING.md
|-- Dockerfile
|-- pytest.ini
|-- requirements.txt
`-- README.md
```
