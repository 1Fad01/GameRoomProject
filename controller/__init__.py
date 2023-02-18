from veiw import Printer
from model.Game_room import GameRoom

from util import *


def main():
    number = int(input("Enter a number of toys: "))
    list_of_toys = Factory.create_toys(number)
    Printer.print_empty_line()

    game_room = GameRoom(list_of_toys)

    Printer.print(game_room)
    Printer.print_empty_line()
    Printer.print("Common price: ", Assistant.calculate_common_price(game_room))
    Printer.print("Common weight: ", Assistant.calculate_common_weight(game_room))
    Printer.print("The most expensive toy: ", list_of_toys[Assistant.find_most_expensive_toy(game_room)])
    Printer.print_empty_line()

    context = Context()

    context.set_sort_type(Price_sort())
    context.execute_sorting(game_room)
    Printer.print("After price sorting")
    Printer.print(game_room)
    Printer.print_empty_line()

    context.set_sort_type(Weight_sort())
    context.execute_sorting(game_room)
    Printer.print("After Weight sorting")
    Printer.print(game_room)
    Printer.print_empty_line()

    context.set_sort_type(Name_sort())
    context.execute_sorting(game_room)
    Printer.print("After name sorting")
    Printer.print(game_room)
    Printer.print_empty_line()

    value = input("Enter the name of the toy you want to find: ")
    context.set_find_type(Name_find())
    Printer.print("Find by name: ",context.execute_finding(game_room, value))
    Printer.print_empty_line()

    value = int(input("Enter the weight of the toy you want to find: "))
    context.set_find_type(Weight_find())
    Printer.print("Find by weight: ",context.execute_finding(game_room, value))
    Printer.print_empty_line()

    value = int(input("Enter the price of the toy you want to find: "))
    context.set_find_type(Price_find())
    Printer.print("Find by price: ",context.execute_finding(game_room, value))
    Printer.print_empty_line()


    for toy in list_of_toys:
        del toy


if __name__ == "__main__":
    main()
