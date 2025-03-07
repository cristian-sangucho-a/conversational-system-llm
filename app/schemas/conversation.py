from pydantic import BaseModel, Field

class Conversation(BaseModel):
    user_id: int = Field(
        ...,
        description="Unique user identifier",
        example=123
    )
    title: str = Field(
        ...,
        description="title of conversation",
        example="Talk about the weather"
    )

    class Config:
        from_attributes = True
