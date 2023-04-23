from pydantic import BaseModel,Field, EmailStr
from bson import ObjectId
from typing import Optional, List, Union
from app.utils.custom_types import PyObjectId

class UserBase(BaseModel):
    fullname: Optional[str] = Field(...)
    username: str = Field(...)
    hashed_password: str = Field(...)
    disabled: Union[bool, None] = None


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fullname":"test",
                "username": "Jane Doe",
                "hashed_password": "",
            }
        }

class UserCreating(BaseModel):
    fullname: Optional[str]
    username: Optional[str]
    password: Optional[str]
    disabled: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fullname":"test",
                "username": "Jane Doe",
                "password": "",
            }
        }

class UserInput(UserBase):
    fullname: Optional[str]
    username: Optional[str]
    hashed_password: Optional[str]
    disabled: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fullname":"test",
                "username": "Jane Doe",
                "hashed_password": "",
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
                "fullname":"test",
                "id":{
                    "$oid": "643e78087beae247272083d2"
                },
                "username": "Jane Doe",
                "hashed_password": "",
            }
        }


class UserViewModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    username: Optional[str]
    disabled: Optional[bool]
    fullname: Optional[str]



    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fullname":"test",
                "id":{
                    "$oid": "643e78087beae247272083d2"
                },
                "username": "Jane Doe",
            }
        }
