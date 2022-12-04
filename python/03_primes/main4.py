"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
YOU DONT HAVE TO CHECK THE COMPOSITE NUMBERS.
"""


def divisor(target, candidate=3):
    """supplies the divisors of target"""
    while True:
        if target % candidate == 0:
            yield candidate
        if candidate < target:
            candidate += 2
        if candidate >= target:
            return


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


def foo(num):
    results = []
    for i in divisor(num):
        print(i)
        if is_prime(i):
            results.append(i)
            print("appended", i)
        # else: #you dont need to check the composite numbers. 
            # print("checking", num/i,i)
            # results.append(foo(num / i))

    return(results)


print("results:", foo(600851475143))


# mygen = divisor(13195)
# for i in mygen:
    # print(i, is_prime(i))
