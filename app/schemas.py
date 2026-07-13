from pydantic import BaseModel
from datetime import date
from typing import Optional

class LibroSchema(BaseModel):
    id: int
    titulo: str
    autor: str
    fecha_publicacion: Optional[date] = date.today()
    disponible: Optional[bool] = True

class LibroResponseSchema(LibroSchema):
    class Config:
        from_attributes = True

class EstudianteSchema(BaseModel):
    id: int
    nombre: str
    carrera: str
    correo_electronico: str

class EstudianteResponseSchema(EstudianteSchema):
    class Config:
        from_attributes = True

class CreatePrestamoSchema(BaseModel):
    libro_id: int
    estudiante_id: int
    fecha_prestamo: Optional[date] = date.today()
    fecha_devolucion: Optional[date] = None
    devuelto: Optional[bool] = False

class PrestamoResponseSchema(BaseModel):
    id: int
    libro_id: int
    estudiante_id: int
    fecha_prestamo: date
    fecha_devolucion: Optional[date] = None
    devuelto: bool

    class Config:
        from_attributes = True