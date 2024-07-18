from typing import Union
from fastapi import FastAPI, Path, Query, APIRouter, Body
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@router.put("/{item_id}")
async def update_item(
        *,
        item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
        q: Union[str, None] = Query(
            description="Path, Query, リクエストボディを合わせて使う",
        ),
        item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        # クエリがあればクエリを追加
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@router.put("/item_user/{item_id}")
async def update_item_user(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@router.put("/importance/{item_id}")
async def add_importance(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@router.put("/query/{item_id}")
async def query_importance(
    *,
    item_id: int,
    item: Item,
    user: User,
    # リクエストボディになる
    importance: int = Body(gt=0),
    # クエリパラメータになる
    q: Union[str, None] = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
