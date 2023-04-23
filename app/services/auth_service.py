from app.models import User
from app.configs import db
from fastapi.encoders import jsonable_encoder
from app.models import User

class AuthService:
    def __init__(self):
        pass


    async def get_user(self,username: str) -> User:
        user = await db["user"].find_one({"username": username})
        if user:
            return User(**user)





