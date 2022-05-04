import copy, pprint

def addToInventory(inventory, addedItems):
    ret_inventory = copy.deepcopy(inventory)
    for item in addedItems:
        if item in ret_inventory:
            ret_inventory[item] += 1
        else:
            ret_inventory[item] = 1
    return ret_inventory

def displayInventory(inventory):
    print("Inventory:")
    for item, count in inventory.items():
        print("{} {}".format(count, item))

    print("\nTotal number of items: {}".format(sum(inventory.values())))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
