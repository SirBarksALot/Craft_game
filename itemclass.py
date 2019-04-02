# to create Item class object simply:
# apple_juice = Item('Apple juice', True, False, True, False, {apple : 3, cold_water : 1})
# where 'Apple juice' is a display name, then common_shop=True, secret_shop = False, craft = True, drop = False
# and craft requirements are 3 apple objects and 1 water object

# to print an attribute:
# 1.
# apple_juice.print('name', 0)
# OUTPUT:
# Apple juice
# 2.
# apple_juice.print('requirements_dictionary', 0)
# OUTPUT:
# Apple => 3
# Cold Water => 1:
#     Water => 1
#     Ice => 2
# where 'name' is the attribute and 0 is the starting indent level (for nicely looking craft tree)

# in order to increase enchant level:
# apple_juice.enchant_level(3)
# apple_juice.print('name', 0)
# OUTPUT:
# Apple juice +3


class Item:
    def __init__(self, name, common_shop, secret_shop, craft, drop, requirements_dictionary):
        self.name = name
        self.common_shop = common_shop
        self.secret_shop = secret_shop
        self.craft = craft
        self.drop = drop
        self.requirements_dictionary = requirements_dictionary
        print('Creating {}'.format(self.name))

    def __str__(self):
        return self.name

    def __bool__(self):
        return bool(self.requirements_dictionary)

    @staticmethod
    def depth_level_transform(depth_level):  # transform depth_level_for_indent into --
        output_indent = ''
        for i in range(depth_level):
            output_indent += '    '

        return output_indent

    def print(self, what_to_print, depth_level_indent):
        if type(self.__getattribute__(what_to_print)) is dict:  # check if an attribute is a dictionary
            if self.__getattribute__(what_to_print).items():  # check if an object's requirements_dict isn't empty
                for key, value in self.__getattribute__(what_to_print).items():  # looping through dictionary
                    print('{}{} => {}'.format(self.depth_level_transform(depth_level_indent), key, value), end='')
                    if key.__getattribute__(what_to_print).items():  # check if object's req_dict isn't empty
                        depth_level_indent += 1
                        print(':', end='\n')
                        key.print(what_to_print, depth_level_indent)
                        depth_level_indent -= 1
                    else:
                        print('')
            else:
                print('basic')
        else:
            print(self.__getattribute__(what_to_print))

    def enchant_level(self, enchant):
        if enchant > 0:
            enchant = ' +' + str(enchant)
            self.name += enchant
