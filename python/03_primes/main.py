# primefactorfinder.
def factors(num):
    numbers = [i+1 for i in range(num+1) if num % (i+1) == 0 and (i+1) != num and (i+1)!=1]
    if len(numbers) > 0:
        return(numbers)

print(factors(12))

def primefinder(num):
    prime_factors = []
    factors_list = factors(num)

    for i in factors_list:
        if factors(i) is None:
            prime_factors.append(i)
        else:
            factors(i)

    return(prime_factors)

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


print(factors(600851475143))
