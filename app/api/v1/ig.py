from fastapi import FastAPI, Body, HTTPException, status,APIRouter
from fastapi.encoders import jsonable_encoder
from app.configs import db
from app.models.ig import *
from app.utils.response import Response
from app.models import ResponseModel
from app.utils import InstagramHandler,LoginFailedException
router = APIRouter()

@router.post('/ig')
async def login_ig_account(ig: IgInput = Body(...)) -> ResponseModel:
    try:
        item = Ig(username=ig.username,
                cookies={})
        ig_handler=InstagramHandler()
        ig_handler.login(ig.username,ig.password)


        item = Ig(username=ig.username,
                cookies=ig_handler.cookies)
        item = jsonable_encoder(item)
        new_ig = await db["account"].insert_one(item)
        created_ig = await db["account"].find_one({"_id": new_ig.inserted_id})
        created_ig=IgViewModel(**created_ig)
        return Response.created(created_ig)

    except LoginFailedException as e:
        return Response.bad_request({},str(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on insert ig account")
@router.get('/ig/{username}/id/{id}/followers')
async def get_ig_followers(username:str,id:str):
    try:
        ig = await db["account"].find_one({"_id": id})
        if not ig:
            raise HTTPException(status_code=400, detail="instagram id not exists.")
        followers={}
        ig_handler=InstagramHandler()
        ig_handler.cookies=ig['cookies']
        followers=ig_handler.get_followers(username)
        return Response.ok(followers)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on getting follower")



