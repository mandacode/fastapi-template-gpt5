from fastapi import FastAPI

from app.api.v1.routes import router as api_router


def create_app() -> FastAPI:
    application = FastAPI(title="FastAPI Template", version="0.1.0")
    application.include_router(api_router, prefix="/api/v1")
    return application


app = create_app()
