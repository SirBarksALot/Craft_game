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
            self.name += str(enchant)
