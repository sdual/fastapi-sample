from typing import Dict

from fastapi import APIRouter
from fastapi_utils.cbv import cbv

from api_sample.services import SampleRequester, SampleAPIConfig

# https://fastapi.tiangolo.com/tutorial/bigger-applications/
# https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/#the-cbv-decorator

router = APIRouter()


@cbv(router)
class SampleRouter:

    def __init__(self):
        self._res_value: str = 'hello'
        self._res_message: Dict[str, str] = {"message": "updated."}

        self._requester = SampleRequester(SampleAPIConfig().url)

    @router.get('/hello')
    async def hello(self) -> str:
        return self._res_value

    @router.post("/update")
    async def update(self) -> Dict[str, str]:
        return self._res_message

    @router.get('/user')
    async def api_proxy(self) -> str:
        user_id = 1
        res_json = self._requester.request(user_id)
        return res_json
