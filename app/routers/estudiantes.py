from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import EstudianteResponseSchema, EstudianteSchema
from app.models import EstudianteModel

route = APIRouter(prefix="/student", tags=["Students"])

@route.post("/", response_model=EstudianteResponseSchema)
def create_student(student: EstudianteSchema, db: Session=Depends(get_db)):
  try:
    student_db = db.query(EstudianteModel).filter(EstudianteModel.nombre == student.nombre).first()
    if student_db:
      raise HTTPException(status_code=400, detail="Student already exists")

    new_student = EstudianteModel(
      nombre=student.nombre,
      carrera=student.carrera,
      correo_electronico=student.correo_electronico
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
  except Exception as e:
    raise HTTPException(status_code=500, detail="Error creating student")


@route.get("/", response_model=List[EstudianteResponseSchema])
def get_students(db: Session=Depends(get_db)):
  return db.query(EstudianteModel).all()