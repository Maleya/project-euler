value = 0
fiblist = [1, 2]
tol = 4000000
i = 0
while True:
    new_number = fiblist[i]+fiblist[i+1]
    if new_number > tol:
        break
    else:
        fiblist.append(fiblist[i]+fiblist[i+1])
        i += 1
ans = sum([i for i in fiblist if i % 2 == 0])
print(ans)
