from datetime import datetime
from unicodedata import decimal
from pydantic import BaseModel
from decimal import Decimal

class Config(BaseModel):
    latitude: Decimal
    longitude: Decimal