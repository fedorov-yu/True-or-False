import csv
from src.TRUE.Gamestatus import GameStatus


class InvalidOperationError(Exception):
    pass


class TrueOrFalse:
    def __init__(self, filename, count_of_errors):
        self.game_status = GameStatus.IN_PROGRESS
        self.__filename = filename
        self.__count_of_errors = count_of_errors
        self.__count_questions = 0
        self.__my_err = 0
        self.__reader = []
        self.__number_of_question = 0

    def open_file(self):
        with open(self.__filename, encoding='utf-8') as file:
            for row in csv.reader(file, delimiter=";"):
                self.__reader.append(row)
                self.__count_questions += 1
        self.game_status = GameStatus.IN_PROGRESS

    def current_question(self):
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f'Game status {self.game_status} ')
        return self.__reader[self.__number_of_question][0]

    def next_question(self):
        self.__number_of_question += 1

    def let_answer(self, answer):
        if self.__number_of_question > self.__count_questions:
            raise InvalidOperationError(f'No more questions {self.__number_of_question}')
        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f'Game status {self.game_status} ')

        if answer == self.__reader[self.__number_of_question][1]:
            print(True)
        else:
            self.__my_err += 1
            print(False, self.__reader[self.__number_of_question][2])

        if (self.__number_of_question == self.__count_questions - 1) and (self.__count_of_errors >= self.__my_err):
            self.game_status = GameStatus.WIN
        elif self.__count_of_errors < self.__my_err:
            self.game_status = GameStatus.LOSE

    @property
    def status(self):
        return self.game_status
