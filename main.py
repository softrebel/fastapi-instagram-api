from typing import Union
from fastapi import FastAPI,Depends
import uvicorn
import os

from app.api.v1 import auth,user,ig

from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

# import environment variables


app = FastAPI()


app.include_router(auth.router, prefix="/v1")
app.include_router(user.router, prefix="/v1")
app.include_router(ig.router, prefix="/v1")



@app.get('/')
def root():
    return {"Hello":"World"}





if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)
