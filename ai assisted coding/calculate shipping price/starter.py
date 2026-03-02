def calculate_shipping(weight, zone, membership, express):
    if weight > 0:
        if zone in ["domestic", "international"]:
            if membership in ["none", "silver", "gold", "platinum"]:
                if express:
                    if zone == "domestic":
                        if weight <= 5:
                            base = 5.99
                        else:
                            if weight <= 20:
                                base = 12.99
                            else:
                                base = 24.99
                        base = base * 2  # express multiplier
                    else:
                        if weight <= 5:
                            base = 15.99
                        else:
                            if weight <= 20:
                                base = 29.99
                            else:
                                base = 49.99
                        base = base * 2.5
                else:
                    if zone == "domestic":
                        if weight <= 5:
                            base = 5.99
                        else:
                            if weight <= 20:
                                base = 12.99
                            else:
                                base = 24.99
                    else:
                        if weight <= 5:
                            base = 15.99
                        else:
                            if weight <= 20:
                                base = 29.99
                            else:
                                base = 49.99
                if membership == "silver":
                    base = base * 0.9
                elif membership == "gold":
                    base = base * 0.8
                elif membership == "platinum":
                    base = base * 0.7
                return round(base, 2)
            else:
                return -1  # invalid membership
        else:
            return -1  # invalid zone
    else:
        return -1  # invalid weight
    return round(base, 2)

