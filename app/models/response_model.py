from pydantic import BaseModel

class ResponseModel(BaseModel):
    message:str
    data:dict
    status:int = 200

