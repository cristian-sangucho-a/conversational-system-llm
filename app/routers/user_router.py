from fastapi import APIRouter, Form, Depends, status
from schemas.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import get_db
from services.user_service import UserService

user_router = APIRouter(tags=["User Endpoints"])

@user_router.post(
    "/create/",
    status_code=status.HTTP_200_OK,
    response_model=User,
    responses={
        200: {
            "description": "Conversation created successfully",
        },
        400: {"description": "Bad request"},
        500: {"description": "Internal server error."}
    })
async def create_user(user: User = Form(...), db: AsyncSession = Depends(get_db)) -> User:
    conversation_service = UserService(db)
    return await conversation_service.create_user(user)
