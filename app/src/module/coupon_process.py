from app.src.module.calculator import Calculator
from app.src.module.coupon_calculator import CouponCalculator
from app.src.shared.enums.coupon_name_enum import CouponName
from app.src.shared.models.coupon import CouponModel
from app.src.shared.models.product import ProductModel


class CouponProcess:
    
    @staticmethod
    def sort_coupons_by_priority(coupons: list[CouponModel]) -> list[CouponModel]:
        """Sort coupons by category priority: Coupon > On_Top > Seasonal"""
        category_priority = {"Coupon": 1, "On_Top": 2, "Seasonal": 3}
        return sorted(coupons, key=lambda c: category_priority.get(c.campaign_cat, 999))


    @staticmethod
    def apply_coupon_category(coupon: CouponModel, current_price: float) -> float:
        """Apply Coupon category discount (fixed amount)"""
        if coupon.amount and coupon.code == CouponName.FIXED_AMOUNT.value:
            return Calculator.discount_by_amount(current_price, coupon.amount)
        elif coupon.discount_percent and coupon.code == CouponName.PERCENT_DISCOUNT.value:
            return Calculator.discount_by_percentage(current_price, coupon.discount_percent)
        return current_price


    @staticmethod
    def apply_ontop_category(coupon: CouponModel, current_price: float, products: list[ProductModel]) -> float:
        """Apply On_Top category discount (percentage)"""
        if coupon.product_category and coupon.discount_percent and coupon.code == CouponName.PERCENT_BY_CAT.value:
            return CouponCalculator.discount_by_percentage_with_category(
                current_price,
                coupon.product_category,
                products,
                coupon.discount_percent
            )
        elif coupon.customer_point and coupon.code == CouponName.DISCOUNT_BY_POINT.value:
            return CouponCalculator.discount_by_point(current_price, coupon.customer_point)
        return current_price


    @staticmethod
    def apply_seasonal_category(coupon: CouponModel, current_price: float) -> float:
        """Apply Seasonal category discount (tiered)"""
        if coupon.amount and coupon.discount_every_bath and coupon.code == CouponName.SPECIAL_CAMPAIGN.value:
            return CouponCalculator.discount_by_spacial_campaign(
                current_price,
                coupon.amount,
                coupon.discount_every_bath
            )
        return current_price 