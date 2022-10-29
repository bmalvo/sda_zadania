# task 1,3

class Cat:

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

# task 2


cats_list = []

cat1 = Cat('Ninja')
cat2 = Cat('Zara')
cat3 = Cat('Drapek')
cat4 = Cat('Brydzia')
cats_list.append(cat1)
cats_list.append(cat2)
cats_list.append(cat3)
cats_list.append(cat4)

for cat in cats_list:
    print(cat.make_sound(), end=', ')

print('\n')
print(cat1.eat_mouse())
print(cat1.eat_mouse())
print(cat1.eat_mouse())
print(cat3.eat_mouse())
