from sqlalchemy import Column, BIGINT, ForeignKey, String
from sqlalchemy.orm import relationship
from core.database import Base

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey("users.id"))
    title = Column(String(255))
    
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")