import json
import unittest

from fastapi.responses import JSONResponse
from starlette.testclient import TestClient

from app.src.main import fast_api_app
from app.src.price_calculator.price_calculator import calculate_price
from app.src.shared.models.product import ItemAndPromotionList, ProductModel

client = TestClient(fast_api_app)

class TestCalculatePrice(unittest.TestCase):


    def test_calculate_price_empty_cart_data(self):

        mock_input = {
            "cart":[],
            "promotions":[]
        }
        actual_result = client.post("/calculate-price/", json=mock_input)

        expect_result = JSONResponse(
            status_code=422,
            content={
                "body":{
                    "message": "Products Is Empty"
                }
            }
        ).body
        self.assertEqual(422, actual_result.status_code)
        self.assertEqual(json.loads(expect_result), actual_result.json())

    def test_calculate_price_empty_promotion_data(self):

        mock_input = {
            "cart":[
                {
                    "product_name": "Wireless Mouse",
                    "price": 250,
                    "product_type": "electronics"
                },
                {
                    "product_name": "Bluetooth Keyboard",
                    "price": 2500,
                    "product_type": "electronics"
                }
            ],
            "promotions":[]
        }
        actual_result = client.post("/calculate-price/", json=mock_input)

        expect_result = JSONResponse(
            status_code=200,
            content={'final_price': 2750.0,
                     'message': 'Discount calculated successfully',
                     'original_price': 2750.0,
                     'total_discount': 0.0}
        ).body
        self.assertEqual(200, actual_result.status_code)
        self.assertEqual(json.loads(expect_result), actual_result.json())

    def test_calculate_price_with_all_data(self):

        mock_input = {
            "cart":[
                {
                    "product_name": "Wireless Mouse",
                    "price": 250,
                    "product_type": "electronics"
                },
                {
                    "product_name": "Bluetooth Keyboard",
                    "price": 2500,
                    "product_type": "electronics"
                }
            ],
            "promotions":[
                {
                    "code": "Special campaigns",
                    "campaign_cat": "Seasonal",
                    "amount": 50,
                    "discount_every_bath": 1000
                }
            ]
        }
        actual_result = client.post("/calculate-price/", json=mock_input)

        expect_result = JSONResponse(
            status_code=200,
            content={
                'final_price': 100.0,
                'message': 'Discount calculated successfully',
                'original_price': 2750.0,
                'total_discount': 2650.0
            }
        ).body
        self.assertEqual(200, actual_result.status_code)
        self.assertEqual(json.loads(expect_result), actual_result.json())
