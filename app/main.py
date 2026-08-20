from fastapi import FastAPI, HTTPException, status

from app.models import Reserva, ReservaCreate

app = FastAPI(
    title="TurnoFácil API",
    description="Microservicio para registrar y administrar reservas de atención.",
    version="0.1.0",
)

reservas: dict[int, Reserva] = {}
next_id = 1


@app.get("/health", tags=["sistema"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/reservas", response_model=Reserva, status_code=status.HTTP_201_CREATED)
def crear_reserva(datos: ReservaCreate) -> Reserva:
    global next_id
    reserva = Reserva(id=next_id, **datos.model_dump())
    reservas[next_id] = reserva
    next_id += 1
    return reserva


@app.get("/reservas", response_model=list[Reserva])
def listar_reservas() -> list[Reserva]:
    return list(reservas.values())


@app.get("/reservas/{reserva_id}", response_model=Reserva)
def obtener_reserva(reserva_id: int) -> Reserva:
    reserva = reservas.get(reserva_id)
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

