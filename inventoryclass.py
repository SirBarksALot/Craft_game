class Inventory:
    def __init__(self):
        self.inventory_item = []
        self.inventory_amount = []

    def inventory_populate(self, item, amount):
        self.inventory_item.append(item)
        self.inventory_amount.append(amount)

    def inventory_space_add(self, space_add):  # adds space to the inventory 'empty' : 0
        for i in range(space_add):
            self.inventory_populate('empty', 0)

    def add_to_inventory(self, item, amount):  # adds amount of items to inventory
        if item in self.inventory_item:  # checks if item is already in inventory if it does, increase amount
            self.inventory_amount[self.inventory_item.index(item)] += amount
        else:  # if not then adds them
            self.inventory_populate(item, amount)

    def subtract_from_inventory(self, item, amount):  # deletes amount of items from inventory
        self.inventory_amount[self.inventory_item.index(item)] += amount

    def print(self):
        for i in range(len(self.inventory_item)):
            print(self.inventory_item[i] + ' : ' + str(self.inventory_amount[i]))

        print('end of inventory')


bag = Inventory()

bag.inventory_space_add(4)
bag.print()
bag.inventory_space_add(3)
bag.print()
