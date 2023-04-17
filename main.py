from typing import Union
from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from pathlib import Path

# import environment variables
dotenv_path = Path('.env.local')
load_dotenv(dotenv_path=dotenv_path)


from configs.database import db


app = FastAPI()
@app.get('/')
def root():
    return {"Hello":"World"}



if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)
