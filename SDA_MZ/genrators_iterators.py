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

