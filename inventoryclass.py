class Inventory:
    def __init__(self):
        self.inventory_item = []
        self.inventory_amount = []

    def inventory_populate(self, item, amount):  # supplementary function for inventory_space_add
        self.inventory_item.append(item)
        self.inventory_amount.append(amount)

    def inventory_space_add(self, space_add):  # adds space to the inventory ('empty' : None)
        for i in range(space_add):
            self.inventory_populate('empty', None)

    def inventory_space_check(self):
        if 'empty' in self.inventory_item:
            print('Enough space in inventory!')
            return True
        else:
            print('Inventory full')
            return False

    def item_place(self, item):
        place = self.inventory_item.index(item)
        return place

    def add_to_inventory(self, item, amount):  # adds amount of item to inventory
        if item in self.inventory_item:  # checks if item is already in inventory if it does, increase amount
            self.inventory_amount[self.item_place(item)] += amount
        else:  # if not then adds them to first 'empty' bracket
            if self.inventory_space_check():  # checks if there is a space in inventory
                first_empty_place = self.item_place('empty')  # finds first empty spot
                self.inventory_item[first_empty_place] = item
                self.inventory_amount[first_empty_place] = amount

    def subtract_from_inventory(self, item, amount):  # deletes amount of items from inventory
        place = self.item_place(item)
        if self.inventory_amount[place] < amount:  # checks if item amount > deletion amount
            print('Amount of an item is insufficient to subtract!')
        else:
            self.inventory_amount[place] -= amount  # subtract from item's amount
            if self.inventory_amount[place] == 0:  # if item's count is 0 then reset bracket
                self.inventory_item[place] = 'empty'

    def print(self):
        for i in range(len(self.inventory_item)):
            print(self.inventory_item[i] + ' : ' + str(self.inventory_amount[i]))


bag = Inventory()

bag.inventory_space_add(3)
bag.add_to_inventory('Wood', 10)
bag.print()
bag.add_to_inventory('Wood', 5)
bag.print()
bag.add_to_inventory('Thread', 8)
bag.print()
bag.add_to_inventory('Slime', 3)
bag.print()
bag.add_to_inventory('Coal', 1)
bag.print()
bag.subtract_from_inventory('Slime', 3)
bag.print()
bag.subtract_from_inventory('Thread', 16)
bag.print()
bag.add_to_inventory('Coal', 1)
bag.print()
