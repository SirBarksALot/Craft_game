from inventoryclass import Inventory as Inv
from itemslist import items_list as items_list
from itemslist import items_req_dict_list as items_req_dict_list

inv_1 = Inv(5)  # creating inventory with empty space
inv_1.add_to_inventory('Wood', 49)
inv_1.add_to_inventory('Coal', 40)
inv_1.add_to_inventory('Iron Ore', 45)
inv_1.print()
print('')


def craft_function(craft_item, inventory):
    var_1 = items_list.index(craft_item)  # finding index of an item we want to craft in items_list
    var_2 = items_req_dict_list[var_1].items()
    var_3 = True

    for key, value in var_2:  # looping through requirements dictionary
        if inventory.check_item_amount_in_inventory(key, value):  # checks if amount of required item is in inventory
            pass
        else:
            var_3 = False

    if var_3 is True:
        for key, value in var_2:  # looping through requirements dictionary
            inventory.subtract_from_inventory(key, value)  # subtracting items required for a craft

        if inventory.inventory_space_check() is True:  # check if there is an empty place in inventory
            inventory.add_to_inventory(craft_item, 1)  # adding crafted item to inventory
        else:  # if no place in inventory, even after subtract, then give back items
            print('here')
            for key, value in var_2:
                inventory.add_to_inventory(key, value)

    return


craft_function('Wooden claw', inv_1)
# craft_function('Iron bar', inv_1)
inv_1.print()
