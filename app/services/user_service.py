from app.models import User
from app.configs import db

class UserService:
    def __init__(self):
        self.session = Session()

    def get_my_model(self, id: int) -> User:
        return self.session.query(MyModel).filter(MyModel.id == id).first()

    def create_my_model(self, data: dict) -> User:
        my_model = MyModel(**data)
        self.session.add(my_model)
        self.session.commit()
        return my_model

    def login(self,username:str,password:str) -> User:
        pass

    def register(self,input:UserInput) -> User:
        pass

