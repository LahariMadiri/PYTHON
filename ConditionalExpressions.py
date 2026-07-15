# CONDITIONAL EXPRESSIONS 
# X if condition else Y

num = 5
print("Even" if num % 2 == 0 else "Odd")
a = 2
b = 4
max_num = a if a > b else b
print("The maximum number is:", max_num)
min_num = a if a < b else b
print("The minimum number is:", min_num)
age = 18
print("You are eligible to vote" if age >= 18 else "You are not eligible to vote")
temperature = 30
print("summer" if temperature > 25 else "winter")
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)