from Films.Film import Film
import random


class Documental(Film):
    __length__: int

    def __init__(self, name: str, date: int):
        super().__init__(name, date)
        self.__length__ = 0

    def read(self, length: int):
        self.__length__ = length

    def random_read(self):
        self._name_ = ''
        num = random.randint(1, 28)
        for i in range(num):
            self._name_ += chr(ord('a') + random.randint(0, 25))
        self._date_ = random.randint(1980, 2021)
        self.__length__ = random.randint(60, 180)

    def out(self):
        ans = 'Film name: ' + self._name_ + ' , '
        ans += 'Date: ' + str(self._date_) + ' '
        ans += 'It is documental film '
        ans += 'Film length: ' + str(self.__length__) + '\n'
        return ans
