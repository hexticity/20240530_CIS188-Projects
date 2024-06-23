"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description: This program simulates the flipping of a coin 100 times and checks if there is a streak of six heads or tails in a row.
             The experiment is repeated 10,000 times to estimate the probability of such streaks occurring.
"""

import random  # This may be beyond Chapter 4 if it's not covered

# Constants
EXPERIMENTS = 10000  # Number of experiments to perform
LIST_SIZE = 100  # Number of coin flips in each experiment
STREAK_SIZE = 6  # Size of streak to look for (six heads or six tails in a row)

numberOfListsWithStreaks = 0  # Counter for lists containing at least one streak of the specified size

for experimentNumber in range(EXPERIMENTS):
    # Generate a list of 100 random 'H' (heads) or 'T' (tails) values
    flips = []
    for i in range(LIST_SIZE):
        if random.randint(0, 1) == 0:  # Using random module
            flips.append('H')
        else:
            flips.append('T')
    
    # Check the list for streaks of 6 heads or tails in a row
    current_streak = 1  # Counter for the current streak length
    found_streak = False  # Flag to indicate if a streak has been found in the current list
    for i in range(1, LIST_SIZE):
        if flips[i] == flips[i-1]:
            current_streak += 1  # Increment streak length if current flip matches the previous one
            if current_streak == STREAK_SIZE:
                found_streak = True  # Set flag if a streak of the desired length is found
                break  # Exit the loop early since a streak has been found
        else:
            current_streak = 1  # Reset streak length if current flip does not match the previous one
    
    if found_streak:
        numberOfListsWithStreaks += 1  # Increment counter if a streak was found in the current list

# Calculate and print the percentage of lists containing a streak
chance_of_streak = (numberOfListsWithStreaks / EXPERIMENTS) * 100
print('Chance of streak: %s%%' % ((numberOfListsWithStreaks / EXPERIMENTS)*100))  # Using concatenation instead of formatted string

