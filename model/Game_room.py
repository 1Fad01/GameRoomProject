from model.toy import Toy


class GameRoom:
    #Название модуей без больших букв и нижних подчёркиваний
    #Методы с индексами
    #Вывод геймрума с фором
    #Переопределить стр
    def __init__(self, lst):
        self.set_list(lst)

    def get_list(self):
        return self.__lst

    def set_list(self, lst):
        if isinstance(lst, list):
            self.__lst = lst

    def add_to_list(self, toy):
        if isinstance(toy, Toy):
            self.__lst.append(toy)

    def sort(self):
        return self.__lst.sort()
