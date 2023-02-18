from model.toy import Toy


class Wood_toy(Toy):
    def __init__(self, name, weight, price, ageing, rating, isWeapon, isComposite):
        super().__init__(name, weight, price, ageing, rating)
        self.__isWeapon = isWeapon
        self.__isComposite = isComposite

    def isWeapon(self):
        return self.__isWeapon

    def set_isWeapon(self, isWeapon):
        self.__isWeapon = isWeapon

    def isComposite(self):
        return self.__isComposite

    def set_isComposite(self, isComposite):
        self.__isComposite = isComposite

    def __str__(self):
        return str(type(self).__name__) + " " + super().__str__() + ", is weapon? = " + str(self.isWeapon()) +\
               ", is composite? = " + str(self.isComposite())