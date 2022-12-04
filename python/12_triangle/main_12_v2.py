"""1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ..."""

def triangle():
    n = 2
    tri = 1
    while True:
        yield tri
        tri += n
        n += 1

def num_div(num):
    counter = 1
    for i in range(1, (num)//2 + 1):
        if num % i == 0:
            # print(f"{num} is divisible by {i}")
            counter += 1

    return counter

def prime(n):
    not_primes = [False] * n        # Skapar en lista med boolean-värden som säger om ett tal [i] inte är ett primtal
    not_primes[1] = True            # Lägger till specialfall [1]

    for i in range (1,int(1+(n**0.5)),2):
        if not_primes[i] == False:   
            not_primes[i*i::2*i] = [True] * (1+int(((n-i*i)/(2*i))))    

    return ([2] + [i for i in range(3,n,2) if not_primes[i] == False])

# -----
gen = triangle()
# 28: 1,2,4,7,14,28
num = 28
print(prime(num//2))
# while True:
#     num = next(gen)
    
#     # print(num)
#     divisors = num_div(num)
#     print(num,divisors)
#     if divisors>500: 
#         print("number found!",num)
#         break


# print(num_div(28))
# print(tri)
# print(f"total divisors: {num_div(tri)}")
n = 20 
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)