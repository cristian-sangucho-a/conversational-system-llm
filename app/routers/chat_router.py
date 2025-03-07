from fastapi import APIRouter, Depends, Form, UploadFile, File
from fastapi.responses import FileResponse
from services.ask_via_audio_service import AskViaAudioService
from services.ask_via_text_service import AskViaTextService
from core.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.message import ChatRequest, ChatResponse

chat_router = APIRouter(tags=["Chat Endpoints"])

@chat_router.post(
    "/audio/", 
    response_class=FileResponse,
    responses={
        200: {"description": "Audio response generated successfully"},
        400: {"description": "Invalid audio file format"},
        500: {"description": "Internal server error"}
    }
)
async def ask_via_audio(
    user_id: int = Form(...), 
    conversation_id: int = Form(...), 
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    ask_via_audio = AskViaAudioService(db)
    return await ask_via_audio.model_response_via_audio(file, user_id, conversation_id)
     
@chat_router.post(
    "/text/",
    response_model=ChatResponse,
     responses={
        200: {"description": "Respuesta de texto generada exitosamente"},
        422: {"description": "Error de validación de datos"},
        500: {"description": "Error interno del servidor"}
    }
    )
async def ask_via_text(
    chat_request: ChatRequest, 
    db: AsyncSession = Depends(get_db)
):
    ask_via_text = AskViaTextService(db)
    return await ask_via_text.model_response_via_text(chat_request)
