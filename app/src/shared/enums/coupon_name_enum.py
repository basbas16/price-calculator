from enum import Enum

class CouponName(Enum):
    FIXED_AMOUNT = "Fixed amount"
    PERCENT_DISCOUNT = "Percent discount"
    PERCENT_BY_CAT = "Percentage discount by item category"
    DISCOUNT_BY_POINT = "Discount by points"
    SPECIAL_CAMPAIGN = "Special campaigns"
