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

def test_actualizar_estado_reserva_exito() -> None:
    # Creamos una reserva previa
    client.post(
        "/reservas",
        json={
            "cliente": "Carlos Ruiz",
            "servicio": "Terapia",
            "fecha_hora": "2026-08-25T15:00:00",
        },
    )
    
    # Hacemos PATCH para cambiar a confirmada
    response = client.patch("/reservas/1", json={"estado": "confirmada"})
    
    assert response.status_code == 200
    assert response.json()["estado"] == "confirmada"


def test_actualizar_estado_reserva_inexistente() -> None:
    # Intentamos modificar una reserva con ID 9999 que no existe
    response = client.patch("/reservas/9999", json={"estado": "cancelada"})
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Reserva no encontrada"

def test_rechaza_cliente_largo() -> None:
    response = client.post(
        "/reservas",
        json={
            "cliente": "A" * 81,  # 81 caracteres, supera el límite de 80
            "servicio": "Soporte técnico",
            "fecha_hora": "2026-08-25T12:00:00",
        },
    )
    assert response.status_code == 422


def test_rechaza_servicio_largo() -> None:
    response = client.post(
        "/reservas",
        json={
            "cliente": "Ana Pérez",
            "servicio": "S" * 81,  # 81 caracteres, supera el límite de 80
            "fecha_hora": "2026-08-25T12:00:00",
        },
    )
    assert response.status_code == 422


def test_acepta_limites_permitidos() -> None:
    # Probando exactamente el límite inferior (2 caracteres)
    response_min = client.post(
        "/reservas",
        json={
            "cliente": "Lu", 
            "servicio": "PC", 
            "fecha_hora": "2026-08-25T12:00:00",
        },
    )
    assert response_min.status_code == 201

    # Probando exactamente el límite superior (80 caracteres)
    response_max = client.post(
        "/reservas",
        json={
            "cliente": "B" * 80,
            "servicio": "T" * 80,
            "fecha_hora": "2026-08-25T12:00:00",
        },
    )
    assert response_max.status_code == 201