def collatz_chain(n):
    """returns chainlength of iterative sequence"""
    i = 1
    while n != 1:
        # print(n)
        if n % 2 == 0:
            n = n // 2
            i += 1
        else:
            n = 3 * n + 1
            i += 1

    return(i)

chains=[]
for n in range(1,int(1000000)):
    x = collatz_chain(n)
    # print(x)
    chains.append(x)

max_value = max(chains)
max_index = chains.index(max_value)

print("max:",max(chains),"index:",max_index)
# the answer is max_index+1 as it starts on 0
