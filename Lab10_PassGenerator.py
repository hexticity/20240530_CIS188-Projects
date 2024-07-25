"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description:
This program reads employee data from a CSV file and generates a new CSV file with added randomly generated passwords.
It performs the following tasks:
1. Defines a function to generate random passwords.
2. Reads employee data from the provided 'employees.csv' file.
3. Generates a random password for each employee.
4. Writes a new CSV file 'employees_with_passwords.csv' containing the first name, last name, email, and the new password.

"""

import csv
import random

# Define the function to generate random passwords
def gen_pass(length=16):
    # Generate a random password using a set of characters
    import string
    all_characters = string.ascii_letters + string.digits + '!@$%^&*-_+=~<>/\\(){}[]?|'
    password = "".join(random.sample(all_characters, length))
    return password

# Paths to the input and output files
input_file_path = '/mnt/data/employees.csv'
output_file_path = '/mnt/data/employees_with_passwords.csv'

# Open the files and set up CSV reader and writer
with open(input_file_path, mode='r', newline='') as infile, open(output_file_path, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header row for the new CSV file
    writer.writerow(['First Name', 'Last Name', 'Email', 'Password'])

    # Process each row in the input file
    for row in reader:
        first_name = row[0]
        last_name = row[1]
        email = row[3]
        password = gen_pass()
        writer.writerow([first_name, last_name, email, password])
