from pydantic import BaseModel

class UserBase(BaseModel):
    pass


class UserInput(UserBase):
    pass

class User(UserBase):
    pass

