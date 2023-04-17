from pydantic import BaseModel,Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from app.utils.custom_types import PyObjectId

class IgBase(BaseModel):
    account: str = Field(...)
    password: str = Field(...)
    cookie: str = Field(...)
    user_id: PyObjectId = Field(default_factory=PyObjectId)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "account": "Jane Doe",
                "password": "",
                "cookie": "",
                "user_id": "",
            }
        }



class IgInput(IgBase):
    account: Optional[str]
    password: Optional[str]
    cookie: Optional[str]
    user_id: Optional[PyObjectId]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "account": "Jane Doe",
                "password": "",
                "cookie": "",
                "user_id": "",
            }
        }

class Ig(IgBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
