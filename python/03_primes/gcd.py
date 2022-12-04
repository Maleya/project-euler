
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        return(a)


print(gcd(20, 7))



def fun(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
            n += 1
    return(n)


print(fun((12)))


# int gcd(int a, int b) {
#     int remainder;
#     while (b != 0) {
#         remainder = a % b;
#         a = b;
#         b = remainder;
#     }
#     return a;
