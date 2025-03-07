import os
from tempfile import NamedTemporaryFile
import speech_recognition as sr
from fastapi import UploadFile, HTTPException

async def speech_to_text(file: UploadFile) -> str:
    # Read the uploaded file
    audio_data = await file.read()
    if not audio_data:
        raise HTTPException(400, detail="Empty audio file")
    
    content_type = file.content_type
    if 'wav' not in content_type.lower():
        raise HTTPException(400, detail="Only WAV files are supported. Please convert your audio to WAV format.")
    # create temp file
    with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(audio_data)
        temp_file_path = temp_file.name
    
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='es-ES')
        return text
    finally:
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)



