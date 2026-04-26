from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "SentinelData AI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Seguridad
    SECRET_KEY: str = "change_me_in_production"
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:8080"]
    
    # Integración con Gemini
    GEMINI_API_KEY: str = ""
    
    # Límites
    MAX_UPLOAD_SIZE: int = 5 * 1024 * 1024  # 5 MB en bytes

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        case_sensitive=True,
        extra="ignore"
    )

settings = Settings()
