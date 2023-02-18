from model.toy import Toy


class Assistant:
    @staticmethod
    def calculate_common_weight(game_room):
        common_weight = 0
        for toy in game_room.get_list():
            if isinstance(toy, Toy):
                common_weight += toy.get_weight()
        return common_weight

    @staticmethod
    def calculate_common_price(game_room):
        common_price = 0
        for toy in game_room.get_list():
            if isinstance(toy, Toy):
                common_price += toy.get_price()
        return common_price

    @staticmethod
    def find_most_expensive_toy(game_room):
        most_expensive_toy_index = 0
        list = game_room.get_list()

        for toy in range(len(list)):
            if isinstance(toy, Toy):
                if list[most_expensive_toy_index].get_price() <= list[toy].get_price():
                    most_expensive_toy_index = toy

        return most_expensive_toy_index
