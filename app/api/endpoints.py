import magic
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.services.analyzer import analyze_content

router = APIRouter()

# Tipos MIME permitidos (ejemplo: texto, pdf, json, csv)
ALLOWED_MIME_TYPES = {
    "text/plain",
    "application/pdf",
    "application/json",
    "text/csv"
}

@router.post("/analyze", status_code=status.HTTP_200_OK)
async def analyze_file(file: UploadFile = File(...)):
    # 1. Validar tamaño del archivo (Max 5MB)
    file_content = await file.read()
    file_size = len(file_content)
    
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"El archivo excede el tamaño máximo permitido de 5MB."
        )
        
    # 2. Validación de Magic Numbers usando python-magic
    try:
        mime_type = magic.from_buffer(file_content, mime=True)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al analizar el contenido del archivo."
        )
        
    if mime_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Tipo de archivo no soportado. Detectado: {mime_type}"
        )
        
    # 3. Análisis de PII y Secretos
    # Se decodifica el archivo como texto, ignorando errores para que funcione con txt/json/csv.
    # En caso de PDF se necesitaría extraer texto con una librería especializada (ej. PyPDF2).
    # Por simplicidad aquí asumimos contenido en texto plano si no es PDF.
    try:
        text_content = file_content.decode("utf-8", errors="ignore")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo decodificar el contenido del archivo a texto."
        )

    analysis_results = analyze_content(text_content)
    
    return {
        "filename": file.filename,
        "size_bytes": file_size,
        "mime_type": mime_type,
        "results": analysis_results
    }
