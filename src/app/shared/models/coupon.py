
from typing import Optional
from pydantic import BaseModel, ConfigDict


class CouponModel(BaseModel):
    code: str
    campaign_cat: str
    amount: Optional[int] = None
    discount_percent: Optional[int] = None
    discount_every_bath: Optional[int] = None
    product_category: Optional[str] = None
    customer_point: Optional[int] = None

    model_config = ConfigDict(extra="forbid")