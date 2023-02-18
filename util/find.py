class Find:
    @staticmethod
    def find(game_room, value):
        return game_room.find()


class Name_find(Find):
    @staticmethod
    def find(game_room, value):
        for toy in game_room.get_list():
            if value == toy.get_name():
                return toy
        return "There is no toy with such data"


class Weight_find(Find):
    @staticmethod
    def find(game_room, value):
        for toy in game_room.get_list():
            if value == toy.get_weight():
                return toy
        return "There is no toy with such data"


class Price_find(Find):
    @staticmethod
    def find(game_room, value):
        for toy in game_room.get_list():
            if value == toy.get_price():
                return toy
        return "There is no toy with such data"
