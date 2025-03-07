from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(
        ...,
        title="Name of the user", 
        description="Name of the user"
    )
    id: int | None = None

    class Config:
        from_attributes = True
