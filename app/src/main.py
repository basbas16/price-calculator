from fastapi import FastAPI, Request

import uvicorn
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.src.price_calculator import price_calculator

fast_api_app = FastAPI(title="Price Calculator API", version="1.0.0")

fast_api_app.include_router(price_calculator.router)


@fast_api_app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0]

    return JSONResponse(
        status_code=422,
        content={
            "error": first_error["msg"],
            "field": ".".join(str(x) for x in first_error["loc"])
        }
    )


# Run with: uvicorn src.app.main:app --reload
if __name__ == "__main__":
    uvicorn.run(fast_api_app, host="0.0.0.0", port=8000)
    
    
