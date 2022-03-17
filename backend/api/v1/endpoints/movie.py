from fastapi import APIRouter
from typing import List

from backend.models import Movie
from backend.schemas import Movie_Pydantic,MovieIn_Pydantic

movie = APIRouter(tags=["电影相关"])

@movie.get("/movie", summary="电影列表",response_model=List[Movie_Pydantic])
async def movie_list(limit:int=10,page:int=1):
    skip = (page-1)*limit
    return await Movie_Pydantic.from_queryset(Movie.all().offset(skip).limit(limit))

@movie.post("/movie", summary="新增电影",response_model=Movie_Pydantic)
async def movie_create(movie_form:MovieIn_Pydantic):
    return await Movie_Pydantic.from_tortoise_orm(await Movie.create(**movie_form.dict()))



@movie.put("/movie/{pk}", summary="编辑电影")
async def movie_update(pk:int, movie_form:MovieIn_Pydantic):
    if await Movie.filter(pk=pk).update(**movie_form.dict()):
        return {"msg":"update"}
    return {"msg":"update error"}


@movie.delete("/movie/{pk}", summary="删除电影")
async def movie_delete(pk:int, movie_form:MovieIn_Pydantic):
    if await Movie.filter(pk=pk).delete():
        return {"msg": "delete"}
    return {"msg": "delete error"}