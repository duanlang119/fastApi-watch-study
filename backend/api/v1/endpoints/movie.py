from fastapi import APIRouter

movie = APIRouter(tags=["电影相关"])

@movie.get("/movie", summary="电影列表")
async def movie_list():
    pass

@movie.post("/movie", summary="新增电影")
async def movie_create():
    pass


@movie.put("/movie", summary="编辑电影")
async def movie_update():
    pass

@movie.delete("/movie", summary="删除电影")
async def movie_delete():
    pass