from sqlalchemy import Column, BIGINT, String
from sqlalchemy.orm import relationship
from core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(BIGINT, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    
    conversations = relationship("Conversation", back_populates="user")