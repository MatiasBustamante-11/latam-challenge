import pickle
import re
from pathlib import Path
import pandas as pd
from app.core.constants.ml_features import feature_headers


__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/finalized_model_logreg-{__version__}.pkl", "rb") as f:
    delay_pred_model = pickle.load(f)


class MlFlightDelay:
    def predict_pipeline_delay(self,opera,tipo_vuelo,mes):
        opera="OPERA_"+str(opera.value)
        mes="MES_"+str(mes)
        tipo_vuelo="TIPOVUELO_"+str(tipo_vuelo.value)

        feature_headers[opera] = feature_headers[opera].replace([0], 1)
        feature_headers[mes] = feature_headers[mes].replace([0], 1)
        feature_headers[tipo_vuelo] = feature_headers[tipo_vuelo].replace([0], 1)

        predicted_value,predicted_prob_no_delay,predicted_prob_delay=delay_pred_model.predict(feature_headers)[0],delay_pred_model.predict_proba(feature_headers)[0][0],delay_pred_model.predict_proba(feature_headers)[0][1]
        return float(predicted_value),float(predicted_prob_no_delay),float(predicted_prob_delay)
        

ml_flight_delay:object= MlFlightDelay()

