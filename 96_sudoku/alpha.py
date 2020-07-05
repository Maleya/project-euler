"""
problem 96
NOTES:
data contains a list of lists
"""

digit_set = set([i for i in range(10)])

with open('data.txt','r') as f:
    alldata = f.readlines()
    alldata = [list(i.rstrip()) for i in alldata]
    data = alldata[1:10] #  select the first grid-

def col(inputlist, col_nr):
    # will return a list of the col_nr:th column. 
    assert col_nr >= 0 and col_nr <= 9
    output = [i[col_nr] for i in inputlist[0:9]]
    return output

def row(inputlist,row_nr):
    # returns a row in list form. 
    assert row_nr >= 0 and row_nr <= 9
    return list(inputlist[row_nr])

def block(inputlist,x_coord, y_coord):
    # returns block in listform
    assert x_coord <= 2 and y_coord <= 2
    assert x_coord >= 0 and y_coord >= 0

    x_start = x_coord*3
    y_start = y_coord*3
    output = []
    for i in range(y_start,y_start+3):
        output += inputlist[i][x_start:x_start+3]

    return output

test = set(row(data,0)) | set(col(data,0)) | set(block(data,0,0))

print(test-digit_set)
# UNIT TESTS:
# print(type(data))
# print(len(data))
# print(data)

# print(col(data,0))
# print(row(data,0))
# print(block(data,0,0))
# print(digit_set)
