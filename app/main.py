from typing import Union
from fastapi import FastAPI, Request
from app.api.v1.endpoints import models, items, second,  third, fourth, fifth, sixth, seventh, stream

app = FastAPI()


# ルータの登録
app.include_router(models.router, prefix="/second", tags=["0614: パスパラメータ"])
app.include_router(models.router, prefix="/models", tags=["0614: パスパラメータ"])
app.include_router(items.router, prefix="/items", tags=["0621: クエリパラメータ"])
app.include_router(third.router, prefix="/third", tags=["0628: リクエストボディ"])
app.include_router(fourth.router, prefix="/fourth", tags=["0704: クエリパラメータと文字列の検証"])
app.include_router(fifth.router, prefix="/fifth", tags=["0711: パスパラメータと数値の検証"])
app.include_router(sixth.router, prefix="/sixth", tags=["0719: ボディ - 複数のパラメータ"])
app.include_router(seventh.router, prefix="/seventh", tags=["0719: ボディ -フィールドとバリデーション"])
app.include_router(stream.router, prefix="/stream", tags=["0730: ストリーミング"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


