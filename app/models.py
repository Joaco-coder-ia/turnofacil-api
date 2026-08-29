from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

EstadoPermitido = Literal["pendiente", "confirmada", "completada", "cancelada"]


class ReservaCreate(BaseModel):
    cliente: str = Field(min_length=2, max_length=80)
    servicio: str = Field(min_length=2, max_length=80)
    fecha_hora: datetime


class Reserva(ReservaCreate):
    id: int
    estado: EstadoPermitido = "pendiente"


class ReservaUpdate(BaseModel):
    estado: EstadoPermitido
