from pydantic import BaseModel
from enum import Enum




class GenresUrlChoice(Enum):
    ROCK = "rock"
    PROGRESSIVE_ROCK = "progressive rock"
    METAL = "metal"
    HIP_HOP = "hip hop"


class Album(BaseModel):
    title: str
    release_year: int

    

class Band(BaseModel):
    id: int
    name: str
    genre: str
    albums: list[Album] = []