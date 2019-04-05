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


class Item:
    def __init__(self, name, options_list, requirements_dictionary):
        self.name = name
        self.common_shop = options_list[0]
        self.secret_shop = options_list[1]
        self.craft = options_list[2]
        self.drop = options_list[3]
        self.enchant = options_list[4]
        self.requirements_dictionary = requirements_dictionary
        if self.enchant is True:
            self.enchant_level = 0

    def __str__(self):
        if self.enchant is True and self.enchant_level > 0:
                return self.name + ' +' + str(self.enchant_level)

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


class WeaponItem(Item):
    def __init__(self, name, options_list, requirements_dictionary):
        self.enchant_level = 0
        self.attack_power = 0
        super().__init__(name, options_list, requirements_dictionary)

    def enchant_fct(self):
        self.enchant_level += 1
