import unittest

from app.src.module.coupon_process import CouponProcess
from app.src.shared.enums.coupon_name_enum import CouponName
from app.src.shared.enums.promotion_name_enum import PromotionCategory
from app.src.shared.models.coupon import CouponModel
from app.src.shared.models.product import ProductModel

class TestCouponProcess(unittest.TestCase):
    
    def test_sort_coupons_by_priority(self):
        
        actual_result = CouponProcess.sort_coupons_by_priority([
            CouponModel(code="C1", campaign_cat="Seasonal"),
            CouponModel(code="C2", campaign_cat="Coupon"),
            CouponModel(code="C3", campaign_cat="On_Top"),
        ])
        
        expected_result = [
            CouponModel(code="C2", campaign_cat="Coupon"),
            CouponModel(code="C3", campaign_cat="On_Top"),
            CouponModel(code="C1", campaign_cat="Seasonal"),
            ]
        self.assertEqual(actual_result, expected_result)

    def test_apply_coupon_category_with_fixed_amount(self):
    
        actual_result = CouponProcess.apply_coupon_category(
            CouponModel(code=CouponName.FIXED_AMOUNT.value, campaign_cat="Coupon", amount=30),
            200
        )
        excepted_result = 170
        self.assertEqual(actual_result, excepted_result)

    def test_apply_coupon_category_discount_by_percent(self):

        actual_result = CouponProcess.apply_coupon_category(
            CouponModel(code=CouponName.PERCENT_DISCOUNT.value, campaign_cat="Coupon", discount_percent=30),
            200
        )
        excepted_result = 140
        self.assertEqual(actual_result, excepted_result)

    def test_apply_ontop_category_percent_by_cat(self):

        product = [
                ProductModel(product_name="mock1", product_type="Electronics", price=100),
                ProductModel(product_name="mock2", product_type="Clothing", price=50),
                ProductModel(product_name="mock3", product_type="Electronics", price=150)
        ]
        coupon = CouponModel(code=CouponName.PERCENT_BY_CAT.value, campaign_cat="On_Top",product_category="Electronics", discount_percent=30)


        actual_result = CouponProcess.apply_ontop_category(coupon, 300, product)

        expect_result = 225

        self.assertEqual(actual_result, expect_result)

    def test_apply_ontop_category_customer_point(self):

        product = [
                ProductModel(product_name="mock1", product_type="Electronics", price=100),
                ProductModel(product_name="mock2", product_type="Clothing", price=50),
                ProductModel(product_name="mock3", product_type="Electronics", price=150)
        ]
        coupon = CouponModel(code=CouponName.DISCOUNT_BY_POINT.value, campaign_cat="On_Top",customer_point=50)


        actual_result = CouponProcess.apply_ontop_category(coupon, 300, product)

        expect_result = 250

        self.assertEqual(actual_result, expect_result)

    def test_apply_seasonal_category(self):
        coupon = CouponModel(code=CouponName.SPECIAL_CAMPAIGN.value, campaign_cat=PromotionCategory.SEASONAL.value, discount_every_bath=500, amount=50)

        actual_result = CouponProcess.apply_seasonal_category(coupon, 2000)

        expect_result = 1800

        self.assertEqual(actual_result, expect_result)
