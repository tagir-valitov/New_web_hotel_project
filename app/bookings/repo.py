from sqlalchemy import select
from .models import Bookings
from ..database import async_session_maker
from ..repo.base import BaseRepo



class BookingREPO(BaseRepo):
    model = Bookings
   


