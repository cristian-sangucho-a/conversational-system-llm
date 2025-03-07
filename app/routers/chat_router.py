from fastapi import APIRouter, Depends, Form, UploadFile, File
from services.ask_via_audio_service import AskViaAudioService
from core.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession

chat_router = APIRouter()

@chat_router.post(
    "/audio/")
async def ask_via_audio(
    user_id: int = Form(...), 
    conversation_id: int = Form(...), 
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    ask_via_audio = AskViaAudioService(db)
    return await ask_via_audio.model_response_via_audio(file, user_id, conversation_id)
     
    
