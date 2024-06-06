"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description: The following program will ask the user three questions, output the users answers, and output a final
message that possesses a newly calculated age based on a designed equation (length of name + inputted age = new age)
"""

# Asking for the user's name
name = input("What is your name? ")

# Greeting the user
print("Hello, " + name)

# Asking for the user's age
age = int(input("What is your age? "))

# Calculate the length of the name
name_len = len(name)

# Calculating the new age based on the length of the name
new_age = age + name_len

# Printing the final message
print(name + ", if we add the number of letters in your name to your age then you will be " + str(new_age) + " in " + str(name_len) + " years.")
