class Item:
    def __init__(self, name, commonshop, secretshop, craftable, drop, requirementsdictionary):
        self.name = name
        self.commonshop = commonshop
        self.secretshop = secretshop
        self.craftable = craftable
        self.drop = drop
        self.requirementsdictionary = requirementsdictionary

    def __str__(self):
        return self.name

    def __bool__(self):
        return bool(self.requirementsdictionary)

    @staticmethod
    def depthleveltransform(depthlevel):  # transform depthlevelforindent into --
        outputindent = ''
        for i in range(depthlevel):
            outputindent += '--'

        return outputindent

    def print(self, whattoprint, depthlevelforindent):
        if whattoprint in vars(self):  # check if requested attribute is in this object
            if type(self.__getattribute__(whattoprint)) is dict:  # check if an attribute is a dictionary
                if self.__getattribute__(whattoprint).items():  # check if an object's requirementsdict isn't empty
                    for key, value in self.__getattribute__(whattoprint).items():  # looping through dictionary
                        print('{}{} => {}'.format(self.depthleveltransform(depthlevelforindent), key, value), end='')
                        if key.__getattribute__(whattoprint).items():  # check if an object's requirementsdict isn't empty
                            depthlevelforindent += 1
                            print(':', end='\n')
                            key.print(whattoprint, depthlevelforindent)
                            depthlevelforindent -= 1
                        else:
                            print(' basic')
                else:
                    print('basic')
            else:
                print(self.__getattribute__(whattoprint))
        else:
            print('No attribute named + {} + found!'.format(whattoprint))
