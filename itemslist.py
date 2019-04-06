# creating item template:
# item = object_class('Display name', \
# boolean_list[common_shop, secret_shop, craft, drop, enchant], {requirements_dictionary})



items_list = []  # creating empty items_list
items_req_dict_list = []  # empty requirements dictionary list

def add_an_item_to_items_list(working_list, item, req_dict):
    working_list.append(item)
    items_req_dict_list.append(req_dict)

    return working_list, items_req_dict_list


add_an_item_to_items_list(items_list, 'Wood', {})
add_an_item_to_items_list(items_list, 'Coal', {})
add_an_item_to_items_list(items_list, 'Iron ore', {})
add_an_item_to_items_list(items_list, 'Iron bar', {'Wood': 2, 'Coal': 4, 'Iron Ore': 5})
add_an_item_to_items_list(items_list, 'Wooden claw', {'Wood': 50})
add_an_item_to_items_list(items_list, 'Iron claw', {'Wood': 25, 'Iron Bar': 15, 'Wooden claw': 1})


def depth_level_transform(depth_level):  # transform depth_level_for_indent into --
    output_indent = ''
    for i in range(depth_level):
        output_indent += '    '

    return output_indent


def indent_print(var_1, global_list, global_list_of_req_dic, depth_level_indent):
    print('{}{}:'.format(depth_level_transform(depth_level_indent), global_list[var_1]))
    temp_dict_var = global_list_of_req_dic[var_1]

    if not temp_dict_var:  # check if an item's dictionary is empty
        print(' - basic')
    else:
        depth_level_indent += 1
        for key, value in temp_dict_var.items():  # looping through dictionary
            i = global_list.index(key)
            print('{}{} => {}'.format(depth_level_transform(depth_level_indent), key, value))
            if global_list_of_req_dic[i]:  # check if object's req_dict isn't empty
                indent_print(i, global_list, global_list_of_req_dic, depth_level_indent)

    return


# from item class import Item as Item
# from item class import WeaponItem as WeaponItem

# basic mats
# wood = Item('Wood', [True, False, False, True, False], {})
# sand = Item('Sand', [True, False, False, True, False], {})
# coal = Item('Coal', [True, False, False, True, False], {})
# wool = Item('Wool', [True, False, False, True, False], {})
# thread = Item('Thread', [True, False, False, True, False], {})
# bone = Item('Bone', [True, False, False, True, False], {})
# honey = Item('Honey', [True, False, False, True, False], {})

# ores
# iron_ore = Item('Iron ore', [True, False, False, True, False], {})
# malachite_ore = Item('Malachite ore', [False, False, False, True, False], {})

# metals
# iron_bar = Item('Iron bar', [False, False, True, False, False], {iron_ore: 5, coal: 4, wood: 3})
# steel_bar = Item('Steel bar', [False, False, True, False, False], {iron_bar: 3, coal: 10, wood: 2})
# malachite = Item('Malachite', [False, False, True, False, False], {malachite_ore: 3})

# key mats
# wolf_claw = Item('Wolf claw', [False, False, False, True, False], {})
# eagle_talon = Item('Eagle talon', [False, False, False, True, False], {})
# dragon_claw = Item('Dragon claw', [False, False, False, True, False], {})
# wraith_nail = Item('Wraith nail', [False, False, False, True, False], {})

# weapons
# wooden_claw = \
    # WeaponItem('Wooden claw', [True, False, True, True, True], {wood: 50})
# iron_claw = \
    # WeaponItem('Iron claw', [False, False, True, True, True], {wooden_claw: 1, wolf_claw: 6, iron_bar: 20, wood: 25})
# steel_claw = \
    # WeaponItem('Steel claw', [False, True, True, True, True], {eagle_talon: 8, steel_bar: 25, iron_bar: 10, wood: 40})
