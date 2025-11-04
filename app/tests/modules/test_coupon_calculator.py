import unittest

from app.src.module.coupon_calculator import CouponCalculator
from app.src.shared.models.coupon import CouponModel
from app.src.shared.models.product import ProductModel

class TestCouponCalculator(unittest.TestCase):

    def test_discount_by_percentage_with_category(self):
        
        actual_result = CouponCalculator.discount_by_percentage_with_category(
            300,
            "Electronics",
            [
                ProductModel(product_name="mock1", product_type="Electronics", price=100),
                ProductModel(product_name="mock2", product_type="Clothing", price=50),
                ProductModel(product_name="mock3", product_type="Electronics", price=150),
            ],
            10
        )
        
        expected_result = 275.0
        self.assertEqual(actual_result, expected_result)

    def test_discount_by_point_point_more_than_20_percent_of_total_amount(self):
        
        actual_result = CouponCalculator.discount_by_point(500, 250)
        
        expected_result = 400.0
        self.assertEqual(actual_result, expected_result)
        
    
    def test_discount_by_point_point_below_20_percent_of_total_amount(self):
        
        actual_result = CouponCalculator.discount_by_point(500, 20)
        
        expected_result = 480.0
        self.assertEqual(actual_result, expected_result)
        
    def test_discount_by_spacial_campaign(self):
        
        actual_result = CouponCalculator.discount_by_spacial_campaign(550, 30, 100)
        
        expected_result = 400.0
        self.assertEqual(actual_result, expected_result)
        
    def test_coupon_validation_invalid(self):
        
        actual_result = CouponCalculator.coupon_validation(
            [
                # Valid coupon
                CouponModel(code="SUMMER21", campaign_cat="Seasonal"),
                # Duplicate coupon category
                CouponModel(code="WINTER21", campaign_cat="Seasonal"),
                # Invalid coupon code
                CouponModel(code="INVALIDCODE", campaign_cat="Holiday"),
                # Invalid campaign category
                CouponModel(code="SPRING21", campaign_cat="InvalidCategory"),
            ]
        )
        
        self.assertFalse(actual_result)
        
    def test_coupon_validation_valid(self):
        
        actual_result = CouponCalculator.coupon_validation(
            [
                CouponModel(code="Special campaigns", campaign_cat="Seasonal"),
                CouponModel(code="Percent discount", campaign_cat="Coupon"),
            ]
        )
        self.assertTrue(actual_result)