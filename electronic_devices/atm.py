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

    def transfer(self, deposit):
        if (self.account_state + deposit) >= 0:
            self.account_state += deposit
            return self.account_state
        else:
            return "You have no money!"



class Card(Account):
    def __init__(self, pin):
        self.pin = pin


s1 = Account(123321, "Bob", "Marley", 1000, 0)
s1.transfer(300)
s1.transfer(-200)
s1.transfer(-1300)
print(Account.balance(s1))