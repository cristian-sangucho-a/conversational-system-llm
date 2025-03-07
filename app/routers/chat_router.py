from fastapi import APIRouter, Depends, Form, UploadFile, File
from services.ask_via_audio import AskViaAudio
chat_router = APIRouter()

@chat_router.post(
    "/audio/")
async def ask_via_audio(
    user_id: int = Form(...), 
    conversation_id: int = Form(...), 
    file: UploadFile = File(...),
):
    ask_via_audio = AskViaAudio()
    return await ask_via_audio.model_response_via_audio(file, user_id, conversation_id)
     
    
