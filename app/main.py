from typing import Union
from fastapi import FastAPI, Request
from app.api.v1.endpoints import models, items, second,  third, fourth

app = FastAPI()


# ルータの登録
app.include_router(models.router, prefix="/second", tags=["0614: パスパラメータ"])
app.include_router(models.router, prefix="/models", tags=["0614: パスパラメータ"])
app.include_router(items.router, prefix="/items", tags=["0621: クエリパラメータ"])
app.include_router(third.router, prefix="/third", tags=["0628: リクエストボディ"])
app.include_router(fourth.router, prefix="/fourth", tags=["0704: クエリパラメータと文字列の検証"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


