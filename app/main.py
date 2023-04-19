from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.router.flight_router import flight_router
from app.core.config import settings

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME,version=1)
    _app.include_router(flight_router.router)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


app = get_application()
