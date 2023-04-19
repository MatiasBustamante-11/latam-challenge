from pydantic import BaseModel

class MlSwaggerOutput(BaseModel):
    predicted_value:float
    predicted_prob_no_delay:float 
    predicted_prob_delay:float