'''
    CIS188 Sample Program
    This program is a companion sample for Lab 10

    You can use this program as a template to start
    or copy/paste the gen_pass() function definition
    into your own .py file

    Author: Professor McInstructor
'''

import random

# Length of the generated password
PASS_LENGTH = 16

# Number of passwords to generate
NUM_PASS = 10

# Function definition for gen_pass()
# Generate a password of size length using all ascii letters, numbers 0-9,
# and a subset of special characters
# A localized import is included for the string library
# The randomly generated passedword is returned
def gen_pass(length):
    import string
    all = string.ascii_letters + string.digits + '!@$%^&*-_+=~<>/\(){}[]?|'
    password = "".join(random.sample(all,length))
    return password

# For loop demonstrates calling the function and displaying the returned value
# This code is for demo only, please modify the program to meet lab requirements
for i in range(NUM_PASS):
    returned_value = gen_pass(PASS_LENGTH)
    print('The returned value #' + str(i+1)+ ' is ' + str(returned_value))
