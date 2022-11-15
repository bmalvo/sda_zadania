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


# task 3, 4, 5, 6, 7, 9, 10


class Complex:

    def __init__(self, reality, imaginary=0):
        self.reality = reality
        self.imaginary = imaginary

    def __str__(self):
        sign = '+'
        if self.reality == 0:
            reality = ""
            sign = ''
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
        return f'{(cx_1.reality + cx_2.reality) + (cx_1.imaginary + cx_2.imaginary)}i'

    @staticmethod
    def add_three_complex(cx1, cx2, cx3):
        return f'{(cx1.reality + cx2.reality + cx3.reality) + (cx1.imaginary + cx2.imaginary + cx3.imaginary)}i'

    @staticmethod
    def add_multiple_complex(*cx):
        reality_all = sum([num.reality for num in cx])
        imaginary_all = sum([num.imaginary for num in cx])
        return f'{reality_all + imaginary_all}i'


numb1 = Complex(6, -4)
print(numb1)
numb2 = Complex(6, -4)
numb3 = Complex(0, 4)
print(numb1.__eq__(numb3))
print(numb1.__eq__(numb2))
print(Complex.add_complex(numb1, numb2))
print(Complex.add_three_complex(numb1, numb2, numb3))
print(Complex.add_multiple_complex(numb1, numb2, numb3))
