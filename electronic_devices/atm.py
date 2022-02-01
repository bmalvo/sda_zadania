# -1. Są dwie klasy: Account i Card -done
# -2. Przy tworzeniu obiektu Account musimy podać takie parametry jak:
# -* numer konta - done
# -* imię - done
# -* nazwisko - done
# -* stan konta- domyślnie 0 - done
# -* wysokość debetu do którego możemy zejść- domyślnie 0 - done
#
# -3. Natomiast Card będzie miało takie własności jak:
# -* konto - do którego jest "podpięta" - done
# -* numer pin - done
#
# 4. Metody dla klasy Account:
# - odwołanie się do obiektu Account powinno zwracać numer konta
# - metoda Account.owner() powinna zwracać imię i nazwisko właściciela
# - metoda Account.balance() powinna zwracać aktualny stan konta
# - metoda Account.number() powinna zwracać numer konta
# - metoda Account.transfer() powinna zmieniać stan konta o podaną kwotę
# - dodajcie metodę która będzie sprawdzać czy transfer() jest możliwy- jeżeli transfer spowodowałby obniżenie
# stanu konta poniżej możliwego debetu to wywołajmy własny warunek "NoFundsError"
#
# 5. Metody dla klasy Card:
# - odwołanie się do obiektu card powinno zwracać imię i nazwisko właściciela konta
# - metoda Card.check_pin powinna sprawdzić czy pin jest poprawny
#
# 6. Napiszcie testy jednostkowe do powstałych klas i ich metod, Sprawdźcie pokrycie kodu testami
# za pomocą "pytest --cov". Doprowadźcie wynik do 100%
#
# 7. Uruchomcie narzędzie pylint i zastosujcie się do wskazówek przez niego zwróconych (Instalacja: pip install pylint,
#                                                                                                  użycie: pylint)
#
# 8. Utwórzcie plik main.py a w nim zaimplementujcie aplikację, która będzie przypominać zachowanie bankomatu w
# interakcji z użytkownikiem, wykorzystując napisane klasy.
# Załóżmy że w bankomacie możemy założyć konto, wpłacać i wypłacać środki.
#
# 9. Na podstawie zadania person-descriptor przygotujcie paczkę PyPi dla napisanej przez Was aplikacji-
# (Odpowiednio skonfigurujcie plik setup.py) Zbudujcie paczkę, zainstalujcie i spróbujcie ją uruchomić.


class Account:
<<<<<<< HEAD

    surname: object

    def __init__(self, account_number, name, surname, account_state=0, debt=0):
=======
    def __init__(self, account_number, name, surname, account_state = 0,debt =0):
>>>>>>> atm
        self.account_number = account_number
        self.name = name
        self.surname = surname
        self.account_state = account_state
        self.debt = debt

<<<<<<< HEAD
    def __str__(self):
        return f"{self.account_number}".format(self=self)
=======
>>>>>>> atm

    def owner(self):
        return self.name, self.surname

    def balance(self):
        return self.account_state

    def number(self):
        return self.account_number

    def transfer(self, operation):
        if (self.account_state + operation) >= 0:
            self.account_state += operation
            return self.account_state
        else:
            raise NoFundsError



class Card(Account):
<<<<<<< HEAD
    def __init__(self, account_number, pin, name, surname):
        super().__init__(account_number, name, surname)
        self.pin = pin

    def __str__(self):
        return f'{self.name} {self.surname}'.format(self=self)

    def check_pin(self):
        pin = self.pin
        check = int(input('Please, enter the PIN: '))
        if check != pin:
            print(pin)
            print('Wrong PIN')
        else:
            print('PIN accept')



s1 = Account(123321, "Bob", "Marley", 1000, 0)
c1 = Card(123321, 8520, 'Bob', 'Marley')

Account.owner(s1)
print(s1)
print(c1)
c1.check_pin()
=======
    def __init__(self,acc_number, pin):
        self.account_number = acc_number
        self.pin = pin

    def __str__(self):
        return Account.owner(Card)

class NoFundsError(Exception):
    def __init__(self):
        message = "Brak środków na koncie"
        super().__init__(message)


# s1 = Account(123321, "Bob", "Marley", 1000, 0)
# s1.transfer(300)
# s1.transfer(-200)
# s1.transfer(-1300)
# print(Account.balance(s1))
#
# print(Account.owner(s1))

c1 = Card(123321,456654)
print(c1)
>>>>>>> atm
