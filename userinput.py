# User Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age += 1 
print(f"Hello, {name}! You are {age} years old.")

# EXAMPLE 1: Area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"The area of the rectangle is: {area} cm²")

# EXAMPLE 2 : Shopping Cart Total
item1_price = float(input("Enter the price of item 1: "))
quantity1 = int(input("Enter the quantity of item 1: "))
item2_price = float(input("Enter the price of item 2: "))
quantity2 = int(input("Enter the quantity of item 2: "))
item3_price = float(input("Enter the price of item 3: "))
quantity3 = int(input("Enter the quantity of item 3: "))

total = (item1_price * quantity1) + (item2_price * quantity2) + (item3_price * quantity3)

print(f"The total cost of your shopping cart is: ${total:.2f}")
