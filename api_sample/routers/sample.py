from typing import Dict

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter()


@cbv(router)
class SampleRouter:

    def __init__(self):
        self._res_value: str = 'hello'
        self._res_message: Dict[str, str] = {"message": "updated."}

    @router.get('/hello')
    async def hello(self) -> str:
        return self._res_value

    @router.post("/update")
    async def update(self) -> Dict[str, str]:
        return self._res_message
