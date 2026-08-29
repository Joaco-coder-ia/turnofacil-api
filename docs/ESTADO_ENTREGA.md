# Estado de entrega EP1

Última revisión: 29 de agosto de 2026.

Este documento separa lo que ya está preparado de lo que todavía debe ocurrir en GitHub. Un mensaje o una rama preparada no reemplaza un commit, una revisión, una ejecución de CI o un merge real.

## Verificado

- El repositorio público es `Joaco-coder-ia/turnofacil-api`.
- El README incluye a Joaquín Alberto González Sánchez, Mateo Nogueira Calvo, Benjamín Patricio Dattoli Peña, Maximiliano Gael Rodriguez Gamboa y Vicente Alonso Fabar Arce.
- Existen `main`, `develop`, ramas `feature/*` y `hotfix/validar-texto-vacio`.
- El workflow `.github/workflows/ci.yml` ejecuta pytest, pip check, compilación y construcción Docker.
- En la copia local de `develop` se ejecutan 16 pruebas exitosas.
- El PR [#7](https://github.com/Joaco-coder-ia/turnofacil-api/pull/7) fue aprobado por BenjaDaDuoc y fusionado en `develop`.
- El PR [#8](https://github.com/Joaco-coder-ia/turnofacil-api/pull/8) recibió una revisión técnica de Maeton, se corrigió la observación y fue fusionado en `develop`.
- El PR [#12](https://github.com/Joaco-coder-ia/turnofacil-api/pull/12) fue revisado por Joaco-coder-ia, retargeteado correctamente a `develop` y fusionado.
- El PR [#9](https://github.com/Joaco-coder-ia/turnofacil-api/pull/9) quedó dirigido a `main`; al revisarlo estaba sin conflictos y con su check exitoso.
- La última ejecución de GitHub Actions sobre `develop` terminó correctamente.

## Falta para entregar

1. Maximiliano debe revisar el PR #9; después debe fusionarse el hotfix en `main`.
2. Después del merge del hotfix, hay que sincronizar `main` hacia `develop` y ejecutar nuevamente la suite completa.
3. El PR final de `develop` hacia `main` debe actualizarse, quedar sin conflictos, obtener una revisión y completar CI en verde.
4. El equipo debe escribir personalmente su justificación de GitFlow y cada integrante su reflexión en `docs/CONCLUSIONES.md`, sin texto generado por IA.
5. Proteger `main` con revisiones/checks obligatorios, crear la etiqueta `v0.1.0` sólo después del merge final y enviar el enlace por AVA y correo.

## Orden recomendado de cierre

`revisión y merge del hotfix a main` → `sync main/develop` → `PR final` → `conclusiones personales` → `protección y tag`.

## Qué aprendimos

- La rama base importa: las features se integran en `develop`; el hotfix nace y llega a `main`, y luego debe volver a `develop`.
- Los PR y las revisiones dejan evidencia de colaboración; no basta con mencionar a alguien en un comentario.
- La CI detecta regresiones antes del merge y debe mantenerse en verde después de cada cambio.
- Los tests de límites, errores 404 y flujos completos protegen el comportamiento real de la API.
- Los commits convencionales, la trazabilidad y el README permiten explicar quién hizo qué y cómo verificarlo.
- Las conclusiones personales deben reflejar lo que cada estudiante realmente hizo y aprendió; por eso no se completan automáticamente.
