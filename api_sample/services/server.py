from fastapi import FastAPI

import api_sample.routers.sample


class APIServer:

    @staticmethod
    def run() -> FastAPI:
        app = FastAPI()
        app.include_router(api_sample.routers.sample.router)
        return app
