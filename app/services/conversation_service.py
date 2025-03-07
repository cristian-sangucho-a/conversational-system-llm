from schemas.conversation import Conversation
from repositories.conversation_repository import ConversationRepository
class ConversationService:
    def __init__(self, db):
        self.conversation_repository = ConversationRepository(db)

    async def create_conversation(self, conversation: Conversation) -> Conversation:
        orm_conversation = await self.conversation_repository.create_conversation(conversation)
        return Conversation.from_orm(orm_conversation) 