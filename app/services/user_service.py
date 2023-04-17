from app.models import User
from app.configs import db
from fastapi.encoders import jsonable_encoder
from app.models.user import User,UserInput

class UserService:
    def __init__(self):
        pass

    async def get_user(self, id: int) -> User:
        users = await db["user"].find().to_list()
        return users

    async def create_user(self, user:UserInput) -> User:
        new_user = await db["user"].insert_one(user)
        created_user = await db["user"].find_one({"_id": new_user.inserted_id})
        return User(**created_user)

    def login(self,username:str,password:str) -> User:
        pass

    def register(self,input:UserInput) -> User:
        pass

