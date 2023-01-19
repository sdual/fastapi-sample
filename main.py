import traceback

import uvicorn
from fastapi import FastAPI

import api_sample.routers.sample


def run_api():
    app = FastAPI()
    app.include_router(api_sample.routers.sample.router)
    return app


if __name__ == '__main__':
    try:
        uvicorn.run(run_api, port=5000, log_level='info') # uvicorn 以外の web server 使ってる場合はここは書き換える
    except:
        # logger を使って error log を出す
        traceback.print_exc()
