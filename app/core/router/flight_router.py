from fastapi import APIRouter,Path, Query
from app.core.enum.tipo_vuelo import TipoVuelo
from app.core.enum.airlines import Airlines


class FlightRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/flight-prediction",self.make_prediction_router,methods=["GET"])

    async def make_prediction_router(self,opera: Airlines=Query(...,description="Nombre de aerolínea que opera"),
                       tipo_vuelo:TipoVuelo =Query(...,description="Tipo de vuelo, I =Internacional, N =Nacional"),
                         mes :int = Query(...,description="Número del mes de operacion del vuelo",ge=1,le=12)):
        
        return opera
    


flight_router:object = FlightRouter()
