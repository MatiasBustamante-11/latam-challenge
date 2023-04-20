from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.core.exception.validation_errors import validation_exception_handler
from app.core.router.flight_router import flight_router
from app.core.config import settings
from app.core.router.health_check import health_check_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME,version=1)
    _app.exception_handler(RequestValidationError)(validation_exception_handler)
    _app.include_router(health_check_router.router)
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
