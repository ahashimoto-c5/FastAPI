from typing import Union, List
from fastapi import FastAPI, APIRouter, Query
from pydantic import BaseModel

router = APIRouter()


# BaseModelを継承したクラスなので、データ型を定義できる
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@router.post("/")
async def create_item(item: Item):
    return item


@router.post("/dict")
async def dict_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict