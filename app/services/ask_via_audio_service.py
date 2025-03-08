from fastapi import UploadFile
from fastapi.responses import FileResponse
from services.stt_service import speech_to_text
from services.tts_service import text_to_speech
from sqlalchemy.ext.asyncio import AsyncSession

from services.chat_service import ChatService

class AskViaAudioService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.DEFAULT_MEDIA_TYPE = "audio/mpeg"
        self.DEFAULT_FILE_NAME = "response.mp3"
        
        
    async def model_response_via_audio(self, file: UploadFile, user_id: int, conversation_id: int, language: str) -> FileResponse:
        # proccess the audio file and convert it to text
        message_in_text = await speech_to_text(file, language)
        
        # use chat service
        chat_service = ChatService(self.db)
        response_of_model = await chat_service.chat(message_in_text, user_id, conversation_id)
        
        # convert the response to audio
        audio_response_path = await text_to_speech(text=str(response_of_model), languaje=language)

        responsefile = FileResponse(
        path=audio_response_path,
        media_type=self.DEFAULT_MEDIA_TYPE,
        filename=self.DEFAULT_FILE_NAME
        )
        return responsefile
        
        
