from fastapi import FastAPI, HTTPException
from enum import Enum


app = FastAPI()
BANDS = [
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Led Zeppelin", "genre": "Rock"},
    {"id": 3, "name": "Pink Floyd", "genre": "Progressive Rock"},
    {"id": 4, "name": "Queen", "genre": "Rock"}

]

class GenreUrlChoice(Enum):
    ROCK = "rock"
    PROGRESSIVE_ROCK = "progressive rock"
    METAL = "metal"
    HIP_HOP = "hip hop"


@app.get('/bands')
async def index() -> list:
    return BANDS


@app.get('/bands/{band_id}') 
async def get_band(band_id: int) -> dict:
    band = next((band for band in BANDS if band["id"] == band_id), None)
    if band:
        return band
    raise HTTPException(status_code=404, detail="Band not found")


@app.get('/bands/genre/{genre}')
async def get_bands_by_genre(genre: GenreUrlChoice) -> list[dict]:
    genre = [band for band in BANDS if band["genre"].lower() == genre.value.lower()]
    if genre:
        return genre
    raise HTTPException(status_code=404, detail="Genre not found")

