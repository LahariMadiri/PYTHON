# IF STATEMENTS

#EXAMPLE 1
age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign in.")
elif age >= 18:
    print("You are allowed to sign in.")
else:
    print("Invalid age.")

#EXAMPLE 2
response = input("would you like food? (yes/no): ")
if response == "yes":
    print("have some food.")
else:
    print("No food for you.")

#EXAMPLE 3
name = input("Enter your name: ")
if name == "":
    print("you didn't type anything.")
else:
    print(f"Hello {name}")

#BOOLEAN IF STATEMENTS
# EXAMPLE 
for_scale = False
if for_scale:
    print("This item is for scale.")
else:
    print("This item is not for scale.")