from fastapi import FastAPI, Request
from app.api.v1.endpoints import models

app = FastAPI()


# ルータの登録
app.include_router(models.router, prefix="/models", tags=["items"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


@app.options("/example/options")
async def options_example():
    return {"methods": ["GET", "POST", "OPTIONS"]}


@app.head("/example/head")
async def head_example():
    return {"message": "This is the header of the resource"}


@app.trace("/example/trace")
async def trace_example(request: Request):
    return {"request": request}

