def displayInventory(inventory):
    """
    Displays each item in the inventory with its count, and then the total count of all items.
    """
    print("Inventory:")
    total_items = 0
    # Loop through the dictionary to print items and calculate the total
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print("Total number of items: " + str(total_items))

def addToInventory(inventory, addedItems):
    """
    Updates the inventory with new items from the dragon's loot.
    If the item is already in the inventory, increases the quantity.
    If not, adds the item to the inventory.
    """
    # Process each item in the addedItems list
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print('Inventory updated!')
    return inventory

def main():
    """
    Main function to manage the game inventory and simulate item looting.
    """
    # Initial setup of the player's inventory
    current_inventory = {'rope': 1, 'gold coin': 42, 'dagger': 1}
    # Items found after defeating a dragon
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    print("Initial Inventory:")
    displayInventory(current_inventory)

    print('\nThe dragon has been vanquished! Collecting loot...')
    current_inventory = addToInventory(current_inventory, dragon_loot)

    print("\nUpdated Inventory:")
    displayInventory(current_inventory)

# Run the main function
main()
