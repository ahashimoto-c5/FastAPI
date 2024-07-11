from typing import Union, List
from fastapi import FastAPI, APIRouter, Request
from pydantic import BaseModel, Field

router = APIRouter()


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@router.options("/example/options")
async def options_example():
    return {"methods": ["GET", "POST", "OPTIONS"]}


@router.head("/example/head")
async def head_example():
    return {"message": "This is the header of the resource"}


@router.trace("/example/trace")
async def trace_example(request: Request):
    return {"request": request}

