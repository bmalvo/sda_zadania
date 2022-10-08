# task 1


def iterator_ex():
    cats = {
        'dąbrowskiego': ['Stefka', 'Brydzia'],
        'wierzbowa': 'Ninja',
        'zawoja': 'Drapek',
        'cygany': 'Zara'
    }

    for street, cat in cats.items():
        print(street)

    for street, cat in cats.items():
        print(cat)


# task 2


def numbers(n):
    lst_numb = []
    for i in range(n):
        lst_numb.append(i)
    return sum(lst_numb)

# task 3


class IteratorNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


itek = IteratorNumbers()
print(sum(itek))  # -> 55

# task 4


def reader(file, chunk=46):
    while True:
        data = file.read(chunk)
        if not data:
            break
        yield data


read_file = open('inwokacja.txt', encoding='utf-8')
print(next(reader(read_file)))
print(next(reader(read_file)))


# task 5


def line_reader():
    for line in open('inwokacja.txt', encoding='utf-8'):
        print(line, end='\n')

