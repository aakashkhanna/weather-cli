from datetime import datetime
from unicodedata import decimal
from pydantic import BaseModel
from decimal import Decimal

class CurrentWeather(BaseModel):
    time: datetime
    temperature: Decimal
    weathercode: int
    windspeed: Decimal
    winddirection: int