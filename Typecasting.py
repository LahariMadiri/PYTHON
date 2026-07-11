# Typecasting
name = "John"
age = 20
price = 10.5
is_student = True
print(f"Is Student: {is_student}")

# Converting to different types

name = str(name)
print(f"Name: {name}, Type: {type(name)}")
age = float(age)
print(f"Age: {age}, Type: {type(age)}")
price = int(price)
print(f"Price: {price}, Type: {type(price)}")

pens = "Blue"
print(bool(pens)) 
pencils = ""
print(bool(pencils))