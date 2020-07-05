# prime factorization

# def divisors(num):
#     skip = [1, 2]
#     for i in range(num):
#         for k in skip:
#             if i % k:
#                 skip.append(i)
#         if i not in skip and num % i ==0:

#             skip.append(i)
#             yield i


def divisors_old(num):
    for i in range(3, num):
        if num % i == 0:
            yield i


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int((number)**0.5 + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve(num):
    # She *is* working on Project Euler #10, I knew it!
    primes = [1, 2]
    for next_prime in get_primes(3):
        if next_prime < num:
            primes.append(next_prime)
            print(next_prime)
        else:
            # print(primes)
            return(primes)


def divisor(target, candidate=2):
    """supplies the divisors of target"""
    while True:
        if target % candidate == 0:
            yield candidate
        candidate += 1




# print(i for i in divisors_old(24))
# print(solve(600851475143))
# print(is_prime(is_prime(137)))
mygen = divisor(48)
for i in mygen:
    print(i, is_prime(i))
