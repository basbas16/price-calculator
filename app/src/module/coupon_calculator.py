from app.src.module.calculator import Calculator
from app.src.shared.enums.coupon_name_enum import CouponName
from app.src.shared.enums.promotion_name_enum import PromotionCategory
from app.src.shared.models.coupon import CouponModel
from app.src.shared.models.product import ProductModel
import math


class CouponCalculator:

    @staticmethod
    def discount_by_percentage_with_category(total_amount: float, category: str, product: list[ProductModel], percent_amount):
        discount_item = [item for item in product if item.product_type.lower() == category.lower()]
        discount_amount = 0
        for item in discount_item:
            discount_amount += item.price
        discount_category = Calculator.discount_by_percentage(discount_amount, percent_amount)
        discount_price = (total_amount - discount_amount) + discount_category
        return discount_price

    @staticmethod
    def discount_by_point(total_amount: float, points: int) -> float:
        discount = points / total_amount
        if discount > 0.2:
            return Calculator.discount_by_percentage(total_amount, 20)

        return Calculator.discount_by_amount(total_amount, points)

    @staticmethod
    def discount_by_spacial_campaign(total_amount: float, discount_amount: float, discount_every: float) -> float:
        discount = math.floor(total_amount / discount_every) * discount_amount
        return Calculator.discount_by_amount(total_amount, discount)

    @staticmethod
    def coupon_validation(coupons: list[CouponModel]) -> bool:

        enum_promo_cate = [item.value for item in PromotionCategory]
        enum_coupon_name = [item.value for item in CouponName]

        # Check 1: Find invalid coupon types (not in enum)
        seen_types = set()
        duplicate_types = []
        invalid_coupons = []

        for coupon in coupons:

            if coupon.campaign_cat not in enum_promo_cate or coupon.code not in enum_coupon_name:
                invalid_coupons.append(coupon.campaign_cat)

            if coupon.campaign_cat in seen_types:
                if coupon.campaign_cat not in duplicate_types:
                    duplicate_types.append(coupon.campaign_cat)
            else:
                seen_types.add(coupon.campaign_cat)

        # Return True if any validation errors found
        has_invalid = len(invalid_coupons) > 0
        has_duplicates = len(duplicate_types) > 0

        if has_invalid or has_duplicates:
            return False

        return True
