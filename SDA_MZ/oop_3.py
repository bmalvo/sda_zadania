# task 1

week_days = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}

# task 3


class Complex:

    def __init__(self, reality, imaginary=0):
        self.reality = reality
        self.imaginary = imaginary

    def show(self):
        sign = '+'
        if self.reality == 0:
            reality = ""
        else:
            reality = self.reality
        if self.imaginary == 1:
            imaginary = 'i'
        elif self.imaginary == 0:
            sign = ''
            imaginary = ''
        elif self.imaginary < 0:
            sign = '-'
            imaginary = f'{abs(self.imaginary)}i'
        else:
            imaginary = f'{self.imaginary}i'
        result = f'{reality} {sign} {imaginary}'
        return result


numb = Complex(6, -4)
print(numb.show())
