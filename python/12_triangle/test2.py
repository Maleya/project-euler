import math
n = 315
#  1, 3, 5, 7, 9, 15, 21, 35, 45, 63, 105, 315.
# missing 15,21,63

def Factors(n):
    old_n = n
    fact = [1,n]

    while n % 2 == 0:
        fact.append(n)
        fact.append(n//2)
        n = n // 2
        fact.append(old_n//n)

    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
        print(f"i={i}")
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(f"n={n}")
            fact.append(n)
            fact.append(i)
            fact.append(n//i)
            fact.append(old_n//i)
            print(f"testing:{old_n}/{i}={old_n//i}")
            print(f"{n}/{i} = {n//i}")
            # fact.append(n/(n//i))
            n = n // i
            fact.append(old_n//n)
            # m+=1
            # fact.append(n*m)


              
    # Condition if n is a prime *
    # number greater than 2 
    if n > 2: 
        fact.append(n)
    # print(fact.sort())
    fact=list(set(fact))
    fact.sort()
    return fact
    # return set(fact)

print(Factors(n))