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


