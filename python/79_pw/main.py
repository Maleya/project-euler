import collections

file = 'p079_keylog.txt'
with open(file, 'r') as readfile:
    lines = readfile.readlines()

newlist = [element.strip('\n') for element in lines]

n0 = set(element[0] for element in newlist)
n1 = set(element[1] for element in newlist)
n2 = set(element[2] for element in newlist)

# test = [(element.split()) for element in newlist]

# CHECK FOR REPETITIONS: NONE?
for i in range(len(newlist)):
    count = collections.Counter(newlist[i])
    for i in count:
        if (count[i]) > 1:
            print("Repettions found")

# print("first2",(n0 | n1))
# print("last",n2)
# print("unique numbers in spot2",bothsets-n2)

# print("unique in spot1",n1-n0)

# print("total unique elements:",len((n0 | n1| n2)))
# print("repetitions0-1",(n0 & n1))
# print("repetitions0-2",(n0 & n2))
