from fastapi import FastAPI
from HTTPException import HTTPException

app = FastAPI()
BANDS = [
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Led Zeppelin", "genre": "Rock"},
    {"id": 3, "name": "Pink Floyd", "genre": "Progressive Rock"},
    {"id": 4, "name": "Queen", "genre": "Rock"}

]
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
async def get_bands_by_genre(genre: str) -> list:
    genere = next((band for band in BANDS if band["genre"].lower() == genre.lower()), None)
    if genere:
        return genere
    raise HTTPException(status_code=404, detail="Genre not found")
