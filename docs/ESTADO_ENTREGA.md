# Estado de entrega EP1

Última revisión: 25 de agosto de 2026.

Este documento separa lo que ya está preparado de lo que todavía debe ocurrir en GitHub. Un mensaje o una rama preparada no reemplaza un commit, una revisión, una ejecución de CI o un merge real.

## Verificado

- El repositorio público es `Joaco-coder-ia/turnofacil-api`.
- El README incluye a Joaquín Alberto González Sánchez, Mateo Nogueira Calvo, Benjamín Patricio Dattoli Peña, Maximiliano Gael Rodriguez Gamboa y Vicente Alonso Fabar Arce.
- Existen `main`, `develop`, ramas `feature/*` y `hotfix/validar-texto-vacio`.
- El workflow `.github/workflows/ci.yml` ejecuta pytest, pip check, compilación y construcción Docker.
- En la copia local de documentación se ejecutan 7 pruebas exitosas.
- El PR [#7](https://github.com/Joaco-coder-ia/turnofacil-api/pull/7) quedó dirigido a `develop`.
- El PR [#8](https://github.com/Joaco-coder-ia/turnofacil-api/pull/8) quedó dirigido a `develop` y contiene filtro, actualización y eliminación.
- El PR [#9](https://github.com/Joaco-coder-ia/turnofacil-api/pull/9) quedó dirigido a `main`; al revisarlo estaba sin conflictos y con su check exitoso.
- La invitación de colaborador para `Maeton` fue enviada y está pendiente de aceptación.

## Falta para entregar

1. Mateo debe aceptar la invitación `Maeton`.
2. Cada integrante debe subir sus tres pruebas nuevas desde su propia cuenta, con commit convencional, ejecución de `pytest` y PR o actualización verificable. Los mensajes publicados son instrucciones, no evidencia terminada.
3. Maximiliano todavía necesita una asignación explícita de sus tres pruebas y debe dejar una revisión real del PR que no sea suyo.
4. Los PR #7 y #8 requieren revisiones y aprobaciones de integrantes distintos del autor antes de fusionarse en `develop`.
5. El PR #9 requiere revisión de Maximiliano; después debe fusionarse en `main` por la persona autorizada.
6. Después del merge del hotfix, hay que sincronizar `main` hacia `develop` y comprobar nuevamente el filtro, PATCH y DELETE.
7. Se debe abrir y completar el PR final de `develop` hacia `main` si el flujo de entrega lo exige.
8. Benjamín debe completar `docs/TRAZABILIDAD.md` con revisores y enlaces reales a Actions; no se deben dejar marcadores `[COMPLETAR...]`.
9. El equipo debe escribir su justificación de GitFlow y cada integrante su reflexión en `docs/CONCLUSIONES.md`, con experiencias reales y sin texto generado por IA.
10. Proteger `main` con revisiones/checks obligatorios, crear la etiqueta `v0.1.0` sólo después del merge final y enviar el enlace por AVA/correo.

## Orden recomendado de cierre

`tests de cada integrante` → `revisiones` → `merge de features a develop` → `revisión y merge del hotfix a main` → `sync main/develop` → `PR final` → `trazabilidad, conclusiones, protección y tag`.

## Qué aprendimos

- La rama base importa: las features se integran en `develop`; el hotfix nace y llega a `main`, y luego debe volver a `develop`.
- Los PR y las revisiones dejan evidencia de colaboración; no basta con mencionar a alguien en un comentario.
- La CI detecta regresiones antes del merge y debe mantenerse en verde después de cada cambio.
- Los tests de límites, errores 404 y flujos completos protegen el comportamiento real de la API.
- Los commits convencionales, la trazabilidad y el README permiten explicar quién hizo qué y cómo verificarlo.
- Las conclusiones personales deben reflejar lo que cada estudiante realmente hizo y aprendió; por eso no se completan automáticamente.
