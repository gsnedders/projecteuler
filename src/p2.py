from itertools import takewhile

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-2) + fib(n-1)

def fib_iter():
    n = 0
    while True:
        yield fib(n)
        n += 1

def calc():
    values = takewhile(lambda x: x <= 4000000, fib_iter())
    return sum(x for x in values if (x % 2) == 0)

if __name__ == "__main__":
    print(calc())
