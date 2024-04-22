from prostopay.task_2.db import get_async_session, DATABASE_URL
from prostopay.task_2.models import UserDTO, User


class UserService:
    def __init__(self, db_url: str = DATABASE_URL):
        self.session = get_async_session(db_url)

    async def get(self, user_id: int) -> UserDTO:
        async with self.session() as session:
            user = await session.get(User, user_id)
            if user:
                return UserDTO.from_orm(user)
            else:
                return None

    async def add(self, user: UserDTO) -> None:
        async with self.session() as session:
            new_user = User(**user.dict())
            session.add(new_user)
            await session.commit()