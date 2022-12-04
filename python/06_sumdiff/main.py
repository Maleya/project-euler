def sum_square(n):
    total = 0
    """The sum of the squares of the n ten natural numbers """
    for i in range(n+1):
        total += i**2
    return(total)


def square_sum(n):
    """The square of the sum of the first n natural numbers is"""
    # for i in range(n)+1:
    total = sum([i for i in (range(n+1))])
    return(total ** 2)


print("answer:",square_sum(100)-sum_square(100))
