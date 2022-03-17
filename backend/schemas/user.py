from backend.models import User
from tortoise.contrib.pydantic import pydantic_model_creator


#返回
User_Pydantic=pydantic_model_creator(User,name="User",exclude=['password'])
UserIn_Pydantic=pydantic_model_creator(User,name="UserIn",exclude_readonly=True)