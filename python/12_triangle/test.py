import math
n = 100

def Factors(n): 
    factors = [1,n]

    if n % 2 == 0:
        factors.append(2)
        m = 0  #tracks multiplicity of 2
        while n % 2 == 0:
            n = n // 2
            factors.append(n)
            m+=1
            factors.append(2*m)
    print(f"n={n}")
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        if n % i== 0: 
            factors.append(i)
            m = 0
            while n % i== 0: 
                n = n // i
                factors.append(i)
                factors.append(n)
                m+=1
                factors.append(n*m)


              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(n)

    return set(factors)

print(Factors(n))