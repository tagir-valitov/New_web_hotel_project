from fastapi import FastAPI, Query, Depends
import uvicorn
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from .bookings.router import router as router_bookings
app = FastAPI()
app.include_router(router_bookings)

class HotelSearchArgs:
    def __init__(self,
                 date_from: date,
                 date_to: date,
                 location: str,
                 stars: Optional[int] = Query(None, ge=1, le=5),
                 has_spa: Optional[bool] = None
    ):
        self.location = location
        self.date_from = date_from
        self. date_to = date_to
        self.stars = stars
        self.has_spa = has_spa

class SHotels(BaseModel):# валидация данных
    address: str
    name: str
    stars: int
    has_spa: bool

@app.get("/hotels") #это гет запрос после которого мы должны вернуть пользователю то что он хочет
def get_hotels(search_args: HotelSearchArgs = Depends()) :
    return search_args


class SBooking(BaseModel): # мы воледируем данные добавляя их в функцию которая скорее всего передаст их в базу данных
    room_id: int
    date_from: date
    date_to: date
    prise: int
@app.post("/booking")
def add_booking(booking: SBooking):
    pass






if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
