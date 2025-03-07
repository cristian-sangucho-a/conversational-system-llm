from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.message import Message

class MessageRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_messages_by_conversation(self, conversation_id: int):
        result = await self.db.execute( 
                select(Message)
                .where(Message.conversation_id == conversation_id)
            )
        return result.scalars().all()

    async def save_request_message(self, text: str, role: str, conversation_id: int) -> Message:
            message = Message(
                text=text,
                role=role,
                conversation_id=conversation_id
            )
            self.db.add(message)
            await self.db.commit()
            await self.db.refresh(message)
            return message
    