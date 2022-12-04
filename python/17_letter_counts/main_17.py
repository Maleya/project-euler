# data structs

# one, two, three, four, five, six, seven, eight, nine ten.
# ones
#  = {"1": 3, "2": 3, "3": 5, "4": 4, "5": 4, "6": 3, "7": 5, "8": 5, "9": 4}

up_to_19 = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
tens = {
    "0": "",
    "1": "",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

def num_to_let(n):
    """int n is written out in words and counted for characters.
    Max number is 1000
    Do not count spaces or hyphens. 
    For example, 342 (three hundred and forty-two) contains 23 letters and 
    115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage."""
    count = 0
    str_n = str(n)
    print(f"input:{str_n}")
    length = len(str_n)
    assert length >= 1 and length <= 4
    # print("length:", length)

    if length == 4:
        count += len("onethousand")

    if length == 3:
        count += (len(up_to_19[str_n[0]]) + len("hundred"))
        if str_n[1] or str_n[2] != 0: 
            length += -1

    if length == 2:
        tenth = int(len(tens[str_n[0]]))
        ones = int(len(up_to_19[str_n[1]]))
        count = tenth + ones
    elif length == 1:
        pass

    # print("count:",count)
    return count


assert num_to_let(42) == (len("forty-two") - 1)
print("foo")
print(num_to_let(300))
assert num_to_let(300) == len("threehundred")
# assert num_to_let(342) == 23
# assert num_to_let(115) == 20