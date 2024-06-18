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

print("Welcome to the Collatz Sequence calculator.")
number = int(input("Please enter a positive number: "))

while number != 1:
    number = collatz(number)
