# Trazabilidad del proyecto TurnoFácil API

Los campos pendientes deben completarse sólo con información real de GitHub.

## Feature 1: filtro por estado

- Rama: `feature/filtrar-reservas`
- Objetivo: filtrar reservas mediante el parámetro `estado`.
- Commit: [`765232e`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/765232e20937bd228e3837b9ad5be191e349d223)
- Pull request: [#1](https://github.com/Joaco-coder-ia/turnofacil-api/pull/1)
- Revisor: `[COMPLETAR CON REVISOR REAL]`
- Resultado CI: `[COMPLETAR CON ENLACE A ACTION]`

## Feature 2: actualización de estado

- Rama: `feature/actualizar-estado`
- Objetivo: actualizar el estado mediante `PATCH /reservas/{id}`.
- Commit: [`6aa6b1a`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/6aa6b1a)
- Pull request: [#6](https://github.com/Joaco-coder-ia/turnofacil-api/pull/6)
- Revisor: `[COMPLETAR CON REVISOR REAL]`
- Resultado CI: `[COMPLETAR CON ENLACE A ACTION]`

## Hotfix: validación de textos vacíos

- Rama: `hotfix/validar-texto-vacio`
- Problema: `cliente` y `servicio` aceptaban textos compuestos sólo por espacios.
- Commit: [`1510d2d`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/1510d2d7e9a94402c3f4cfae70b39d45a6cfaf6f)
- Pull request: `[CREAR HACIA main Y PEGAR EL ENLACE]`
- Revisor: `[COMPLETAR CON REVISOR REAL]`
- Resultado CI: `[COMPLETAR CON ENLACE A ACTION]`

## Comandos aplicados

El flujo incluye `clone`, `checkout`, `pull`, `add`, `commit`, `push` y merges mediante pull requests. Las features nacen desde `develop`; el hotfix nace desde `main` y después del merge debe sincronizarse nuevamente hacia `develop`.
