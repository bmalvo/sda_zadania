import datetime

# task 1, 2


class Person:

    def __init__(self, name, surname, birth_year):
        self._name = name
        self._surname = surname
        self._birth_year = birth_year

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, year):
        current_year = datetime.datetime.now().year
        if current_year < year:
            raise ValueError('Are you from future? So come back there!')
        else:
            self._birth_year = year

# task 3


class Employee(Person):
    pass
