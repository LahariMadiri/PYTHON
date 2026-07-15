# ARITHMETIC OPERATIONS

# x = 10
# x = x + 5
# x += 3
# x = x - 7
# x -= 2
# x = x * 4
# x *= 2
# x = x / 3
# x /= 2
# x = x % 4
# x %= 3
# x = x ** 2
# x **= 3

x = 3.14
y = 26
z = -2
p = 2

print("Result = ", round(x), abs(z), pow(y, p), max(x, y, z, p), min(x, y, z, p))

# USEFUL MATH FUNCTIONS
import math
x = 3.23
print("Result = ", math.ceil(x), math.floor(x), math.sqrt(x), math.pi, math.e)

# EXAMPLES FOR MATH FUNCTIONS
# CIRCUMFERENCE OF CIRCLE

import math
radius = float(input ("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f" the Circumference of the circle is: {round(circumference, 3)} cms")

#AREA OF CIRCLE
import math
radius = float(input ("Enter the radius of the circle: "))
area = math.pi * radius ** 2
# area = math.pi * radius * radius
# area = math.pi * pow(radius, 2)
print(f" the Area of the circle is: {round(area, 2)} sq.cms")

# HYPOTENUSE OF A RIGHT ANGLE TRIANGLE
import math
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
hypotenuse = math.sqrt(base ** 2 + height ** 2)
# hypotenuse = math.sqrt(pow(base, 2) + pow(height, 2))
print(f" the Hypotenuse of the triangle is: {round(hypotenuse, 2)} cms")