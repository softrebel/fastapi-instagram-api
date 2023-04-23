from datetime import datetime, timedelta
from typing import Union
from typing_extensions import Annotated
from fastapi import APIRouter
from app.models.user import UserViewModel,User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi import Depends, FastAPI, HTTPException, status
from app.services.auth_service import AuthService
from app.utils.auth import *

from app.configs import db

router = APIRouter()


async def authenticate_user(username: str, password: str) -> UserViewModel:
    service = AuthService()
    user = await service.get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    output = UserViewModel(id=user.id,
                           username=user.username,
                           disabled=user.disabled,
                           fullname=user.fullname)
    return output


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    service = AuthService()
    user = await service.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    output = UserViewModel(id=current_user.id,
                           username=current_user.username,
                           disabled=current_user.disabled,
                           fullname=current_user.fullname)
    return output


@router.post('/auth')
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}





@router.get("/auth/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> UserViewModel:
    return current_user
