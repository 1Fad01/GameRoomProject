from model.toy import Toy


class Soft_toy(Toy):
    def __init__(self, name, weight, price, ageing, rating, isFluffy, size):
        super().__init__(name, weight, price, ageing, rating)
        self.__isFluffy = isFluffy
        self.__size = size

    def isFluffy(self):
        return self.__isFluffy

    def set_isFluffy(self, isFluffy):
        self.__isFluffy = isFluffy

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def __str__(self):
        return str(type(self).__name__) + " " + super().__str__() + ", size = " + str(self.get_size()) +\
               ", is fluffy? = " + str(self.isFluffy())

