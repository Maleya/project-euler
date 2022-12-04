"""
problem 96
NOTES:
"""

import numpy as np

n_total = 50
full = set([i for i in range(1, 10)])

with open("data_clean.txt", "r") as f:
    alldata = f.readlines()
    alldata = [list(i.rstrip()) for i in alldata]
    alldata = [list(map(int, i)) for i in alldata]

doku_list = []
for n in range(n_total):
    doku_list.append(np.array(alldata[0 + n : 9 + n]))


def set_row(array, n):
    return set(array[n, :].flatten())


def set_col(array, n):
    return set(array[:, n].flatten())


def set_box(array, n):
    # row major order
    assert 0 <= n <= 8

    if n < 3:
        box_set = set(array[0:3, n * 3 : n * 3 + 3].flatten())

    elif 3 <= n < 6:
        box_set = set(array[3:6, (n - 3) * 3 : (n - 3) * 3 + 3].flatten())

    elif 6 <= n < 9:
        box_set = set(array[6:9, (n - 6) * 3 : (n - 6) * 3 + 3].flatten())

    return box_set


def coord_to_box(coord_tuple):
    """
    tells you what box you are in starting on (0,0)
    """
    row, col = coord_tuple
    assert row * col <= 64

    if 0 <= col <= 2:
        box = 0
    if 3 <= col <= 5:
        box = 1
    if 6 <= col <= 8:
        box = 2

    if 0 <= row <= 2:
        box += 0
    if 3 <= row <= 5:
        box += 3
    if 6 <= row <= 8:
        box += 6

    return box


def solver(array):
    """
    solves the (9,9) array one element (i,j) at a time 
    """
    
    full = set([i for i in range(1, 10)])
    _a, _b = np.where(array == 0)

    while len(_a) > 0:
        _a, _b = np.where(array == 0)
        counter = len(_a)
        print("remaining:", counter)
        for i, j in zip(_a, _b):
            row_legal = full - set_row(array, i)
            col_legal = full - set_col(array, j)
            box_n = coord_to_box((i, j))
            box_legal = full - set_box(array, box_n)
            final = row_legal & col_legal & box_legal
            if len(final) == 1:
                array[i, j] = list(final)[0]
                # print(f"({i},{j}) has {len(final)} options")
                # print(list(final)[0])
            _a, _b = np.where(array == 0)
            counter_new = len(_a)
        if counter == counter_new and counter != 0: 
            print("failed")
            return array
    print("success")
    return array


s0 = doku_list[0]

for elem in doku_list:
    solver(elem)

# solver(doku_list[0])
# print(s0) 
# solver(s0)
# print(doku_list[0])

"""
algo: 
1. start with a high rank item
2. establish what cannot be inside its missing squares 
3. if we can deduce a number fill it in and repeat. 

(0,0) means we check 
row0 
col0 
box0 

(1,3) means we check 
row1
col3
box1

we need a (1,3) => box number mapping 
"""
