from typing import Dict

from fastapi import APIRouter

# https://fastapi.tiangolo.com/tutorial/bigger-applications/

sample_router = APIRouter()


@sample_router.get('/hello')
async def hello() -> str:
    return 'hello'


@sample_router.post("/update")
async def update() -> Dict[str, str]:
    return {"message": "updated."}
