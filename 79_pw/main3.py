import collections as col

file = 'p079_keylog.txt'
with open(file, 'r') as readfile:
    lines = readfile.readlines()
logins = [element.strip("\n") for element in lines]  # a list of successful logins


def setmaker(input_list):
    your_set = set()  # create a set of all occuring numbers in pws
    for num_seq in input_list:
        for numbers in num_seq:
            your_set.add(numbers)
    return(your_set)


def links(num_seq):
    length = len(num_seq)
    for i in range(length - 1):
        for j in range(i + 1, length):
            yield(num_seq[i], num_seq[j])


def make_number_graph(logins):
    graph = col.defaultdict(set)
    for num_seq in logins:
        for a, b in links(num_seq):
            graph[a].add(b)
    return graph


# def tree_trav(start, set, graph):  # no longer in use
#     queue = col.deque()
#     path = []
#     choices = graph[start]
#     print(choices)


def sorter(graph):
    unsorted_list = []
    for items in graph:
        unsorted_list.append(graph[items])
    sorted_list = sorted(unsorted_list, key=len, reverse=True)
    return(sorted_list)


superset = setmaker(logins)  # contains all the available numbers
graph = make_number_graph(logins)
combinations = sorter(graph)
answer = []
for i in range(1, len(combinations)):
    answer.append(combinations[i-1] - combinations[i])
    print(combinations[i-1] - combinations[i])
print(answer) #a final missing 0 needs adding, too lazy to code it. 

# what is happening here: links() is returning all the possible "next numbers"
# so 123 would mean that 1 can lead to 2 lead to 3, 2 can lead to 3

# next we make a dictionary with a key for each current number,
# where the values stored are a set of all possible "next vals"

# by picking a key and val you can traverse the tree,
# and we are looking for the shortest traverse that contains all the "superset" nums

# things this challenge will teach you:
#     * col.defaultdict (why we can have a set running inside of it? => google this)
#     * generators and yield (what you need to solve Eu_03)
#     * better list comprehension
