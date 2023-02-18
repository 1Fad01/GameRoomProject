from model.toy import Toy


class Plastic_toy(Toy):
    def __init__(self, name, weight, price, ageing, rating, color, isElectric):
        super().__init__(name, weight, price, ageing, rating)
        self.__color = color
        self.__isElectric = isElectric

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def isElectric(self):
        return self.__isElectric

    def set_isElectric(self, isElectric):
        self.__isElectric = isElectric

    def __str__(self):
        return str(type(self).__name__) + " " + super().__str__() + ", color = " + str(self.get_color()) +\
               ", is electric? - " + str(self.isElectric())
