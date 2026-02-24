from fastapi import FastAPI, HTTPException
from schema import GenresUrlChoice, Band



app = FastAPI()
BANDS = [
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Led Zeppelin", "genre": "Rock"},
    {"id": 3, "name": "Pink Floyd", "genre": "Progressive Rock", "albums": [{"title": "The Dark Side of the Moon", "release_year": 1973}]}, 
    {"id": 4, "name": "Queen", "genre": "Rock"}

]

@app.get('/bands')
async def index(genre: GenresUrlChoice | None = None) -> list[Band]:
    if genre:
        return [
            Band(**band) for band in BANDS if band["genre"].lower() == genre.value.lower()
        ]
    return [Band(**band) for band in BANDS]


@app.get('/bands/{band_id}') 
async def get_band(band_id: int) -> Band:
    band = next((band for band in BANDS if band["id"] == band_id), None)
    if band:
        return Band(**band)
    raise HTTPException(status_code=404, detail="Band not found")


@app.get('/bands/genre/{genre}')
async def get_bands_by_genre() -> list[dict]:
    genre = [band for band in BANDS if band["genre"].lower() == genre.value.lower()]
    if genre:
        return genre
    raise HTTPException(status_code=404, detail="Genre not found")
