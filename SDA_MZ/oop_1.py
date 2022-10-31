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


ferrari = Car()
print(ferrari.move())
fifi = Cat('fifi')
print(fifi)
print(fifi.move())
