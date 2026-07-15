# TEMPARATURE CONVERTER

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

if unit == "C":
    converted_temp = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {converted_temp:.2f}")
elif unit == "F":
    converted_temp = (temperature - 32) * 5/9
    print(f"The temperature in Celsius is: {converted_temp:.2f}")
else:
    print("Invalid unit.")