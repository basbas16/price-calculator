

class Calculator:
    
    @staticmethod
    def discount_by_amount(total_amount: float, discount_amount: float) -> float:

        if (total_amount - discount_amount) < 0:
            return 0

        return total_amount - discount_amount
    
    @staticmethod
    def discount_by_percentage(total_amount: float, percentage_discount: float) -> float:

        result = round((total_amount * (1-(percentage_discount/100))), 2)
        if result > 0:
            return result

        return 0