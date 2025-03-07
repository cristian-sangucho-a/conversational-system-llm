from fastapi import APIRouter, status, Form, Depends
from schemas.conversation import Conversation
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import get_db
from services.conversation_service import ConversationService

conversation_router = APIRouter(tags=["Conversation Endpoints"])

@conversation_router.post(
    "/create/",
    status_code=status.HTTP_200_OK,
    response_model=Conversation,
    responses={
        200: {
            "description": "Conversation created successfully",
        },
        400: {"description": "Bad request"},
        500: {"description": "Internal server error."}
    })
async def create_conversation(conversation: Conversation = Form(...), db: AsyncSession = Depends(get_db)) -> Conversation:
    conversation_service = ConversationService(db)
    return await conversation_service.create_conversation(conversation)
