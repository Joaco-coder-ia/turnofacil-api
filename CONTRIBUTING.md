# Guía de contribución

## Estrategia de ramas: GitFlow

- `main`: versión estable y entregable.
- `develop`: integración del trabajo terminado.
- `feature/<nombre>`: nueva funcionalidad creada desde `develop`.
- `hotfix/<nombre>`: corrección urgente creada desde `main`.

## Flujo para una feature

1. Actualizar `develop`: `git checkout develop` y `git pull origin develop`.
2. Crear la rama y cambiarse a ella: `git checkout -b feature/nombre-corto`.
3. Hacer cambios y pruebas.
4. Crear commits pequeños con mensajes convencionales.
5. Publicar: `git push -u origin feature/nombre-corto`.
6. Abrir pull request hacia `develop`, solicitar revisión y fusionar.

## Flujo para un hotfix

1. Crear `hotfix/nombre-corto` desde `main`.
2. Corregir el defecto y agregar o actualizar una prueba.
3. Abrir pull request hacia `main`.
4. Luego de fusionar, sincronizar el mismo cambio en `develop`.

## Convención de commits

Formato: `tipo(alcance): descripción breve`

Tipos aceptados:

- `feat`: funcionalidad nueva.
- `fix`: corrección de error.
- `test`: pruebas.
- `docs`: documentación.
- `ci`: integración continua.
- `chore`: mantenimiento.

Ejemplos:

```text
feat(reservas): agrega filtro por estado
fix(api): responde 404 al buscar una reserva inexistente
test(reservas): cubre actualización de estado
docs(readme): documenta ejecución local
```

## Revisión de pull requests

- El título usa la misma convención de los commits.
- La descripción indica qué cambió y cómo se probó.
- Al menos el otro integrante revisa el PR.
- La acción de CI debe finalizar correctamente antes del merge.
- No se hacen commits directos a `main` ni `develop`.

## Buenas prácticas de control de versiones

- Actualizar `develop` antes de crear una feature.
- Mantener commits pequeños y con un único propósito.
- Ejecutar las pruebas antes de cada push.
- No fusionar pull requests cuando GitHub Actions esté fallando.
- No versionar `.venv`, `.env`, `__pycache__`, cachés ni archivos temporales.
- Mantener `main` estable y lista para una entrega.
- Sincronizar en `develop` todo hotfix fusionado en `main`.
- Resolver conflictos en la rama de trabajo y repetir las pruebas.
- Etiquetar cada entrega estable, por ejemplo `v0.1.0`.

## Distribución colaborativa

- La persona autora crea la rama, los commits y el pull request.
- Otra persona revisa el código y registra una aprobación o solicita cambios.
- Una tercera persona puede verificar el resultado de GitHub Actions.
- Ninguna persona aprueba su propio pull request.
- Cada integrante debe conservar evidencia de su contribución en commits o revisiones.

## Estructura del repositorio

```text
app/                 código del microservicio
tests/               pruebas automatizadas
.github/workflows/   automatización de CI
docs/                evidencias y material de entrega
```
