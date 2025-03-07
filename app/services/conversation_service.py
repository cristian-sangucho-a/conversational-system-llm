from schemas.conversation import Conversation
from repositories.conversation_repository import ConversationRepository
class ConversationService:
    def __init__(self, db):
        self.conversation_repository = ConversationRepository(db)

    async def create_conversation(self, conversation: Conversation) -> Conversation:
        orm_conversation = await self.conversation_repository.create_conversation(conversation)
        return Conversation(
            id=orm_conversation.id,
            title=orm_conversation.title,
            user_id=orm_conversation.user_id
        )