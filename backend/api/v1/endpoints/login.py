from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from backend.core import verify_password
from backend.core.security import create_access_token
from backend.models import User
from backend.schemas import UserIn_Pydantic, ResponseToken, Response400, Response200, User_Pydantic

login = APIRouter(tags=["认证相关"])

@login.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if user := await User.get(username=form_data.username):
        if verify_password(form_data.password,user.password):
            token = create_access_token({"sub":user.username})
            return ResponseToken(data={"token":f"bearer {token}"},access_token=token)
        return Response400(msg="账号或密码错误")


@login.post("/user", summary="用户新增")
async def user_create(user: UserIn_Pydantic):

    return Response200(data=await User_Pydantic.from_tortoise_orm(await User.create(**user.dict())))
