from fastapi import APIRouter,Path,Query
from app.core.enum.tipo_vuelo import TipoVuelo
from app.core.enum.airlines import Airlines
from app.core.service.flight_service import flight_service
from app.core.swagger.ml_response_codes import ml_response_codes
from app.core.swagger.ml_swagger_output import MlSwaggerOutput
from typing import Optional

class FlightRouter:
    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route("/flight-prediction",self.make_prediction_router,methods=["GET"],response_model=MlSwaggerOutput,responses={**ml_response_codes})

    async def make_prediction_router(self,
                                fecha_vuelo: Optional[str] = None,
                                numero_vuelo: Optional[str] = None,
                                codigo_ciudad_origen: Optional[str] = None,
                                codigo_ciudad_destino: Optional[str] = None,
                                codigo_aerolinea: Optional[str] = None,
                                fecha_operacion: Optional[str] = None,
                                vuelo_operacion: Optional[str] = None,
                                codigo_origen_operacion: Optional[str] = None,
                                codigo_destino_operacion: Optional[str] = None,
                                codigo_aerolinea_operado: Optional[str] = None,
                                dia: Optional[str] = None,
                                mes :int = Query(...,description="Número del mes de operacion del vuelo",ge=1,le=12),
                                ano: Optional[str] = None,
                                dia_nominal: Optional[str] = None,
                                tipo_vuelo:TipoVuelo =Query(...,description="Tipo de vuelo, I =Internacional, N =Nacional"),
                                opera: Airlines=Query(...,description="Nombre de aerolínea que opera"),
                                sigla_origen : Optional[str] = None,
                                sigla_destino : Optional[str] = None
                                ):
        
        return flight_service.prediction_delay(opera,tipo_vuelo,mes)
    
flight_router:object = FlightRouter()
