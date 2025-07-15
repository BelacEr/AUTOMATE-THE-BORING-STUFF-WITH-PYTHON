def addToInventory(inventory, addedItems):
    for item in addedItems:
        # If the item already exists in inventory, increment its count
        if item in inventory:
            inventory[item] += 1
        # If it's a new item, add it to inventory with count 1
        else:
            inventory[item] = 1
    return inventory

# The displayInventory function from before
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

# Example usage
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)