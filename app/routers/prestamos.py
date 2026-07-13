from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import PrestamoModel, LibroModel, EstudianteModel
from app.schemas import CreatePrestamoSchema, PrestamoResponseSchema

route = APIRouter(prefix="/loans", tags=["Loans"])

@route.post("/", response_model=PrestamoResponseSchema)

def create_loan(loan: CreatePrestamoSchema, db: Session = Depends(get_db)):
  student = db.query(EstudianteModel).filter(EstudianteModel.id == loan.estudiante_id).first()
  if not student:
    raise HTTPException(status_code=404, detail="Student not found")
  
  book = db.query(LibroModel).filter(LibroModel.id == loan.libro_id).first()
  if not book:
    raise HTTPException(status_code=404, detail="Book not found")
  if not book.disponible:
    raise HTTPException(status_code=400, detail="Book is not available for loan")
  
  new_loan = PrestamoModel(
    libro_id=loan.libro_id,
    estudiante_id=loan.estudiante_id,
    fecha_prestamo=loan.fecha_prestamo,
    fecha_devolucion=loan.fecha_devolucion,
    devuelto=loan.devuelto
  )
  book.disponible = False
  db.add(new_loan)
  db.commit()
  db.refresh(new_loan)
  return new_loan

@route.get("/", response_model=List[PrestamoResponseSchema])
def get_loans(db: Session = Depends(get_db)):
  return db.query(PrestamoModel).all()
  