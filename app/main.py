from fastapi import FastAPI
from app.core.config import settings
from app.core.security import setup_security
from app.api.endpoints import router as api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configurar seguridad (CORS, Trusted Hosts)
setup_security(app)

# Registrar rutas
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}
