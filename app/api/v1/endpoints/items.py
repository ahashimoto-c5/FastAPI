from typing import Union, List
from fastapi import FastAPI, APIRouter, Query

router = APIRouter()

# ダミー辞書 = 連想配列
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/")
# skip: 返すアイテムの開始インデックスを指定します。デフォルトは0。
# limit: 返すアイテムの最大数を指定します。デフォルトは10。
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@router.get("/{item_id}")
# パスパラメータではない q は、クエリパラメータになる
# Unionで複数の型を持つことができる
async def read_item(item_id: str, q: Union[str, None] = None):
    # クエリパラメータがあればそれを出力する
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.get("/required")
async def required_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

