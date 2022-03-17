from backend.models import Movie
from tortoise.contrib.pydantic import pydantic_model_creator

Movie_Pydantic=pydantic_model_creator(Movie,name="Movie")
MovieIn_Pydantic=pydantic_model_creator(Movie,name="MovieIn")