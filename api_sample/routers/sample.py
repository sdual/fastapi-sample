from typing import Dict

from fastapi import APIRouter

# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter()


@router.get('/hello')
async def hello() -> str:
    return 'hello'


@router.post("/update")
async def update() -> Dict[str, str]:
    return {"message": "updated."}
