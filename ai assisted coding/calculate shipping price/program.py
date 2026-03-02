'''
The code is calculating shipping based on 
- weight
- zone
- membership
- express or not

But
- validation should be done first and in the separate method (weight, zone, membership)
- base price calculation should be done in separate classes - DomesticShippingCalculator, InternationalShippingCalculator  with  common BaseShippingCalculator with method Calculate(). You need to add an __init__ to BaseShippingCalculator. calculate() method  should accept weight and express parameters. 

- concrete calculator should be created by the factory using the zone, and pass weight and express parameters to concrete calculator constructor.  
- the membership should be taken into account in a separate function get_membership_multiplier. 
- RoundPrice function should be defined to return the final result from the concrete calculator


Overall, the method should be refactored as follows:
- the validation done first 
- the shipping base price is calculated with concrete shipping calculator from the factory
- the membership multiplier is defined based on membership and applied to the shipping base price
- the price after the membership multiplication is passed to RoundPrice() and the rounded price is returned from the RoundPrice()

(Ignore this line: NOTE: Update after pass 1)
- there is no need for complex concrete shipping calculators, just pass tier prices (tier1, tier2, tier3) to the base constructor
    - for DomesticShippingCalculator, tier 1 (5.99), tier 2(12.99), tier 3 (24.99)
    - for InternationalShippingCalculator, tier 1 (15.99), tier 2 (29.99), tier 3 (49.99)
- for base shipping calculator, define tier borders for weight as constants (the 5, 20 values)
- membership function: membership multipliers dict should be static, not to create it every time when calling the function.  introduce a function apply_membership_discount (accepts base price and membership, returns discounted price) 

(Ignore this line: NOTE: Update after pass 2)
- get_membership_multiplier name can be refactored to apply_membership_discount (accepts base price, returns discounted)

'''






def calculate_shipping(weight, zone, membership, express):
    if not validate_input(weight, zone, membership):
        return -1
    
    calculator = ShippingCalculatorFactory.create(zone)
    base_price = calculator.calculate(weight, express)
    final_price = apply_membership_discount(base_price, membership)
    return round_price(final_price)


def validate_input(weight, zone, membership):
    if weight <= 0:
        return False
    if zone not in ["domestic", "international"]:
        return False
    if membership not in ["none", "silver", "gold", "platinum"]:
        return False
    return True


_MEMBERSHIP_MULTIPLIERS = {
    "none": 1.0,
    "silver": 0.9,
    "gold": 0.8,
    "platinum": 0.7
}

def apply_membership_discount(base_price, membership):
    multiplier = _MEMBERSHIP_MULTIPLIERS.get(membership, 1.0)
    return base_price * multiplier


def round_price(price):
    return round(price, 2)


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
        super().__init__(tier1_price=5.99, tier2_price=12.99, tier3_price=24.99, express_multiplier=2.0)


class InternationalShippingCalculator(BaseShippingCalculator):
    def __init__(self):
        super().__init__(tier1_price=15.99, tier2_price=29.99, tier3_price=49.99, express_multiplier=2.5)


class ShippingCalculatorFactory:
    @staticmethod
    def create(zone):
        if zone == "domestic":
            return DomesticShippingCalculator()
        elif zone == "international":
            return InternationalShippingCalculator()
        return None


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