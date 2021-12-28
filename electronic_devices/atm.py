class Account:
    def __init__(self, account_number, name, surname, account_state = 0,debt =0):
        self.account_number = account_number
        self.name = name
        self.surname = surname
        self.account_state = account_state
        self.debt = debt


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