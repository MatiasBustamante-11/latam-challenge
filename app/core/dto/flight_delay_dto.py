class FlightDelayDto:
    def __init__(self,predicted_value:float,predicted_prob_no_delay:float,predicted_prob_delay:float):
        self.predicted_value=predicted_value
        self.predicted_prob_no_delay=predicted_prob_no_delay
        self.predicted_prob_delay=predicted_prob_delay