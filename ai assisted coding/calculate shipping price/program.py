'''
The prompt
The initial code is calculating shipping based on 
- weight
- zone
- membership
- express or not

But
- validation should be done first and in the separate method (weight, zone, membership)
- base price calculation should be done in separate classes (DomesticShippingCalculator, InternationalShippingCalculator  with  common AbstractShippingCalculator classes with method Calculate() ). You need to add an __init__ to AbstractShippingCalculator that stores weight and express, and update calculate() to use self instead of parameters
- concrete calculator should be created by the factory using the zone, and pass weight and express parameters to concrete calculator constructor.  
- the membership should be taken into account in a separate function  (GetMembershipMultiplier with param membership). membership multipliers dict should be static, not to create it every time when calling the function
- RoundPrice function should be defined to return the final result from the concrete calculator

Overall, the method should be refactored as follows:
- the validation done first 
- the shipping base price is calculated with concrete shipping calculator from the factory
- the membership multiplier is defined based on membership and applied to the shipping base price
- the price after the membership multiplication is passed to RoundPrice() and the rounded price is returned from the RoundPrice()
'''

from abc import ABC, abstractmethod


class AbstractShippingCalculator(ABC):
    def __init__(self, weight, express):   # Accept and store args
        self.weight = weight
        self.express = express

    @abstractmethod
    def calculate(self):   # No longer takes params — uses self.weight/self.express
        pass


class DomesticShippingCalculator(AbstractShippingCalculator):
    def calculate(self):
        if self.weight <= 5:
            base = 5.99
        elif self.weight <= 20:
            base = 12.99
        else:
            base = 24.99
        if self.express:
            base *= 2
        return base


class InternationalShippingCalculator(AbstractShippingCalculator):
    def calculate(self):
        if self.weight <= 5:
            base = 15.99
        elif self.weight <= 20:
            base = 29.99
        else:
            base = 49.99
        if self.express:
            base *= 2.5
        return base


class ShippingCalculatorFactory:
    @staticmethod
    def create_calculator(zone, weight, express):   # Pass weight & express here
        if zone == "domestic":
            return DomesticShippingCalculator(weight, express)
        elif zone == "international":
            return InternationalShippingCalculator(weight, express)
        return None


def validate_inputs(weight, zone, membership):
    if weight <= 0:
        return False
    if zone not in ["domestic", "international"]:
        return False
    if membership not in ["none", "silver", "gold", "platinum"]:
        return False
    return True


def get_membership_multiplier(membership):
    multipliers = {
        "none": 1.0,
        "silver": 0.9,
        "gold": 0.8,
        "platinum": 0.7
    }
    return multipliers.get(membership, 1.0)


def round_price(price):
    return round(price, 2)


def calculate_shipping(weight, zone, membership, express):
    if not validate_inputs(weight, zone, membership):
        return -1
    
    calculator = ShippingCalculatorFactory.create_calculator(zone, weight, express)
    if calculator is None:
        return -1
    
    base_price = calculator.calculate()   # No args needed anymore
    multiplier = get_membership_multiplier(membership)
    return round_price(base_price * multiplier)


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