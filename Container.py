import random
from Films.Cartoon import Cartoon
from Films.Documental import Documental
from Films.Gaming import Gaming


class Container:
    __size__: int
    __cont__: list

    def __init__(self, size: int):
        self.__size__ = size
        self.__cont__ = []

    def file_in(self, lines: list):
        ind = 0
        for i in range(0, self.__size__):
            line1 = list(lines[ind].split())
            ind += 1
            film_type = int(line1[0])
            name = line1[1]
            date = int(line1[2])

            line2 = lines[ind]
            ind += 1
            if film_type == 1:
                fi = Gaming(name, date)
                fi.read(line2)
                self.__cont__.append(fi)
            elif film_type == 2:
                fi = Cartoon(name, date)
                fi.read(int(line2))
                self.__cont__.append(fi)
            elif film_type == 3:
                fi = Documental(name, date)
                fi.read(int(line2))
                self.__cont__.append(fi)

    def random_in(self):
        for i in range(0, self.__size__):
            film_type = random.randint(1, 3)

            if film_type == 1:
                fi = Gaming('', 0)
                fi.random_read()
                self.__cont__.append(fi)
            elif film_type == 2:
                fi = Cartoon('', 0)
                fi.random_read()
                self.__cont__.append(fi)
            elif film_type == 3:
                fi = Documental('', 0)
                fi.random_read()
                self.__cont__.append(fi)

    def out(self):
        ans = 'Container contains ' + str(self.__size__) + ' elements.' + '\n\n'
        ind = 0
        for fi in self.__cont__:
            ans += str(ind) + ': '
            ans += fi.out()
            ind += 1
        ans += '\n\n'
        return ans

    def sorter(self):
        for i in range(1, self.__size__):
            j = i
            while j > 0 and (self.__cont__[j - 1].value() > self.__cont__[j].value()):
                self.__cont__[j - 1], self.__cont__[j] = self.__cont__[j], self.__cont__[j - 1]
                j -= 1
