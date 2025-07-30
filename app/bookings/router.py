from fastapi import APIRouter, FastAPI
from app.bookings.shema import SBookings
from .repo import BookingREPO



router = APIRouter(
    prefix="/bookings",
    tags=["бронирование"]
)


@router.get("")
async def get_bookings2()->list[SBookings]:
    return await BookingREPO.find_all()