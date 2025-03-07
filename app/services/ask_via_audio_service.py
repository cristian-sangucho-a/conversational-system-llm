from fastapi import UploadFile
from fastapi.responses import FileResponse
from services.stt_service import speech_to_text
from services.tts_service import text_to_speech
from sqlalchemy.ext.asyncio import AsyncSession

from services.chat_service import ChatService

class AskViaAudioService:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def model_response_via_audio(self, file: UploadFile, user_id: int, conversation_id: int) -> FileResponse:
        # proccess the audio file and convert it to text
        message_in_text = await speech_to_text(file)
        
        # use chat service
        chat_service = ChatService(self.db)
        response_of_model = await chat_service.chat(message_in_text, user_id, conversation_id)
        
        # convert the response to audio
        audio_response_path = await text_to_speech(str(response_of_model))

        responsefile = FileResponse(
        path=audio_response_path,
        media_type="audio/mpeg",
        filename="response.mp3"
        )
        return responsefile
        
        
