from typing import Union
from fastapi import FastAPI, Request
from app.api.v1.endpoints import models, items, third, fourth

app = FastAPI()


# ルータの登録
app.include_router(models.router, prefix="/models", tags=["items"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(third.router, prefix="/third", tags=["0627"])
app.include_router(fourth.router, prefix="/fourth", tags=["0704"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/{user_id}/items/{item_id}")
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


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     return {"item_id": item_id}


@app.options("/example/options")
async def options_example():
    return {"methods": ["GET", "POST", "OPTIONS"]}


@app.head("/example/head")
async def head_example():
    return {"message": "This is the header of the resource"}


@app.trace("/example/trace")
async def trace_example(request: Request):
    return {"request": request}

