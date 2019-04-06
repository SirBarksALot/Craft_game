# to create Inventory class object simply:
# bag = Inventory()

# to add space to an existing inventory use:
# bag.inventory_space_add(x)
# where x is an amount of bracket you want to add

# to check whether there is enough space in inventory use:
# bag.inventory_space_check() method

# to check an index of a particular item use:
# bag.item_place(item) method
# where item is an item you are looking for a place of

# to add an item to an existing inventory use:
# bag.add_to_inventory('Wood', 10)
# where 'Wood' is an item and 10 is it's amount

# to subtract an item to an existing inventory use:
# bag.subtract_from_inventory('Slime', 5)
# where 'Slime' is an item from which you want to subtract 5 instances

# to check whether item exists in inventory use:
# bag.check_if_item_exists_in_inventory(search_item)
# where search_item is an item you are looking for

# to check whether amount of specific item is in inventory use:
# bag.check_item_amount_in_inventory(search_item, search_amount)
# where search_item is an item you are looking for and search_amount is the amount you are requesting to check
# note that this method first calls check_if_item_exists_in_inventory method

# to print whole inventory use:
# bag.print()


class Inventory:
    def __init__(self, space):  # inventory object constructor
        self.inventory_item = []
        self.inventory_amount = []
        self.inventory_space_add(space)  # create space long empty inventory

    def inventory_populate(self, item, amount):  # supplementary function for inventory_space_add
        self.inventory_item.append(item)
        self.inventory_amount.append(amount)

    def inventory_space_add(self, space_add):  # adds space to the inventory ('empty' : None)
        for i in range(space_add):
            self.inventory_populate('empty', None)

    def inventory_space_check(self):
        if 'empty' in self.inventory_item:
            return True
        else:
            return False

    def item_place(self, item):
        place = self.inventory_item.index(item)
        return place

    def add_to_inventory(self, item, amount):  # adds amount of item to inventory
        if item in self.inventory_item:  # checks if item is already in inventory if it does, increase amount
            self.inventory_amount[self.item_place(item)] += amount
        else:  # if not then adds them to first 'empty' bracket
            if self.inventory_space_check():  # checks if there is a space in inventory, otherwise return False
                first_empty_place = self.item_place('empty')  # finds first empty spot
                self.inventory_item[first_empty_place] = item
                self.inventory_amount[first_empty_place] = amount
            else:
                return False

    def subtract_from_inventory(self, item, amount):  # deletes amount of items from inventory
        place = self.item_place(item)
        if self.inventory_amount[place] < amount:  # checks if item amount > deletion amount
            print('Insufficient amount of {} to subtract from!'.format(item))
        else:
            self.inventory_amount[place] -= amount  # subtract from item's amount
            if self.inventory_amount[place] == 0:  # if item's count is 0 then reset bracket
                self.inventory_item[place] = 'empty'

    def check_if_item_exists_in_inventory(self, search_item):
        if search_item in self.inventory_item:
            return True
        else:
            print('No {} in inventory.'.format(search_item))
            return False

    def check_item_amount_in_inventory(self, search_item, search_amount):
        if self.check_if_item_exists_in_inventory(search_item):
            i = self.item_place(search_item)
            if self.inventory_amount[i] >= search_amount:
                return True
            else:
                var_1 = search_amount - self.inventory_amount[i]
                print('Not enough {} in inventory, you need {} more.'.format(search_item, var_1))
                return False
        else:
            return False

    def print(self):
        for i in range(len(self.inventory_item)):
            print(self.inventory_item[i] + ' : ' + str(self.inventory_amount[i]))
