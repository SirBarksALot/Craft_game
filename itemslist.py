from itemclass import Item as Item

# basic mats
wood = Item('Wood', True, False, False, True, {})
sand = Item('Sand', True, False, False, True, {})
coal = Item('Coal', True, False, False, True, {})
wool = Item('Wool', True, False, False, True, {})
thread = Item('Thread', True, False, False, True, {})
bone = Item('Bone', True, False, False, True, {})
honey = Item('Honey', True, False, False, True, {})

# ores
iron_ore = Item('Iron ore', True, False, False, True, {})
malachite_ore = Item('Malachite ore', False, False, False, True, {})

# metals
iron_bar = Item('Iron bar', False, False, True, False, {iron_ore: 5, coal: 4, wood: 3})
steel_bar = Item('Steel bar', False, False, True, False, {iron_bar: 3, coal: 10, wood: 2})
malachite = Item('Malachite', False, False, True, False, {malachite_ore: 3})

# keymats
wolf_claw = Item('Wolf claw', False, False, False, True, {})
eagle_talon = Item('Eagle talon', False, False, False, True, {})
dragon_claw = Item('Dragon claw', False, False, False, True, {})
wraith_nail = Item('Wraith nail', False, False, False, True, {})

# weapons
wooden_claw = \
    Item('Wooden claw', True, False, True, True, {wood: 50})
iron_claw = \
    Item('Iron claw', False, False, True, True, {wooden_claw: 1, wolf_claw: 6, iron_bar: 20, wood: 25})
steel_claw = \
    Item('Steel claw', False, True, True, True, {eagle_talon: 8, steel_bar: 25, iron_bar: 10, wood: 40})
