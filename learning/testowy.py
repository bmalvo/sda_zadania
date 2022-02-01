import pytest

# Zadanie: Zaimplementuj i przetestuj funkcje:
# is_palindrome(text: str) -> bool
# is_isogram(text: str) -> bool
# Testy powinny zawierać przynajmniej takie case'y:
#     1. pozytywny - podany tekst jest palindromem zwraca True
#     2. negatywny - podany tekst nie jest palindromem zwraca False
#     3. tekst nie posiada znaków "pusty" zwraca True
#     4. tekst posiada jeden znak
#     5. tekst posiada kilka znaków
#     6. tekst posiada wiele/dużo znaków
# Funkcje powinny być "not case senstive" przykład: o == O  Z == z (edited)
tekst = "Kobyła ma mały bok"


def palindrom():
    tekst_1 = tekst.replace(",","")
    tekst_1 = tekst.replace(" ","")
    tekst_1 = tekst_1.lower()
    tekst_2 = tekst.replace(",", "")
    tekst_2 = tekst.replace(" ", "")
    tekst_2 = tekst_2.lower()
    print(tekst_2)
    print(tekst_1 == tekst_2[::-1])

palindrom()

def test_is_palindrom(palindrom):
    assert palindrom("Kajak","kajak") == True




