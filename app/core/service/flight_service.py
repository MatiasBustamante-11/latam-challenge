from fastapi import HTTPException
from app.core.dto.flight_delay_dto import FlightDelayDto
from app.core.ml.flight_delay import ml_flight_delay

class FlightService:
    def prediction_delay(self,opera,tipo_vuelo,mes):
        predicted_value,predicted_prob_no_delay,predicted_prob_delay=ml_flight_delay.predict_pipeline_delay(opera,tipo_vuelo,mes)
        predicted_values=FlightDelayDto(predicted_value,predicted_prob_no_delay,predicted_prob_delay)
        return predicted_values.__dict__
 
flight_service:object = FlightService()
 