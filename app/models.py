from pydantic import BaseModel, validator
from typing import List
from datetime import date, time


class Item(BaseModel):
    shortDescription: str
    price: str

    @validator("price")
    def validate_price(cls, price):
        try:
            float(price)
        except ValueError:
            raise ValueError("Price must be a numeric value")
        return price


class Receipt(BaseModel):
    retailer: str
    purchaseDate: date
    purchaseTime: time
    total: str
    items: List[Item]

    @validator("total")
    def validate_total(cls, total):
        try:
            float(total)
        except ValueError:
            raise ValueError("Total must be a numeric value")
        return total
