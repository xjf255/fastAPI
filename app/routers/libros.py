from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import LibroModel
from app.schemas import LibroSchema, LibroResponseSchema

route = APIRouter(prefix="/books", tags=["Books"])

@route.post("/", response_model=LibroResponseSchema)
def create_book(book: LibroSchema, db: Session = Depends(get_db)):
    try:
        book_db = db.query(LibroModel).filter(LibroModel.titulo == book.titulo).first()
        if book_db:
            raise HTTPException(status_code=400, detail="Book already exists")

        new_book = LibroModel(
            titulo=book.titulo,
            autor=book.autor,
            fecha_publicacion=book.fecha_publicacion,
            disponible=book.disponible
        )
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating book")
    
@route.get("/", response_model=List[LibroResponseSchema])
def get_books(db: Session = Depends(get_db)):
    return db.query(LibroModel).all()
