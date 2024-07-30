import asyncio
from fastapi import FastAPI, APIRouter, Query
from fastapi.responses import StreamingResponse
import time
import json

router = APIRouter()


def generate_large_file():
    for i in range(1, 1000):
        if i > 1:
            time.sleep(0.01)  # シミュレーションのため、各行の読み込みに遅延を追加
        yield f"Line {i}\n"


@router.get("/stream")
def stream_large_file():
    return StreamingResponse(generate_large_file(), media_type="text/plain")


@router.get("/stream-json")
async def stream_json_example():
    async def generate_json_data():
        for i in range(10):
            data = {"index": i, "message": f"Hello from index {i}"}
            await asyncio.sleep(1.0)
            yield f"data:{json.dumps(data)}\n\n"

    return StreamingResponse(content=generate_json_data(), media_type="text/event-stream")
