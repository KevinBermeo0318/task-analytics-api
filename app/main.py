from fastapi import FastAPI
from app.config import settings
from app.database import engine, Base
from app.routers import tasks, analytics

#CREA  LAS TABLAS EN LA BASE DE DATOS AL INICIAR (PARA DESARROLLO, NO PRODUCCIÓN)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API para la gestión de tareas y análisis de productividad",
    docs_url="/docs",
    redoc_url="/redoc",
)

#Registra Routers
app.include_router(tasks.router)
app.include_router(analytics.router)

@app.get("/", tags=["Root"])
def read_root():
    """Endpoint raíz que devuelve un mensaje de bienvenida."""
    return {"message": "Bienvenido a la API de gestión de tareas y análisis de productividad.",
            "docs": "/docs",
            "redoc": "/redoc"
        }

