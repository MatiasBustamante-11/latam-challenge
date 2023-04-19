from fastapi import HTTPException
from app.core.dto.flight_delay_dto import FlightDelayDto
from app.core.ml.flight_delay import ml_flight_delay

class FlightService:
    def prediction_delay(self,opera,tipo_vuelo,mes):
        return ml_flight_delay.predict_pipeline_delay(opera,tipo_vuelo,mes)
 
flight_service:object = FlightService()
 