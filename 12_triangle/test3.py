import math

n = 28
res = [1, 3, 5, 7, 9, 15, 21, 35, 45, 63, 105, 315]
# missing 15,21,63


def divisors(n):
    factors = []
    i = 1
    while i <= int(math.sqrt(n)) + 1:
        if n % i == 0:

            if n / i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n//i)
        i += 1
    factors.sort()
    return factors
output = divisors(n)
print(output)


def total_divisors(n):
    factors = []
    i = 1
    while i <= int(math.sqrt(n)) + 1:
        if n % i == 0:

            if n / i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n//i)
        i += 1
    return len(factors)
output = divisors(n)
print(output)

# assert res == output