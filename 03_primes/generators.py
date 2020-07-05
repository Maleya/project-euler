# understanding generators

def counter(n):
    yield(n+1)
    yield(n+2)
# mygen = counter(4)


def is_even(n):
    if n % 2 == 0:
        return(True)
    else:
        return(False)


print(is_even(3))


def get_even(number):  # yield all the even numbers =< number
    n = 0
    while number > n:
        if is_even(n):
            yield n
        n += 1

# i think the idea is that you never really want reach the end of a generator.
# while true: then just keep calling next. 


print(len(mygen))
# for i in mygen:
    # print(i)


print(next(mygen))
print(next(mygen))
print(next(mygen))
