class Account:
    def __init__(self,account_number, name, surname, account_state=0, debt=0):
        self.account_number = account_number
        self.name = name
        self.surname = surname
        self.account_state = account_state
        self.debt = debt

    def __str__(self):
        return f"{self.account_number}".format(self=self)


    def owner(self):
         return self.name, self.surname


class Card(Account):
    def __init__(self, pin):
        self.pin = pin


s1 = Account(123321, "Bob", "Marley", 1000, 0)

Account.owner(s1)
print(str(s1))