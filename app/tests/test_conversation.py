# tests/test_conversation_endpoints.py
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_conversation_success():
    test_data = {
        "user_id": 1,
        "title": "Test Conversation"
    }
    
    with patch("routers.conversation_router.ConversationService") as mock_service:
        mock_instance = mock_service.return_value
        mock_instance.create_conversation = AsyncMock(return_value={
            "id": 1,
            "user_id": 1,
            "title": "Test Conversation"
        })
        
        response = client.post(
            "/conversation/create/",
            data=test_data 
        )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "user_id": 1,
        "title": "Test Conversation"
    }