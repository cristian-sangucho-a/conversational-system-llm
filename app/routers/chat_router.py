from fastapi import APIRouter, Depends, Form, UploadFile, File

chat_router = APIRouter()

@chat_router.post(
    "/audio/")
async def ask_via_audio(
    user_id: int = Form(...), 
    conversation_id: int = Form(...), 
    file: UploadFile = File(...),
):
    return {"response": "Hello World"}
    
