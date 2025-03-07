from models.conversation import Conversation

class ConversationRepository:
    def __init__(self, db):
        self.db = db

    async def create_conversation(self, conversation: Conversation) -> Conversation:
        new_conversation = Conversation(
            user_id=conversation.user_id,
            title=conversation.title
        )
        self.db.add(new_conversation)
        await self.db.commit()
        await self.db.refresh(new_conversation)
        return new_conversation

    