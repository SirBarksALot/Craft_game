# adding an item to the list:
# add_an_item_to_items_list(index, 'Name_1', {'Name_2: amount', 'Name_3': amount})
# where index is a place in a list, Name_1 is a name of an item and {} is a dictionary of craft requirements


items_list = []  # creating empty items_list
items_req_dict_list = []  # empty requirements dictionary list


def add_an_item_to_items_list(item, req_dict):
    items_list.append(item)
    items_req_dict_list.append(req_dict)

    return items_list, items_req_dict_list


# basic mats
add_an_item_to_items_list('Wood', {})
add_an_item_to_items_list('Coal', {})
add_an_item_to_items_list('Sand', {})
add_an_item_to_items_list('Wool', {})
add_an_item_to_items_list('Thread', {})
add_an_item_to_items_list('Bone', {})
add_an_item_to_items_list('Honey', {})

# ores
add_an_item_to_items_list('Iron ore', {})
add_an_item_to_items_list('Malachite ore', {})

# key mats
add_an_item_to_items_list('Wolf claw', {})
add_an_item_to_items_list('Eagle talon', {})
add_an_item_to_items_list('Dragon claw', {})
add_an_item_to_items_list('Wraith nail', {})

# metals
add_an_item_to_items_list('Iron bar', {'Wood': 2, 'Coal': 4, 'Iron ore': 5})
add_an_item_to_items_list('Steel bar', {'Wood': 1, 'Coal': 6, 'Iron ore': 4, 'Iron bar': 3})
add_an_item_to_items_list('Malachite bar', {'Wood': 1, 'Coal': 5, 'Malachite ore': 5})

# weapons
add_an_item_to_items_list('Wooden claw', {'Wood': 50})
add_an_item_to_items_list('Iron claw', {'Wood': 10, 'Coal': 25, 'Iron bar': 10, 'Wolf claw': 6, 'Wooden claw': 1})
add_an_item_to_items_list('Steel claw', {'Wood': 15, 'Coal': 35, 'Steel bar': 8, 'Eagle talon': 8})


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
