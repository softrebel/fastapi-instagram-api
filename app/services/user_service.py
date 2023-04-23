from app.models import User
from app.configs import db
from fastapi.encoders import jsonable_encoder
from app.models.user import User,UserInput,UserViewModel

class UserService:
    def __init__(self):
        pass

    async def get_user(self, id: int) -> User:
        users = await db["user"].find_one({"_id": id})
        return User(**users)

    async def create_user(self, user:UserInput) -> UserViewModel:
        item = jsonable_encoder(user)
        new_user = await db["user"].insert_one(item)
        created_user = await db["user"].find_one({"_id": new_user.inserted_id})
        created_user=UserViewModel(**created_user)
        return created_user

