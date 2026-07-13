from fastapi import FastAPI
from app.routers import prestamos, estudiantes, libros
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
  title="Library Management API",
  description="API for managing library loans, books, and students.",
  version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management API!", "status": "running", "docs": "/docs"}

app.include_router(prestamos.route)
app.include_router(estudiantes.route)
app.include_router(libros.route)
