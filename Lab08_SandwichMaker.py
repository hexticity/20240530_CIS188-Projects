

import pyinputplus as pyip

# Prices for each option
prices = {
    'bread': {'wheat': 1.0, 'white': 1.0, 'sourdough': 1.5},
    'protein': {'chicken': 2.0, 'turkey': 2.5, 'ham': 2.0, 'tofu': 1.5},
    'cheese': {'cheddar': 0.5, 'swiss': 0.5, 'mozzarella': 0.75},
    'extras': {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.5, 'tomato': 0.5}
}

def get_sandwich_preference():
    # Get user's sandwich preferences

    # Ask for bread type using inputMenu() to provide a selection list
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Choose your bread type:\n')

    # Ask for protein type using inputMenu() to provide a selection list
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Choose your protein type:\n')

    # Ask if the user wants cheese using inputYesNo() for yes/no question
    cheese_choice = pyip.inputYesNo('Do you want cheese? (yes or no)\n')

    # If user wants cheese, ask for the type of cheese
    if cheese_choice == 'yes':
        cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt='Choose your cheese type:\n')
    else:
        cheese = None

    # Ask for additional extras (mayo, mustard, lettuce, tomato) using inputYesNo()
    extras = []
    for extra in ['mayo', 'mustard', 'lettuce', 'tomato']:
        if pyip.inputYesNo(f'Do you want {extra}? (yes or no)\n') == 'yes':
            extras.append(extra)

    # Ask for the number of sandwiches using inputInt() with a minimum value of 1
    num_sandwiches = pyip.inputInt('How many sandwiches would you like to order?\n', min=1)

    return bread, protein, cheese, extras, num_sandwiches

def calculate_cost(bread, protein, cheese, extras, num_sandwiches):
    # Calculate total cost of the sandwich based on user's choices

    # Start with the cost of bread and protein
    total_cost = prices['bread'][bread] + prices['protein'][protein]

    # Add cost of cheese if selected
    if cheese:
        total_cost += prices['cheese'][cheese]

    # Add cost of each extra
    for extra in extras:
        total_cost += prices['extras'][extra]

    # Multiply by the number of sandwiches
    return total_cost * num_sandwiches

def display_order_summary(bread, protein, cheese, extras, num_sandwiches, total_cost):
    # Display the order summary in a user-friendly format
    print('\nOrder Summary:')
    print(f'Bread: {bread}')
    print(f'Protein: {protein}')
    if cheese:
        print(f'Cheese: {cheese}')
    else:
        print('Cheese: None')
    if extras:
        print('Extras: ' + ', '.join(extras))
    else:
        print('Extras: None')
    print(f'Number of sandwiches: {num_sandwiches}')
    print(f'Total cost: ${total_cost:.2f}')

# Start of the program
print('Welcome to the Sandwich Maker!')

# Get the user's sandwich preferences
bread, protein, cheese, extras, num_sandwiches = get_sandwich_preference()

# Calculate the total cost based on the user's preferences
total_cost = calculate_cost(bread, protein, cheese, extras, num_sandwiches)

# Display the summary of the order with the total cost
display_order_summary(bread, protein, cheese, extras, num_sandwiches, total_cost)


