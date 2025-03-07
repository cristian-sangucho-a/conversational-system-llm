from sqlalchemy.ext.asyncio import AsyncSession
from services.chat_service import ChatService
from schemas.message import ChatRequest, ChatResponse

class AskViaTextService:
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def model_response_via_text(self, chat_request: ChatRequest) -> ChatResponse:
        
        # use chat service
        chat_service = ChatService(self.db)
        response_of_model = await chat_service.chat(chat_request.message, chat_request.user_id, chat_request.conversation_id)
        
        return ChatResponse(response=response_of_model)
        