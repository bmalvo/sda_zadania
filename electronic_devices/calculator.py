import os


class NoBatteryError(ValueError):
    pass


class NoFileDefinedError(FileNotFoundError):
    pass


class Calculator:
    def __init__(self, battery: int = 100, memory=0, round_digit: int = 2, file=None):
        self.battery = battery
        self.memory = memory
        self.check_battery()
        self.round_digit = round_digit
        self.file = file

    def check_battery(self):
        if self.battery <= 0:
            raise NoBatteryError("Battery Low")

    def add(self, *args):
        self.check_battery()
        self.battery -= 1
        result = 0
        for n in args:
            result += n
        result = round(result, self.round_digit)
        self.memory = result
        return result

    def subtract(self, *args):
        self.check_battery()
        self.battery -= 1
        result = args[0]
        for n in args[1:]:
            result -= n
        result = round(result, self.round_digit)
        self.memory = result
        return result

    def multiply(self, *args):
        self.check_battery()
        self.battery -= 1
        result = args[0]
        for n in args[1:]:
            result *= n
        result = round(result, self.round_digit)
        self.memory = result
        return result

    def divide(self, *args):
        self.check_battery()
        self.battery -= 1
        result = args[0]
        for n in args[1:]:
            if n == 0:
                raise ValueError("Pamiętaj cholero nie dziel przez zero")
            result /= n
        result = round(result, self.round_digit)
        self.memory = result
        return result

    def to_nth_power(self, n, power):
        self.check_battery()
        self.battery -= 1
        result = n ** power

        result = round(result, self.round_digit)
        self.memory = result
        return result

    def is_even(self, n):
        self.check_battery()
        self.battery -= 1
        result = n % 2 == 0
        self.memory = result
        return result

    # [[1, 2], [2, 2, 2], [1, 1, 1, 5, 2]]
    def _get_data(self):
        if not self.file:
            raise NoFileDefinedError("Nie zdefiniowałeś pliku do oblicznia średniej")
        if os.path.isfile(self.file):
            with open(self.file) as f:
                lines = f.readlines()
            # for line in lines:
            #     lines_splited = line.split(",")
            lines_splited = [line.split(",") for line in lines]
            data = []
            for line in lines_splited:
                # for x in line:
                #     data.append(int(x))
                data.append([int(x) for x in line])
            return data
        return None

    def avg_from_file(self):
        self.check_battery()
        self.battery -= 1
        # data = self._get_data()
        # if data is None:
        #     raise FileNotFoundError("Podana ścieżka nie prowadzi do pliku!")
        if (data := self._get_data()) is None:
            raise FileNotFoundError("Podana ścieżka nie prowadzi do pliku!")
        result = [sum(x) / len(x) for x in data]
        result = [round(r, self.round_digit) for r in result]
        self.memory = result
        return result

