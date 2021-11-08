from Films.Film import Film
import random


class Cartoon(Film):
    __type__: int

    def __init__(self, name: str, date: int):
        super().__init__(name, date)
        self.__type__ = 0

    def read(self, line: str):
        self.__type__ = int(line)

    def random_read(self):
        self._name_ = ''
        num = random.randint(1, 28)
        for i in range(num):
            self._name_ += chr(ord('a') + random.randint(0, 25))
        self._date_ = random.randint(1980, 2021)
        self.__type__ = random.randint(1, 3)

    def out(self):
        ans = 'Film name: ' + self._name_ + ' , '
        ans += 'Date: ' + str(self._date_) + ' '
        ans += 'It is cartoon '
        if self.__type__ == 1:
            ans += 'Type of Cartoon: drawn' + '\n'
        elif self.__type__ == 2:
            ans += 'Type of Cartoon: dollhouse' + '\n'
        elif self.__type__ == 3:
            ans += 'Type of Cartoon: plastiline' + '\n'

        return ans
