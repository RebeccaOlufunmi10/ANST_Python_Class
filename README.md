

### Assignment

##### Task 1: simple_interest.py

Your task is to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:
•	( I ) is the interest earned,
•	( P ) is the principal amount (initial investment),
•	( R ) is the annual interest rate (as a decimal),
•	( T ) is the time the money is invested for in years.
Instructions:
•	Create a file named simple_interest.py.
•	Define three variables in this file:
		o	principal with a value of 1000 (representing $1000),
		o	rate with a value of 0.05 (representing 5% annual interest rate),
		o	time with a value of 3 (representing 3 years).
•	Calculate the simple interest using the formula provided and store the result in a variable named interest.
•	Print the calculated interest in a format: The simple interest is: [interest].
**Expected Output:**
When executed, your script should print the simple interest calculated with the provided values. For principal = 1000, rate = 0.05, and time = 3, the output should be:


##### Task 2: hours_to_seconds.py

For this task, write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.
Instructions:
•	Create a file named hours_to_seconds.py.
•	Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
•	Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
•	Store the result of the conversion in a variable named seconds.
•	Print the result in the format: [hours] hour(s) is [seconds] seconds.
**Expected Output:**
Given the value hours = 2, your script should output:


##### Task 3: future_age_calculator.py

Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.
Instructions:
•	Create a file named future_age_calculator.py.
•	Prompt the user to input their current age with the question: “How old are you? ”.
•	Assume the user will input a valid integer value.
•	Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
•	Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.


**Expected Script Flow:**

1. The script prompts the user for their current age.
2. The user enters their age.
3. The script calculates and prints how old the user will be in 2050.
   Example Interaction:
   If the user inputs 30 when prompted for their current age, the output should be:


##### Task 4: finance_calculator.py

You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
Instructions:

1. User Input for Financial Details:
   o	Prompt the user for their monthly income: “Enter your monthly income: ”.
   o	Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
2. Calculate Monthly Savings:
   o	Calculate the monthly savings by subtracting monthly expenses from the monthly income.
3. Project Annual Savings:
   o	Assume a simple annual interest rate of 5%.
   o	Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
4. **Output Results:**
   o	Display the user’s monthly savings.
   o	Display the projected annual savings after including interest.
