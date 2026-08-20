from datetime import datetime

from pydantic import BaseModel, Field


class ReservaCreate(BaseModel):
    cliente: str = Field(min_length=2, max_length=80)
    servicio: str = Field(min_length=2, max_length=80)
    fecha_hora: datetime


class Reserva(ReservaCreate):
    id: int
    estado: str = "pendiente"
