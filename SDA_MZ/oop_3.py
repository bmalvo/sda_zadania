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

# task 3, 4, 5, 6, 7


class Complex:

    def __init__(self, reality, imaginary=0):
        self.reality = reality
        self.imaginary = imaginary

    def __str__(self):
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

    def __eq__(self, number):
        return self.reality == number.reality and self.imaginary == number.imaginary

    @staticmethod
    def add_complex(cx_1, cx_2):
        return f'{(cx_1.reality + cx_2.reality)+(cx_1.imaginary + cx_2.imaginary)}i'


numb1 = Complex(6, -4)
print(numb1)
numb2 = Complex(6, -4)
numb3 = Complex(0, 4)
print(numb1.__eq__(numb3))
print(numb1.__eq__(numb2))
print(Complex.add_complex(numb1, numb2))
