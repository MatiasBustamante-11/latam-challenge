from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

async def validation_exception_handler(request: Request, exc: RequestValidationError):
      error_message=[]
      if (exc.errors()):
           for details in exc.errors():
               error_message.append({"parameter":details["loc"][1],"message":details["msg"].split(";")[0]})
      return JSONResponse(
         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
         content=jsonable_encoder({"details": error_message, # optionally include the errors
               "message": "Unable to process your request due to invalid data"}),
      )