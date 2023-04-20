from fastapi import APIRouter,Path,Query
from app.core.enum.tipo_vuelo import TipoVuelo
from app.core.enum.airlines import Airlines
from app.core.enum.siglades import Siglades
from app.core.service.flight_service import flight_service
from app.core.swagger.ml_response_codes import ml_response_codes
from app.core.swagger.ml_swagger_output import MlSwaggerOutput
from typing import Optional

class FlightRouter:
    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route("/delay-prediction",self.make_prediction_router,methods=["GET"],response_model=MlSwaggerOutput,responses={**ml_response_codes})

    async def make_prediction_router(self,
                                fecha_vuelo: Optional[str] = Query (None,description="Fecha y hora programada del vuelo"),
                                numero_vuelo: Optional[int] = Query(None,description="Número de vuelo programado", ge=0, le=9999),
                                codigo_ciudad_origen: Optional[str] = Query(None,description="Código de vuelo de ciudad de origen programado",min_length=3,max_length=5),
                                codigo_ciudad_destino: Optional[str] = Query(None,description="Código de ciudad de destino programado",min_length=3,max_length=5),
                                codigo_aerolinea: Optional[str] = Query(None,description="Código aerolínea de vuelo programado",min_length=3,max_length=3),
                                fecha_operacion: Optional[str] = Query(None,description="Fecha y hora de operación del vuelo"),
                                vuelo_operacion: Optional[int] = Query(None,description="Número de vuelo de operación del vuelo",ge=10, le=9999),
                                codigo_origen_operacion: Optional[str] = Query(None,description="Código de ciudad de origen de operación",min_length=3,max_length=5),
                                codigo_destino_operacion: Optional[str] = Query(None,description="Código de ciudad de destino de operación",min_length=3,max_length=5),
                                codigo_aerolinea_operado: Optional[str] = Query(None,description="Código aerolínea de vuelo operado",min_length=3,max_length=3),
                                dia: Optional[int] = Query(None,description="Día del mes de operacion del vuelo",ge=1,le=31),
                                mes : int = Query(...,description="Número del mes de operacion del vuelo",ge=1,le=12),
                                ano: Optional[int] = Query(None,description = "Año de operacion del vuelo",ge= 2000,le=3000),
                                dia_nominal: Optional[str] = Query(None,description ="Día de la semana de operación del vuelo",min_length=4,max_length=100),
                                tipo_vuelo:TipoVuelo =Query(...,description="Tipo de vuelo, I =Internacional, N =Nacional"),
                                opera: Airlines=Query(...,description="Nombre de aerolínea que opera"),
                                sigla_origen : Optional[str] = Query(None,description="Nombre ciudad origen",min_length=3,max_length=100),
                                sigla_destino : Optional[Siglades] = Query(None,description="Nombre ciudad destino")
                                ):
        
        return flight_service.prediction_delay(opera,tipo_vuelo,mes)
    
flight_router:object = FlightRouter()
