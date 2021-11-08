from Films.Film import Film
import random


class Gaming(Film):
    __producer__: str

    def __init__(self,  name: str, date: int):
        super().__init__(name, date)
        self.__producer__ = ''

    def read(self, line: str):
        self.__producer__ = line.rstrip()

    def random_read(self):
        self._name_ = ''
        num = random.randint(1, 28)
        for i in range(num):
            self._name_ += chr(ord('a') + random.randint(0, 25))
        self._date_ = random.randint(1980, 2021)
        self.__producer__ = ''
        num = random.randint(1, 28)
        for i in range(num):
            self.__producer__ += chr(ord('a') + random.randint(0, 25))

    def out(self):
        ans = 'Film name: ' + self._name_ + ' , '
        ans += 'Date: ' + str(self._date_) + ' '
        ans += 'It is gaming film, '
        ans += 'Producer: ' + self.__producer__ + '\n'
        return ans
