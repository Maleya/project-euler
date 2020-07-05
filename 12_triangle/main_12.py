import math


def triangle():
    n = 2
    tri = 1
    while True:
        yield tri
        tri += n
        n += 1


def total_divisors(n):
    factors = []
    i = 1
    while i <= int(math.sqrt(n)) + 1:
        if n % i == 0:

            if n / i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n // i)
        i += 1
    return len(factors)


gen = triangle()

while True:
    num = next(gen)
    # print(num)
    divisors = total_divisors(num)
    print(num, divisors)
    if divisors > 500:
        print("number found!", num)
        break
