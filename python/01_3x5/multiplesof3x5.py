def multsum35(max):
    # returns the sum of the multiples of 3 and 5 under n

    multiples = [i for i in range(max) if i % 3 == 0 or i % 5 == 0]
    return(sum(multiples))


print(multsum35(1000))
