import random

from model.plastic_toy import Plastic_toy
from model.soft_toy import Soft_toy
from model.toy import Toy
from model.wood_toy import Wood_toy


class Factory:
    WOOD_TOY_TYPE = 0
    SOFT_TOY_TYPE = 1
    PLASTIC_TOY_TYPE = 2
    LIST_OF_BOOL = [True, False]

    @staticmethod
    def create_toys(number):
        names = ["Box", "Car", "Rabbit", "Fox", "Cubes", "Lego"]
        colors = ["Red", "Yellow", "Blue", "Green"]
        list_of_toys = []

        for i in range(number):
            name = random.choice(names)
            type = random.randint(0, 2)
            weight = random.randint(100, 1000)
            price = random.randint(10, 100)
            ageing = random.randint(0, 24)
            rating = round(random.uniform(0, 5), 2)

            if type == Factory.WOOD_TOY_TYPE:
                isWeapon = Factory.__get_random_bool()
                isComposite = Factory.__get_random_bool()
                list_of_toys.append(Wood_toy(name, weight, price, ageing, rating, isWeapon, isComposite))
            elif type == Factory.SOFT_TOY_TYPE:
                isFluffy = Factory.__get_random_bool()
                size = random.randint(1, 250)
                list_of_toys.append(Soft_toy(name, weight, price, ageing, rating, isFluffy, size))
            elif type == Factory.PLASTIC_TOY_TYPE:
                isElectric = Factory.__get_random_bool()
                color = random.choice(colors)
                list_of_toys.append(Plastic_toy(name, weight, price, ageing, rating, color, isElectric))

        list_of_toys.append(Toy("Baltuska"))
        return list_of_toys

    @staticmethod
    def __get_random_bool():
        return random.choice(Factory.LIST_OF_BOOL)
