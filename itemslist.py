# creating item template:
# item = object_class('Display name', \
# boolean_list[common_shop, secret_shop, craft, drop, enchant], {requirements_dictionary})

from itemclass import Item as Item
from itemclass import WeaponItem as WeaponItem

# basic mats
wood = Item('Wood', [True, False, False, True, False], {})
sand = Item('Sand', [True, False, False, True, False], {})
coal = Item('Coal', [True, False, False, True, False], {})
wool = Item('Wool', [True, False, False, True, False], {})
thread = Item('Thread', [True, False, False, True, False], {})
bone = Item('Bone', [True, False, False, True, False], {})
honey = Item('Honey', [True, False, False, True, False], {})

# ores
iron_ore = Item('Iron ore', [True, False, False, True, False], {})
malachite_ore = Item('Malachite ore', [False, False, False, True, False], {})

# metals
iron_bar = Item('Iron bar', [False, False, True, False, False], {iron_ore: 5, coal: 4, wood: 3})
steel_bar = Item('Steel bar', [False, False, True, False, False], {iron_bar: 3, coal: 10, wood: 2})
malachite = Item('Malachite', [False, False, True, False, False], {malachite_ore: 3})

# key mats
wolf_claw = Item('Wolf claw', [False, False, False, True, False], {})
eagle_talon = Item('Eagle talon', [False, False, False, True, False], {})
dragon_claw = Item('Dragon claw', [False, False, False, True, False], {})
wraith_nail = Item('Wraith nail', [False, False, False, True, False], {})

# weapons
wooden_claw = \
    Item('Wooden claw', [True, False, True, True, True], {wood: 50})
iron_claw = \
    Item('Iron claw', [False, False, True, True, True], {wooden_claw: 1, wolf_claw: 6, iron_bar: 20, wood: 25})
steel_claw = \
    WeaponItem('Steel claw', [False, True, True, True, True], {eagle_talon: 8, steel_bar: 25, iron_bar: 10, wood: 40})
