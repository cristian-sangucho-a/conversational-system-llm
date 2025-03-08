from models.user import User
from sqlalchemy import select

class UserRepository:
    def __init__(self, db):
        self.db = db

    async def create_user(self, user: User) -> User:
        new_user = User(
            username=user.username
        )
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user
    
    async def get_username(self, user_id: int) -> str:
        result = await self.db.execute( 
                select(User.username)
                .where(User.id == user_id)
            )
        return result.scalar_one()