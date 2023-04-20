from fastapi import APIRouter
from app.core.config import settings

class HealthCheckRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/health-check",self.flight_prediction,methods=["GET"])
    def flight_prediction(self):
        return {"status":"Ml app is up","model_version": settings.MODEL_VERSION}
        
health_check_router:object = HealthCheckRouter()