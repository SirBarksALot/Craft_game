from inventoryclass import Inventory as Inv
from itemslist import items_list as items_list
from itemslist import items_req_dict_list as items_req_dict_list

inv_1 = Inv(4)  # creating inventory with empty space
inv_1.add_to_inventory('Wood', 10)
inv_1.add_to_inventory('Coal', 10)
inv_1.add_to_inventory('Iron Ore', 5)
inv_1.print()
print('')


def craft_function(craft_item, inventory):
    i = items_list.index(craft_item)  # finding index of crafted item
    var_1 = True

    for key, value in items_req_dict_list[i].items():  # looping through requirements dictionary
        if inventory.check_item_amount_in_inventory(key, value):  # checks if amount of required item is in inventory
            pass
        else:
            var_1 = False

    if var_1 is True:
        for key, value in items_req_dict_list[i].items():  # looping through requirements dictionary
            inventory.subtract_from_inventory(key, value)  # subtracting items required for a craft

        inventory.add_to_inventory(craft_item, 1)  # adding crafted item to inventory

    return


craft_function('Iron bar', inv_1)
inv_1.print()
