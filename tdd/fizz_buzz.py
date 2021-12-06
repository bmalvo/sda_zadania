def fizz_buzz(n: int):
    if is_multiple(n,3):
        if is_multiple(n, 5):
            return "FizzBuzz"
        return "Fizz"
    if is_multiple(n,5):
        return "Buzz"
    return str(n)

def is_multiple(value, mod):
    return(value % mod) == 0
