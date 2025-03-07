from repositories.user_repository import UserRepository
from schemas.user import User
class UserService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    async def create_user(self, user):
        orm_user = await self.user_repository.create_user(user)
        return User(
            id=orm_user.id,
            username=orm_user.username
        )
    
    
