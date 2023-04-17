from fastapi import APIRouter
from fastapi import FastAPI, Body, HTTPException, status
from app.models.user import UserInput,User
from app.services.user_service import UserService
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response, JSONResponse


service=UserService()
router = APIRouter()

from app.configs.database import db

@router.post('/user', response_description="Add new user", response_model=User)
async def insert_user(user: UserInput = Body(...)):
    user = jsonable_encoder(user)
    new_user = await db["user"].insert_one(user)
    created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    # created_user = await service.create_user(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)

@router.get('/user')
async def get_user():
    pass

@router.get('/user/{id}')
async def get_user(id):
    pass
