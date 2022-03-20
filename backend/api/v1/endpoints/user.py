from fastapi import APIRouter, Depends

from backend.core import deps
from backend.models import User
from backend.schemas import User_Pydantic,UserIn_Pydantic

user = APIRouter(tags=["用户相关"],dependencies=[Depends(deps.get_current_user)])

@user.get("/user", summary="当前用户")
async def user_info(user_obj: User = Depends(deps.get_current_user)):
    return await User_Pydantic.from_tortoise_orm(user_obj)

@user.put("/user", summary="修改信息")
async def user_update(user_form: UserIn_Pydantic,user_obj:User = Depends(deps.get_current_user)):
    if await User.filter(username=user_form.username).update(**user_form.dict()):
        return {"msg":"update"}
    return {"msg": "no update"}

__all__=[
    "user"
]