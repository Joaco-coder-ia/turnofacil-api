import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    resultado = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-p",
            "no:cacheprovider",
            str(Path(__file__).resolve()),
        ],
        check=False,
    )
    raise SystemExit(resultado.returncode)

from fastapi.testclient import TestClient
import app.main as api
from app.main import app, reservas

client = TestClient(app)


def setup_function() -> None:
    reservas.clear()
    api.next_id = 1


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_crear_reserva() -> None:
    response = client.post(
        "/reservas",
        json={
            "cliente": "Ana Pérez",
            "servicio": "Orientación académica",
            "fecha_hora": "2026-08-20T10:30:00",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["estado"] == "pendiente"


def test_listar_reservas() -> None:
    client.post(
        "/reservas",
        json={
            "cliente": "Luis Soto",
            "servicio": "Soporte técnico",
            "fecha_hora": "2026-08-21T12:00:00",
        },
    )

    response = client.get("/reservas")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_reserva_inexistente_entrega_404() -> None:
    response = client.get("/reservas/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Reserva no encontrada"


def test_rechaza_cliente_vacio() -> None:
    response = client.post(
        "/reservas",
        json={
            "cliente": "",
            "servicio": "Soporte técnico",
            "fecha_hora": "2026-08-21T12:00:00",
        },
    )

    assert response.status_code == 422


def test_filtrar_reservas_por_estado() -> None:
    client.post(
        "/reservas",
        json={
            "cliente": "Ana Pérez",
            "servicio": "Orientación académica",
            "fecha_hora": "2026-08-20T10:30:00",
        },
    )

    pendientes = client.get("/reservas", params={"estado": "pendiente"})
    confirmadas = client.get("/reservas", params={"estado": "confirmada"})

    assert pendientes.status_code == 200
    assert len(pendientes.json()) == 1
    assert confirmadas.status_code == 200
    assert confirmadas.json() == []


def test_filtrar_reservas_normaliza_mayusculas_y_espacios() -> None:
    client.post(
        "/reservas",
        json={
            "cliente": "Ana Pérez",
            "servicio": "Orientación académica",
            "fecha_hora": "2026-08-20T10:30:00",
        },
    )

    response = client.get("/reservas", params={"estado": " PENDIENTE "})

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_actualizar_estado_reserva_exito() -> None:
    client.post(
        "/reservas",
        json={
            "cliente": "Carlos Ruiz",
            "servicio": "Terapia",
            "fecha_hora": "2026-08-25T15:00:00",
        },
    )
    
    response = client.patch("/reservas/1", json={"estado": "confirmada"})

    assert response.status_code == 200
    assert response.json()["estado"] == "confirmada"


def test_actualizar_estado_reserva_inexistente() -> None:
    response = client.patch("/reservas/9999", json={"estado": "cancelada"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Reserva no encontrada"


def test_eliminar_reserva() -> None:
    creada = client.post(
        "/reservas",
        json={
            "cliente": "Luis Soto",
            "servicio": "Soporte técnico",
            "fecha_hora": "2026-08-21T12:00:00",
        },
    )

    response = client.delete(f"/reservas/{creada.json()['id']}")

    assert response.status_code == 204
    assert client.get("/reservas").json() == []


def test_eliminar_reserva_inexistente_entrega_404() -> None:
    response = client.delete("/reservas/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Reserva no encontrada"
