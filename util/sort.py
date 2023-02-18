class Sort:
    @staticmethod
    def sort(game_room):
        return game_room.sort()

class Name_sort(Sort):
    @staticmethod
    def sort(game_room):
        return game_room.get_list().sort(key=lambda x: x.get_name())

class Weight_sort(Sort):
    @staticmethod
    def sort(game_room):
        return game_room.get_list().sort(key=lambda x: x.get_weight())

class Price_sort(Sort):
    @staticmethod
    def sort(game_room):
        return game_room.get_list().sort(key=lambda x: x.get_price())
