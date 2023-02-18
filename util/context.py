from util.sort import Sort, Name_sort
from util.find import Find


class Context:
    __sort_type: Sort
    __find_type: Find

    def set_sort_type(self, sort_type):
        self.__sort_type = sort_type

    def execute_sorting(self, game_room):
        if self.__sort_type:
            self.__sort_type.sort(game_room)
        else:
            Name_sort.sort(game_room)

    def set_find_type(self, find_type):
        self.__find_type = find_type

    def execute_finding(self, game_room, value):
        if self.__find_type:
            return self.__find_type.find(game_room, value)
        else:
            return "Filter is empty"

