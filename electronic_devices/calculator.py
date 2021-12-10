from math import pow

class NoBatteryError(ValueError):
    pass

class DividedError(ValueError):
    pass


class Calculator:
    def __init__(self, battery: int = 100, memory=0):
        self.battery = battery
        self.memory = memory
        self.check_battery()

    def check_battery(self):
        if self.battery <= 0:
            raise NoBatteryError("Battery Low")

    def add(self, *args):
        self.check_battery()
        self.battery -= 1
        result = 0

        for n in args:
            result += n

        self.memory = result
        return result

    def subtract(self, *args):
        self.check_battery()
        self.battery -= 1
        result = args[0]

        for n in args[1:]:
            result -= n
        self.memory = result
        return result

    def multiply(self, *args):
        self.check_battery()
        self.battery -= 1
        result = args[0]

        for n in args[1:]:
            result *= n
        self.memory = result
        return result

    def divide(self, dividend, divisor):
        self.check_battery()
        self.battery -= 1
        if divisor == 0:
            raise DividedError("Pamiętaj cholero nie dziel przez zero!")
        else:
            result = dividend/divisor
        self.memory = result
        return result

    def square(self, n):
        self.check_battery()
        self.battery -= 1
        result = n*n
        self.memory = result
        return result

    def n_to_the_power_of(self,n, power):
        self.check_battery()
        self.battery -= 1
        result = pow(n,power)
        self.memory = result
        return result

    def is_even(self, number):
        self.check_battery()
        self.battery -= 1
        result = number%2 == 0
        return bool(result)

    def mean(self, file):
        self.check_battery()
        self.battery -=1
        self.file = open(file,"r")
        with self.file as f:
            list_main = []
            for line in f:
                lista = []
                for i in line:
                    if i.isdigit():
                        lista.append(int(i))
                        list_main.append(lista)






if __name__ == '__main__':
        calc = Calculator()
        print(f"stan baterii po utworzeniu obiektu: {calc.battery}")
        calc.battery = 1
        print(f"stan baterii po nadpisaniu wartości atrybutu battery {calc.battery}")
        result = calc.add(2, 2)
        print(f"Wynik dodawania: {result}")
        print(f"Stan baterii po wykonaniu działania: {calc.battery}")
        try:
            calc.add(2, 2)
        except NoBatteryError:
            print("Włóż baterię!")
            calc.battery = 100
        print(calc.add(2, 2))
        try:
            divide = calc.divide(3,0)
        except DividedError:
            print("Nie dziel cholero przez zero!")
        print(calc.is_even(4))
        calc.mean(input("plik: "))
