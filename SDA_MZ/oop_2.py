import datetime

# task 1, 2


class Person:

    def __init__(self, name='Noname', surname="Anonim", birth_year=1900):
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
        print(current_year)
        if current_year < int(year):
            raise ValueError('Are you from future? So come back there!')
        else:
            self._birth_year = year

# task 3, 4


class Employee(Person):

    @Person.birth_year.setter
    def birth_year(self, value):
        if value < 1900 or value > 2020:
            self._birth_year = 0
        else:
            self._birth_year = value


# John = Employee()
# John.birth_year = 1900
# print(John.birth_year)
# assert John.birth_year == 1900
