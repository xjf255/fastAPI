from sqlalchemy import Integer, String, Boolean, Date, ForeignKey
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class LibroModel(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    autor: Mapped[str] = mapped_column(String, nullable=False)
    fecha_publicacion: Mapped[date] = mapped_column(Date, default=date.today)
    disponible: Mapped[bool] = mapped_column(Boolean, default=True)

class EstudianteModel(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    carrera: Mapped[str] = mapped_column(String, nullable=False)
    correo_electronico: Mapped[str] = mapped_column(String, unique=True, nullable=False)

class PrestamoModel(Base):
    __tablename__ = "prestamos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    libro_id: Mapped[int] = mapped_column(Integer, ForeignKey("libros.id"), nullable=False)
    estudiante_id: Mapped[int] = mapped_column(Integer, ForeignKey("estudiantes.id"), nullable=False)
    fecha_prestamo: Mapped[date] = mapped_column(Date, default=date.today)
    fecha_devolucion: Mapped[date] = mapped_column(Date, nullable=True)
    devuelto: Mapped[bool] = mapped_column(Boolean, default=False)