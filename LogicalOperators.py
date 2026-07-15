# LOGICAL OPERATORS 
# and, or, not

#LOGICAL OR
temp = -45
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.") 
else:
    print("The outdoor event is still scheduled.")

#LOGICAL AND
temp = 28
is_sunny = False
if temp >= 28 and is_sunny:
    print("It is Hot outside.")
    print("It is Sunny.")
elif temp <= 0 and is_sunny:
    print("It is cool outside.")
    print("It is Sunny.")
elif 28 > temp > 0 and is_sunny:
    print("It is  outside.")
    print("It is Sunny.")

if temp > 28 and not is_sunny:
    print("It is Hot outside.")
    print("It is cloudy.")
elif temp < 0 and not is_sunny:
    print("It is cold outside.")
    print("It is cloudy.")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside.")
    print("It is cloudy.")