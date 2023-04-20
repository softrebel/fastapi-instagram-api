from fastapi import FastAPI, Body, HTTPException, status,APIRouter

from app.models.ig import *
from app.utils.response import Response
from app.models import ResponseModel
from app.utils import InstagramHandler,LoginFailedException
router = APIRouter()

@router.post('/ig')
async def insert_ig_account(ig: IgInput = Body(...)) -> ResponseModel:
    try:

        ig_handler=InstagramHandler()
        ig_handler.login(ig.username,ig.password)


        item = Ig()
        item.username=ig_handler.username
        item.password=ig_handler.password
        item.session_id=ig_handler.session_id
        item.csrf_token=ig_handler.csrf_token
        item = jsonable_encoder(item)
        new_ig = await db["account"].insert_one(item)
        created_ig = await db["account"].find_one({"_id": new_ig.inserted_id})
        created_ig=IgViewModel(**created_ig)
        return Response.created(created_ig)

    except LoginFailedException as e:
        return Response.bad_request({},str(e))
    except Exception as e:
        return Response.server_error({},str(e))
@router.get('/ig')
async def get_ig_account():
    pass

@router.get('/ig/{id}')
async def get_ig_account_detail(id):
    pass
