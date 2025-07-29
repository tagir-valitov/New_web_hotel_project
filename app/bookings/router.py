from fastapi import APIRouter, FastAPI
from sqlalchemy import select
from app.database import async_session_maker
from app.bookings.models import Bookings


router = APIRouter(
    prefix="/bookings",
    tags=["бронирование"]
)


@router.get("/{booking_id}")
async def get_bookings2():
    async with async_session_maker() as session:
        query = select(Bookings)
        result = await session.execute(query)
        print(result.all())
