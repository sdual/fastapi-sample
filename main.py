import traceback

import uvicorn
from fastapi import FastAPI

from api_sample.server import APIServer


def run_api() -> FastAPI:
    return APIServer.run()


if __name__ == '__main__':
    try:
        uvicorn.run(run_api, port=8000, log_level='info')  # uvicorn 以外の web server 使ってる場合はここは書き換える
        # FastAPI での logger の設定がどうであれ、それに関係なく web server 側に渡されてしまうらしい。
        # logger の設定は web server 側で行い、例えば uvicorn の場合は
        # uvicorn.run(app, host="0.0.0.0", port=5000, log_config=[設定ファイルへのpath])
        # のように設定できるらしい
    except:
        # logger を使って error log を出す
        traceback.print_exc()
