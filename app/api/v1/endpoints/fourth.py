from typing import Union, List
from fastapi import FastAPI, APIRouter, Query
from pydantic import BaseModel, Field

router = APIRouter()


# # Fieldを使うことで追加のバリデーションを入れることができる
# class User(BaseModel):
#     # ...で必須にできる
#     name: str = Field(..., min_length=1, max_length=10)
#     age: int = Field(..., ge=0, le=120)
#
#
# @router.post("/")
# async def create_user(user: User):
#     return user


@router.get("/validation")
async def vali_items(q: Union[str, None] = Query(
    # ここでバリデーションを設定できる
    default=None, max_length=10
)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/required")
# async def req_items(q: str = Query(..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/lists")
async def list_items(q: Union[List[str]] = Query(default=None)):
    query_items = {"q": q}
    return query_items


@router.get("/lists/failed")
async def list_items(q: Union[List[str]] = None):
    query_items = {"q": q}
    return query_items


@router.get("/meta")
async def meta_items(
        q: Union[str, None] = Query(
            default=None,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results