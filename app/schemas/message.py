from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        description="User input message"
    )
    user_id: int = Field(
        ...,
        description="Unique user identifier",
        example=123
    )
    conversation_id: int = Field(
        ...,
        description="Unique conversation identifier",
        example=456
    )
    
class ChatResponse(BaseModel):
    response: str = Field(
        ...,
        description="Respuesta generada por el modelo",
    )