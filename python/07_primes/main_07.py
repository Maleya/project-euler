
def prime(n):
    not_primes = [False] * n        # Skapar en lista med boolean-värden som säger om ett tal [i] inte är ett primtal
    not_primes[1] = True            # Lägger till specialfall [1]

    for i in range (1,int(1+(n**0.5)),2):
        if not_primes[i] == False:   # Kollar om i är hittils definierat som ett primtal
            not_primes[i*i::2*i] = [True] * (1+int(((n-i*i)/(2*i))))    # Slicear ut varje 2i False ur not_primes och ersätter med True

    return ([2] + [i for i in range(3,n,2) if not_primes[i] == False])  # Returnerar varje "not_primes[i] == False", dvs varje primtal

# print(prime(n)[10001])
ans = prime(1000000)
print(ans[10000])
