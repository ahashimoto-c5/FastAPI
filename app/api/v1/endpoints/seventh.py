import re
from typing import Union
from fastapi import Body, FastAPI, APIRouter
from pydantic import BaseModel, Field, validator

router = APIRouter()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

    @validator('name')
    def name_must_not_contain_special_chars(cls, v):
        if not re.match("^[a-zA-Z0-9]+$", v):
            raise ValueError('Name must be alphanumeric')
        return v

    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v


@router.put("/{item_id}")
# embed=True の記述によって、ボディにitemのキーが必要になる
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
