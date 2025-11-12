
from pydantic import BaseModel, ConfigDict

from app.src.shared.models.coupon import CouponModel


class ProductModel(BaseModel):
    product_name: str
    product_type: str
    price: float

    model_config = ConfigDict(extra="forbid")
    
    
class ItemAndPromotionList(BaseModel):
    cart: list[ProductModel]
    promotions: list[CouponModel]

    model_config = ConfigDict(extra="forbid")
    
    def total_price(self) -> float:
        return sum(p.price for p in self.cart)