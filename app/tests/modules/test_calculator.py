import unittest

from app.src.module.calculator import Calculator


class TestCalculator(unittest.TestCase):
    
    def test_discount_by_amount(self):

        # Test logic for calculating coupon discount
        actual_result = Calculator.discount_by_amount(200, 20)

        expected_result = 180
        self.assertEqual(actual_result, expected_result)

    def test_discount_by_amount_if_discount_more_than_price(self):
        # Test logic for calculating coupon discount
        actual_result = Calculator.discount_by_amount(200, 2000)

        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_discount_by_percentage(self):
        # Test logic for handling invalid coupon codes

        actual_result = Calculator.discount_by_percentage(200, 15)

        expected_result = 170
        self.assertEqual(actual_result, expected_result)
        
    def test_discount_by_percentage_with_discount_over(self):
        # Test logic for handling invalid coupon codes

        actual_result = Calculator.discount_by_percentage(200, 2000)

        expected_result = 0
        self.assertEqual(actual_result, expected_result)