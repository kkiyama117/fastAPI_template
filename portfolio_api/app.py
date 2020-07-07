import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from portfolio_api.core import config
from portfolio_api.db import connection
from portfolio_api.core import initializer
from portfolio_api.routes import v1_0


def create_app():
    # init settings. loaded when this file is loaded.
    application = FastAPI(
        title="portfolio_api API Project",
        description="This is a very fancy project, with auto docs for the API and everything",
        version="1.0.1",
    )

    @application.on_event("startup")
    async def startup():
        initializer.initialize()
        await connection.connect()

    @application.on_event("shutdown")
    async def shutdown():
        await connection.disconnect()

    # All allow for develop
    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        # expose_headers=["Access-Control-Allow-Origin"]
    )

    # major version change has no backward compatibility.
    # but minor has it.
    application.include_router(v1_0.router, prefix="/v1")
    return application


app = create_app()

# Alternative command to run
# you should run by `make start` or `make prod`
if __name__ == "__main__":
    uvicorn.run("portfolio_api.app:app", reload=True)
