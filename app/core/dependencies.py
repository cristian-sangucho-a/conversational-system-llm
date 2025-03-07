from app.core.database import Session

async def get_db():
    async with Session() as session:
        yield session