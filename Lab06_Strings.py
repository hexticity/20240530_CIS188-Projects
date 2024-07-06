"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description: 
This program defines a series of functions that perform various string processing tasks.
The functions include:
1. count_characters(string): Returns the number of characters in the string, excluding spaces.
2. sixth_character(string): Returns the character in the 6th position of the string.
3. to_uppercase(string): Returns the string in all uppercase.
4. repeat_last_word(string): Returns the last word in the string, repeated a random number of times.
5. word_count(string): Creates and returns a dictionary with the count of each word in the string.

The main program asks the user to enter a string, passes that string to each function,
and displays the results in an informative and engaging manner.
"""

import random

def count_characters(string):
    """Return the number of characters in the string, excluding spaces."""
    return len(string.replace(" ", ""))

def sixth_character(string):
    """Return the character in the 6th position of the string."""
    return string[5] if len(string) > 5 else None

def to_uppercase(string):
    """Return the string in all uppercase."""
    return string.upper()

def repeat_last_word(string):
    """Return the last word in the string, repeated a random number of times."""
    words = string.split()
    if not words:
        return ""
    last_word = words[-1]
    repeat_count = random.randint(1, 10)
    return " ".join([last_word + "." for _ in range(repeat_count)])

def word_count(string):
    """Return a dictionary with the count of each word in the string."""
    words = string.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

def main():
    print("Welcome to the String Processing Program!")

    while True:
        user_input = input("Please enter your favorite quote:\n")

        if not user_input.strip():
            print("You entered an empty string. Please try again.")
            continue

        # Perform the required tasks
        char_count = count_characters(user_input)
        sixth_char = sixth_character(user_input)
        upper_case_string = to_uppercase(user_input)
        repeated_last_word = repeat_last_word(user_input)
        word_counts = word_count(user_input)

        # Display the results
        print("\nThe number of characters not including spaces is:", char_count)
        if sixth_char:
            print("The character in the 6th position is:", sixth_char)
        else:
            print("The string is too short to have a 6th character.")
        
        print("\nHere is the quote read by someone yelling:", upper_case_string)
        print(f"\n...{repeated_last_word}\n")
        
        print("--------WORD COUNT--------")
        for word, count in word_counts.items():
            print(f"{word:20} {count:5}")

        # Ask if the user wants to process another string
        again = input("\nThat's all the processing we have for you today! Do you want to do that again? (yes/no)\n").strip().lower()
        if again != 'yes':
            break

    print("Thanks for sharing your favorite quote!")

if __name__ == "__main__":
    main()
