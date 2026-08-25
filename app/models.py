from datetime import datetime

from pydantic import BaseModel, Field, field_validator

class ReservaCreate(BaseModel):
    cliente: str = Field(min_length=2, max_length=80)
    servicio: str = Field(min_length=2, max_length=80)
    fecha_hora: datetime

    @field_validator('cliente', 'servicio')
    @classmethod
    def validar_texto_no_vacio(cls, valor: str) -> str:
        texto_limpio = valor.strip()
        if not texto_limpio:
            raise ValueError("El campo no puede estar vacío ni contener solo espacios.")
        return texto_limpio

class Reserva(ReservaCreate):
    id: int
    estado: str = "pendiente"
