from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

app = FastAPI()


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: int = Query(default=None, ge=1, le=5),
            has_spa: bool = Query(default=None)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class SHotels(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels')
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    hotels = [
        {
            "address": 'Gagarina 1',
            "name": "SuperHotel",
            'stars': 5,
        }
    ]
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: SBooking):
    pass
