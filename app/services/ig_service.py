from app.models import User
from app.configs import db
from fastapi.encoders import jsonable_encoder
from app.models.ig import Ig,IgViewModel

class IgService:
    def __init__(self):
        pass

    async def create_ig_account(self, ig:Ig) -> IgViewModel:
        item = jsonable_encoder(ig)
        new_ig = await db["account"].insert_one(item)
        created_ig = await db["account"].find_one({"_id": new_ig.inserted_id})
        created_ig=IgViewModel(**created_ig)
        return created_ig

    async def get_ig_account(self,ig_id:str) -> Ig:
        ig = await db["account"].find_one({"_id": ig_id})
        if ig:
            return Ig(**ig)
