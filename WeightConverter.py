# WEIGHT CONVERTER USING PYTHON
weight = float(input("Enter your weight: "))
unit = input("Enter unit (K for kilograms, L for pounds): ")

if unit == "K":
    weight_lbs = weight * 2.20462
    print(f"Your weight in pounds is: {weight_lbs:.2f}")
elif unit == "L":
    weight_kg = weight * 0.453592
    print(f"Your weight in kilograms is: {weight_kg:.2f}")
else:
    print("Invalid unit.")