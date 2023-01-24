from fastapi import FastAPI

import api_sample.routers.sample


class SampleAPIApp:

    @staticmethod
    def setup_router() -> FastAPI:
        app = FastAPI()
        app.include_router(api_sample.routers.sample.router)
        return app
