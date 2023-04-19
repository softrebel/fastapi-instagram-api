from fastapi import APIRouter
from fastapi import FastAPI, Body, HTTPException, status
from app.models.user import UserInput,User,UserViewModel,UserCreating
from app.services.user_service import UserService
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse
from app.utils import Response
from app.models import ResponseModel
from app.configs.authentication import *

service=UserService()
router = APIRouter()

from app.configs.database import db

@router.post('/user', response_description="Add new user")
async def insert_user(user: UserCreating = Body(...)) -> ResponseModel :
    hashed_password=get_password_hash(user.password)
    item = UserInput(fullname=user.fullname,
    username=user.username,
    disabled=user.disabled,
    hashed_password=hashed_password
    )
    item = jsonable_encoder(item)
    new_user = await db["user"].insert_one(item)
    created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # created_user = await service.create_user(user)
    created_user=UserViewModel(**created_user)
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
    return Response.created(created_user)

@router.get('/user')
async def get_user():
    pass

@router.get('/user/{id}')
async def get_user(id):
    pass
