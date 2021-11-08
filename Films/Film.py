# Базовый класс фильмов


class Film:
    _date_: int
    _name_: str

    def __init__(self,  name: str, date: int):
        self._name_ = name
        self._date_ = date

    def value(self):
        return float(self._date_) / float(len(self._name_))

