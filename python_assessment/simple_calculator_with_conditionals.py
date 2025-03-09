# Prompt the user for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

# Perform the operation based on the user's input
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operation!")
    exit()

# Print the result
if operation != "divide" or num2 != 0:
    print(f"The result of {operation}ing {num1} and {num2} is {result}.")