from typing import Dict

from fastapi import APIRouter

# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter()


class SampleRouter:

    @router.get('/hello')
    async def hello(self) -> str:
        return 'hello'

    @router.post("/update")
    async def update(self) -> Dict[str, str]:
        return {"message": "updated."}
