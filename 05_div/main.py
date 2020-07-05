
def is_div(number, div=20):
    counter = 0
    for i in range(1, div+1):
        if number % i == 0:
            counter += 1
    if counter >= div:
        return(True)
    return(False)




def checker(start, steps, div=20):
    while is_div(start, div) is False:
        start += steps
        print("false:", start)
    return(start)


print(checker(2520, 2520, 20))
