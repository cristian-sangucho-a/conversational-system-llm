from sqlalchemy import Column, BIGINT, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from core.database import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(BIGINT, primary_key=True, index=True)
    text = Column(Text)
    role = Column(String(255))
    conversation_id = Column(BIGINT, ForeignKey("conversations.id"))
    conversation = relationship("Conversation", back_populates="messages")
    