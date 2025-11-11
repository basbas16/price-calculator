from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.src.module.coupon_calculator import CouponCalculator
from app.src.module.coupon_process import CouponProcess
from app.src.shared.enums.promotion_name_enum import PromotionCategory
from app.src.shared.models.coupon import CouponModel
from app.src.shared.models.product import ItemAndPromotionList, ProductModel
from app.src.shared.models.response import DiscountResponse

router = APIRouter()

@router.post(
    path="/calculate-price/",
    tags=["price calculator"]
)
def calculate_price(items: ItemAndPromotionList):
    try:
        if not items:
            raise HTTPException(
                status_code=400,
                detail="No items provided."
            )

        is_valid = CouponCalculator.coupon_validation(items.promotions)
        if not is_valid:
            raise HTTPException(
                status_code=400,
                detail="Invalid coupon category. Valid categories: Coupon, On_Top, Seasonal"
            )
        print(items)
        # Calculate prices
        original_price = items.total_price()
        print("Price before calculate {}".format(original_price))

        total_discount = calculate_final_price(
            original_price,
            items
        )

        final_price = round(original_price - total_discount, 2)
        print("Final price {}".format(final_price))

        return DiscountResponse(
            original_price=original_price,
            final_price=final_price,
            total_discount=total_discount,
            message="Discount calculated successfully"
        )

    except Exception as e:
        raise HTTPException(
                status_code=500,
                detail=e
            )

def calculate_final_price(total_amount: float, items: ItemAndPromotionList) -> float:

    current_price = total_amount
    sorted_coupons = CouponProcess.sort_coupons_by_priority(items.promotions)
    print(sorted_coupons)
    for coupon in sorted_coupons:
        current_price = apply_coupon_discount(coupon, current_price, items.products)

    return round(current_price, 2)

def apply_coupon_discount(coupon: CouponModel, current_price: float, products: list[ProductModel]) -> float:
    if coupon.campaign_cat == PromotionCategory.COUPON.value:
        return CouponProcess.apply_coupon_category(coupon, current_price)
    elif coupon.campaign_cat == PromotionCategory.ON_TOP.value:
        return CouponProcess.apply_ontop_category(coupon, current_price, products)
    elif coupon.campaign_cat == PromotionCategory.SEASONAL.value:
        return CouponProcess.apply_seasonal_category(coupon, current_price)
    return current_price

