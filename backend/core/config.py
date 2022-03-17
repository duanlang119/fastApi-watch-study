import secrets
from typing import Optional

from pydantic import BaseSettings

class Settings(BaseSettings):
    TITLE: Optional[str]="电影列表接口"
    DESC: Optional[str]="""
    - Hello Flask 的FastAPI实现
    """

    # JWT
    # token相关
    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3


settings = Settings()