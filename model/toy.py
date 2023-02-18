class Toy:
    total = 0

    @staticmethod
    def status():
        return Toy.total

    def __init__(self, name, weight=0, price=0, ageing=0, rating=0):
        self.__name = name
        self.__weight = weight
        self.__price = price
        self.__ageing = ageing
        self.__rating = rating
        Toy.total += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_ageing(self):
        return self.__ageing

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def __str__(self):
        return self.__name + ":weight = " + str(self.__weight) + ", price = " + str(self.__price) + ", age for " + str(
            self.__ageing) + ", rating = " + str(self.__rating)

    def __del__(self):
        print(self.__name + " : toy deleted")
