n = 2**1000

stringified = str(n)
total=0
for char in stringified:
    total += int(char)
print(total)