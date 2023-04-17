from pydantic import BaseModel,Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from app.utils.custom_types import PyObjectId

class UserBase(BaseModel):
    username: str = Field(...)
    password: str = Field(...)


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "Jane Doe",
                "password": "",
            }
        }


class UserInput(UserBase):
    account: Optional[str]
    password: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "Jane Doe",
                "password": "",
            }
        }

class User(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "Jane Doe",
                "password": "",
            }
        }
