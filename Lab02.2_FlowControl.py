"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description: 
This program asks the user for their name and two simple questions about their preferences.
Based on the user's responses, it displays a custom message using decision structures.
The program demonstrates the use of if/else and if/elif/else statements to handle different outcomes.
The program will keep running until the user decides to exit.
It also includes a for loop that iterates a random number of times to display a message.
"""
import random

while True:
    # Ask for the user's name
    name = input("What is your name? ")

    # Ask the first question
    favorite_color = input("What is your favorite color? ")

    # Ask the second question
    pet_preference = input("Do you prefer cats or dogs? ")

    # Decision structure for favorite color
    if favorite_color == 'blue':
        color_message = "Blue is a calming color!"
    elif favorite_color == 'red':
        color_message = "Red is full of energy and passion!"
    else:
        color_message = favorite_color + " is a unique choice!"

    # Decision structure for pet preference
    if pet_preference == 'cats':
        pet_message = "Cats are great companions and very independent."
    elif pet_preference == 'dogs':
        pet_message = "Dogs are loyal and always ready for an adventure."
    else:
        pet_message = "It's great to have diverse pet preferences!"

    # Combine the responses and display the custom message
    print("Hello, " + name + "! " + color_message + " " + pet_message)

    # For loop that iterates a random number of times
    random_times = random.randint(1, 10)
    for i in range(random_times):
        print(f"Yeehaw! {i + 1}")

    # Ask the user if they want to run the program again
    continue_program = input("Do you want to continue? (yes/no) ")
    if continue_program == 'no':
        print("Goodbye!")
        break
