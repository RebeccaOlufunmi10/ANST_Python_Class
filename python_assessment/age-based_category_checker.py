# Ask the user for their age
age = int(input("Enter your age: "))

# Categorize based on the age
if age < 13:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")