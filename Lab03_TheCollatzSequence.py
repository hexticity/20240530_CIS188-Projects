"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description: 
This program defines a function named collatz() that performs the Collatz sequence operation.
If the number is even, it returns number // 2.
If the number is odd, it returns 3 * number + 1.
"""

def collatz(number):
  # Check if the inputted number is even
  if number % 2 == 0:
    result = number // 2
  else:
    # Check if the inputted number is odd
    result = 3 * number + 1
  print(result) # Print the result
  return result # Return the result

# Print a welcome message to the user
print("Welcome to the simplest impossible math problem, the Collatz Sequence!")

# Prompt the user to enter a positive number and convert the input to an integer
number = int(input("Please enter a positive number: "))

# Continue calling collatz() and updating the number until it becomes 1
while number != 1:
    number = collatz(number)
