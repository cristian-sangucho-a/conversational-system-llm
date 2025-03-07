from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        description="Mensaje de entrada del usuario"
    )
    user_id: int = Field(
        ...,
        description="Identificador único del usuario",
        example=123
    )
    conversation_id: int = Field(
        ...,
        description="Identificador único de la conversación",
        example=456
    )
    
class ChatResponse(BaseModel):
    response: str = Field(
        ...,
        description="Respuesta generada por el modelo",
    )