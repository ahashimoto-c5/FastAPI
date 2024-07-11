from typing import Union
from fastapi import FastAPI, Path, Query, APIRouter

router = APIRouter()


@router.get("/default/{item_id}")
async def default(
        item_id: int = Path(title="The ID of the item to get"),
        q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@router.get("/required/{item_id}")
async def required(
        q: str,
        item_id: int = Path(title="The ID of the item to get"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
