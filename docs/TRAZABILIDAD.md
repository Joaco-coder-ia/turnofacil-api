# Trazabilidad del proyecto TurnoFácil API

Los campos pendientes deben completarse sólo con información real de GitHub. Este documento se actualiza después de cada revisión o merge; no se deben inventar revisores ni resultados de CI.

## Feature 1: filtro por estado

- Rama: `feature/filtrar-reservas`
- Objetivo: filtrar reservas mediante el parámetro `estado`.
- Commit: [`765232e`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/765232e20937bd228e3837b9ad5be191e349d223)
- Pull request: [#1](https://github.com/Joaco-coder-ia/turnofacil-api/pull/1)
- Estado observado: PR histórico integrado en `main`.
- Revisor: no quedó una revisión formal registrada en este PR histórico.
- Resultado CI: [ejecución exitosa del PR #1](https://github.com/Joaco-coder-ia/turnofacil-api/actions/runs/32329153482)

## Feature 2: actualización de estado

- Rama: `feature/actualizar-estado`
- Objetivo: actualizar el estado mediante `PATCH /reservas/{id}`.
- Commit: [`6aa6b1a`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/6aa6b1a)
- Pull request: [#6](https://github.com/Joaco-coder-ia/turnofacil-api/pull/6)
- Estado observado: PR histórico integrado en `develop`.
- Revisor: no quedó una revisión formal registrada en este PR histórico.
- Resultado CI: [ejecución exitosa posterior al merge en `develop`](https://github.com/Joaco-coder-ia/turnofacil-api/actions/runs/32899209744)

## Feature 3: filtro y eliminación de reservas

- Rama: `feature/eliminar-reserva`
- Objetivo: conservar el filtro por estado, actualizar estados y eliminar reservas con respuesta 404 cuando no existen.
- Commit: [`7ff5c2c`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/7ff5c2cc2962a91327b43275a5d3c22ab780a8e5)
- Pull request: [#8](https://github.com/Joaco-coder-ia/turnofacil-api/pull/8), fusionado en `develop`.
- Revisor: Maeton dejó una observación técnica; fue atendida en el commit `81df2f1`.
- Resultado CI: validación local de 16 pruebas y ejecución de `develop` posterior al merge.

## Hotfix: validación de textos vacíos

- Rama: `hotfix/validar-texto-vacio`
- Problema: `cliente` y `servicio` aceptaban textos compuestos sólo por espacios.
- Commit: [`1510d2d`](https://github.com/Joaco-coder-ia/turnofacil-api/commit/1510d2d7e9a94402c3f4cfae70b39d45a6cfaf6f)
- Pull request: [#9](https://github.com/Joaco-coder-ia/turnofacil-api/pull/9), abierto hacia `main`.
- Estado observado: sin conflictos y con CI exitoso; falta revisión y merge.
- Revisor solicitado: maxrodriguezg.
- Resultado CI: [ejecución exitosa del PR #9](https://github.com/Joaco-coder-ia/turnofacil-api/actions/runs/33261072736)

## Comandos aplicados

El flujo incluye `clone`, `checkout`, `pull`, `add`, `commit`, `push` y merges mediante pull requests. Las features nacen desde `develop`; el hotfix nace desde `main` y después del merge debe sincronizarse nuevamente hacia `develop`.
