from abc import ABC, abstractmethod

# task 1,3


# class Cat:
#
#     def __init__(self, name='unnamed_cat'):
#         self.name = name
#         self.meal = {
#             'mouse': 0
#         }
#
#     def __repr__(self):
#         return f'Cat - {self.name}'
#
#     def make_sound(self):
#         return f'{self.name}: Meooow!'
#
#     def eat_mouse(self):
#
#         self.meal['mouse'] += 1
#         mice = self.meal['mouse']
#         return f'{self.name} ate {mice} mice'

# task 2


# cats_list = []

# cat1 = Cat('Ninja')
# cat2 = Cat('Zara')
# cat3 = Cat('Drapek')
# cat4 = Cat('Brydzia')
# cats_list.append(cat1)
# cats_list.append(cat2)
# cats_list.append(cat3)
# cats_list.append(cat4)

# for cat in cats_list:
#     print(cat.make_sound(), end=', ')
#
# print('\n')
# print(cat1.eat_mouse())
# print(cat1.eat_mouse())
# print(cat1.eat_mouse())
# print(cat3.eat_mouse())

# task 4


class Dog:

    def __init__(self, name='unnamed_dog'):
        self.name = name

    def __repr__(self):
        return f'Dog - {self.name}'

    def make_sound(self):
        return f'{self.name}: Hau! Hau!'


dog1 = Dog('Sharkey')
dog2 = Dog('Biszkopt')
dog3 = Dog('Czekolada')
dog4 = Dog('Sindy')
# print(dog1)
# print(dog2)
# print(dog3)
# print(dog4)

# task 5


# animals = [cat1, cat2, cat3, cat4, dog1, dog2, dog3, dog4]

# for animal in animals:
#     print(animal.make_sound())

# task 6


class Movable(ABC):

    def move(self):
        pass


class Car(Movable):

    def move(self):
        return f'I drive'

# task 7


class Cat(Movable):

    def __init__(self, name='unnamed_cat'):
        self.name = name
        self.meal = {
            'mouse': 0
        }

    def __repr__(self):
        return f'Cat - {self.name}'

    def make_sound(self):
        return f'{self.name}: Meooow!'

    def eat_mouse(self):

        self.meal['mouse'] += 1
        mice = self.meal['mouse']
        return f'{self.name} ate {mice} mice'

    def move(self):
        return f'I sneak'


# ferrari = Car()
# print(ferrari.move())
# fifi = Cat('fifi')
# print(fifi)
# print(fifi.move())

# task 8, 9, 10


class Vet(ABC):

    @staticmethod
    def say_pet_hello(pet_name):
        if isinstance(pet_name, Cat):
            return f'Hello kittie {pet_name.name}!'
        if isinstance(pet_name, Dog):
            return f'Hello doggie {pet_name.name}!'
        return f'There is no such animal.'


fifi = Cat('Fifi')
pluto = Dog('Pluto')
# print(Vet.say_pet_hello(fifi))
# print(Vet.say_pet_hello(pluto))

# task 11, 12


class Figure(ABC):

    def get_area(self):
        return 'Not defined function'

    @classmethod
    def sum_area(cls, *figures):
        joint_areas = 0
        for figure in figures:
            joint_areas += figure.get_area()
        return round(joint_areas, 2)


class Triangle(Figure):

    def __init__(self, base_side, height):
        self.base_side = base_side
        self.height = height

    def get_area(self):
        return self.base_side * self.height / 2


class Circle(Figure):

    def __init__(self, ray):
        self.ray = ray
        self.pi = 3.14

    def get_area(self):
        return self.pi * self.ray * self.ray


class Rectangle(Figure):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width


triangle = Triangle(40, 18)
rectangle = Rectangle(40, 20)
circle = Circle(7)
print(triangle.get_area())
print(rectangle.get_area())
print(circle.get_area())
print(Figure.sum_area(triangle, rectangle, circle))
