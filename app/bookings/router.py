from fastapi import APIRouter, FastAPI
from .repo import BookingREPO



router = APIRouter(
    prefix="/bookings",
    tags=["бронирование"]
)


@router.get("")
async def get_bookings2():
    return await BookingREPO.find_all()