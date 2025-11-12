import json

from fastapi.responses import JSONResponse

class ResponseUtils:

    @staticmethod
    def get_error_response(status_code: int, message):
        return JSONResponse(
            status_code=status_code,
            content={
                "body":{
                        "message": message
                }
            }
        )