from multipledispatch import dispatch

from model.Game_room import GameRoom
from model.toy import Toy


class Printer:

    @staticmethod
    @dispatch(list)
    def print(list_of_toys):
        for toy in list_of_toys:
            print(toy)

    @staticmethod
    @dispatch(GameRoom)
    def print(game_room):
        for toy in game_room.get_list():
            print(toy)


    @staticmethod
    @dispatch(str, Toy)
    def print(label, toy):
        print(label, toy)

    @staticmethod
    @dispatch(str, str)
    def print(label, label2):
        print(label, label2)

    @staticmethod
    @dispatch(str, int)
    def print(label, number):
        print(label + str(number))

    @staticmethod
    @dispatch(str)
    def print(label):
        print(label)

    @staticmethod
    def print_empty_line():
        print("\n")

