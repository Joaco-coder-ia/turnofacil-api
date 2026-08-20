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

## Estructura del repositorio

```text
app/                 código del microservicio
tests/               pruebas automatizadas
.github/workflows/   automatización de CI
docs/                evidencias y material de entrega
```
