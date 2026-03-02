'''
The code is calculating shipping based on 
- weight
- zone
- membership
- express or not

But
- validation should be done first and in the separate method (weight, zone, membership)
- base price calculation should be done in separate classes - DomesticShippingCalculator and InternationalShippingCalculator  with common base class BaseShippingCalculator containing method Calculate().
- concrete calculator should be created by the factory using the zone parameter
- the membership should be taken into account in a separate function  apply_membership_discount (accepts base price and membership, returns discounted price)
- RoundPrice function should be defined to return the final result
- There is no need for complex concrete shipping calculators. Just pass tier prices (tier1, tier2, tier3) and express multiplier to the base constructor and implement the calculate method in the base class.For base shipping calculator, define tier borders for weight as constants (the 5, 20 values)

Overall, the method should be refactored as follows:
- the validation done first 
- the shipping base price is calculated with concrete shipping calculator from the factory
- the membership multiplier is defined based on membership and applied to the shipping base price
- the price after the membership multiplication is passed to RoundPrice() and the rounded price is returned from the RoundPrice()
'''
def validate_input(weight, zone, membership):
    if weight <= 0:
        return False
    if zone not in ["domestic", "international"]:
        return False
    if membership not in ["none", "silver", "gold", "platinum"]:
        return False
    return True

class BaseShippingCalculator:
    TIER1_WEIGHT = 5
    TIER2_WEIGHT = 20
    
    def __init__(self, tier1_price, tier2_price, tier3_price, express_multiplier):
        self.tier1_price = tier1_price
        self.tier2_price = tier2_price
        self.tier3_price = tier3_price
        self.express_multiplier = express_multiplier
    
    def calculate(self, weight, express):
        if weight <= self.TIER1_WEIGHT:
            base_price = self.tier1_price
        elif weight <= self.TIER2_WEIGHT:
            base_price = self.tier2_price
        else:
            base_price = self.tier3_price
        
        if express:
            base_price = base_price * self.express_multiplier
        
        return base_price

class DomesticShippingCalculator(BaseShippingCalculator):
    def __init__(self):
        super().__init__(tier1_price=5.99, tier2_price=12.99, tier3_price=24.99, express_multiplier=2)

class InternationalShippingCalculator(BaseShippingCalculator):
    def __init__(self):
        super().__init__(tier1_price=15.99, tier2_price=29.99, tier3_price=49.99, express_multiplier=2.5)

class ShippingCalculatorFactory:
    @staticmethod
    def create_calculator(zone):
        if zone == "domestic":
            return DomesticShippingCalculator()
        elif zone == "international":
            return InternationalShippingCalculator()
        return None

def apply_membership_discount(base_price, membership):
    discounts = {
        "none": 1.0,
        "silver": 0.9,
        "gold": 0.8,
        "platinum": 0.7
    }
    return base_price * discounts.get(membership, 1.0)

def round_price(price):
    return round(price, 2)

def calculate_shipping(weight, zone, membership, express):
    if not validate_input(weight, zone, membership):
        return -1
    
    calculator = ShippingCalculatorFactory.create_calculator(zone)
    if calculator is None:
        return -1
    
    base_price = calculator.calculate(weight, express)
    discounted_price = apply_membership_discount(base_price, membership)
    final_price = round_price(discounted_price)
    
    return final_price

if __name__ == "__main__":
    tests = [
        ("Basic Domestic Small", 3, "domestic", "none", False, 5.99),
        ("Intl Medium Express Gold", 12, "international", "gold", True, 59.98),
        ("Invalid Weight Zero", 0, "domestic", "none", False, -1),
        ("Boundary Exactly 5kg", 5, "domestic", "none", False, 5.99),
        ("Boundary Just Over 5kg", 5.1, "domestic", "none", False, 12.99),
        ("Boundary Exactly 20kg", 20, "domestic", "none", False, 12.99),
        ("Boundary Just Over 20kg", 20.1, "domestic", "none", False, 24.99),
        ("Intl Platinum No Express", 10, "international", "platinum", False, 20.99),
        ("Heavy Domestic Silver Express", 25, "domestic", "silver", True, 44.98),
        ("Light Domestic Gold Express", 2, "domestic", "gold", True, 9.58),
        ("Negative Weight", -5, "domestic", "none", False, -1),
        ("Invalid Zone Mars", 5, "mars", "none", False, -1),
        ("Invalid Membership Diamond", 5, "domestic", "diamond", False, -1),
        ("Heavy Intl Express No Discount", 30, "international", "none", False, 49.99),
        ("Intl Silver Rounding", 8, "international", "silver", False, 26.99),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, weight, zone, membership, express, expected in tests:
        result = calculate_shipping(weight, zone, membership, express)
        status = "PASS" if result == expected else "FAIL"
        
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        
        print(f"{status}: {test_name} - Expected: {expected}, Got: {result}")
    
    print(f"\nTotal: {passed} passed, {failed} failed out of {len(tests)} tests")