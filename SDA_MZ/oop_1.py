# task 1

class Cat:

    def __init__(self, name='unnamed_cat'):
        self.name = name

    def __repr__(self):
        return f'Cat - {self.name}'

    def make_sound(self):
        return f'{self.name}: Meooow!'

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
