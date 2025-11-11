from pydantic import BaseModel


# Response models
class DiscountResponse(BaseModel):
    """Response model for discount calculation"""
    original_price: float
    final_price: float
    total_discount: float
    message: str = "Success"

    class Config:
        json_schema_extra = {
            "example": {
                "original_price": 1000.0,
                "final_price": 750.0,
                "total_discount": 250.0,
                "message": "Success"
            }
        }
