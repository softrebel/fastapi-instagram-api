from typing import Union
from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from pathlib import Path
from app.api.v1 import auth,user


# import environment variables
dotenv_path = Path('.env.local')
load_dotenv(dotenv_path=dotenv_path)

app = FastAPI()


app.include_router(auth.router, prefix="/v1")
app.include_router(user.router, prefix="/v1")


@app.get('/')
def root():
    return {"Hello":"World"}



if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)
