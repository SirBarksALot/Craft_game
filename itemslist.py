import itemclass

# basic mats
wood = itemclass.Item('Wood', True, False, False, True, {})
sand = itemclass.Item('Sand', True, False, False, True, {})
coal = itemclass.Item('Coal', True, False, False, True, {})
wool = itemclass.Item('Wool', True, False, False, True, {})
thread = itemclass.Item('Thread', True, False, False, True, {})
bone = itemclass.Item('Bone', True, False, False, True, {})
honey = itemclass.Item('Honey', True, False, False, True, {})

# ores
iron_ore = itemclass.Item('Iron ore', True, False, False, True, {})
malachite_ore = itemclass.Item('Malachite ore', False, False, False, True, {})

# metals
iron_bar = itemclass.Item('Iron bar', False, False, True, False, {iron_ore: 5, coal: 4, wood: 3})
steel_bar = itemclass.Item('Steel bar', False, False, True, False, {iron_bar: 3, coal: 10, wood: 2})
malachite = itemclass.Item('Malachite', False, False, True, False, {malachite_ore: 3})

# keymats
wolf_claw = itemclass.Item('Wolf claw', False, False, False, True, {})
eagle_talon = itemclass.Item('Eagle talon', False, False, False, True, {})
dragon_claw = itemclass.Item('Dragon claw', False, False, False, True, {})
wraith_nail = itemclass.Item('Wraith nail', False, False, False, True, {})

# weapons
wooden_claw = \
    itemclass.Item('Wooden claw', True, False, True, True, {wood: 50})
iron_claw = \
    itemclass.Item('Iron claw', False, False, True, True, {wooden_claw: 1, wolf_claw: 6, iron_bar: 20, wood: 25})
steel_claw = \
    itemclass.Item('Steel claw', False, True, True, True, {eagle_talon: 8, steel_bar: 25, iron_bar: 10, wood: 40})
