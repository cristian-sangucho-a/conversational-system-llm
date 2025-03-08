# tests/test_user_endpoints.py
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_user_success():
    test_data = {
        "username": "testuser",
    }
    
    with patch("routers.user_router.UserService") as mock_service:
        mock_instance = mock_service.return_value
        mock_instance.create_user = AsyncMock(return_value={"id": 1, **test_data})
        
        response = client.post(
            "/user/create/",
            data=test_data
        )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 1, "username": "testuser"}

