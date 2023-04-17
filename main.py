from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return {"Hello":"World"}



if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)
