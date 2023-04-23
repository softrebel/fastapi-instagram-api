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
from app.utils.auth import *

@router.post('/user', response_description="Add new user")
async def insert_user(user: UserCreating = Body(...)) -> ResponseModel :
    try:
        hashed_password=get_password_hash(user.password)
        item = UserInput(fullname=user.fullname,
        username=user.username,
        disabled=user.disabled,
        hashed_password=hashed_password
        )
        created_user = await service.create_user(item)
        return Response.created(created_user)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on insert user")

