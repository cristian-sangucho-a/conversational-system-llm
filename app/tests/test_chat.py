# tests/test_chat.py
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from io import BytesIO
from app.main import app  
from fastapi import File
client = TestClient(app)

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from io import BytesIO
import tempfile
import os

@pytest.mark.asyncio
async def test_ask_via_audio_success():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(b"fake_audio_response")
        temp_audio_path = temp_audio.name

    try:
        audio_file = BytesIO(b"fake_audio_data")
        audio_file.name = "test_audio.mp3"

        with patch("routers.chat_router.AskViaAudioService") as mock_service:
            mock_instance = mock_service.return_value
            # Mock devuelve la ruta del archivo temporal
            mock_instance.model_response_via_audio = AsyncMock(return_value=temp_audio_path)
            
            response = client.post(
                "/chat/audio/",
                data={"user_id": 1, "conversation_id": 1},
                files={"file": ("test_audio.mp3", audio_file, "audio/mpeg")}
            )

        assert response.status_code == status.HTTP_200_OK
        assert response.headers["content-type"] == "audio/mpeg"
    finally:
        os.remove(temp_audio_path)

@pytest.mark.asyncio
async def test_ask_via_audio_invalid_format():
    # Simula un archivo no-audio
    text_file = BytesIO(b"fake_text_data")
    text_file.name = "test.txt"

    response = client.post(
        "/chat/audio/",
        data={"user_id": 1, "conversation_id": 1},
        files={"file": ("test.txt", text_file, "text/plain")}
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    
@pytest.mark.asyncio
async def test_ask_via_text_success():
    test_data = {
        "user_id": 1,
        "conversation_id": 1,
        "message": "Hola"
    }

    with patch("routers.chat_router.AskViaTextService") as mock_service:
        mock_instance = mock_service.return_value
        # Respuesta anidada bajo "response"
        mock_instance.model_response_via_text = AsyncMock(return_value={"response": "Hola, ¿cómo estás?"})

        response = client.post("/chat/text/", json=test_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"response": "Hola, ¿cómo estás?"}
    
@pytest.mark.asyncio
async def test_ask_via_text_validation_error():
    test_data = {"invalid_field": "data"}  
    response = client.post("/chat/text/", json=test_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY