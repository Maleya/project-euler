def is_pal(word):
    """checks if the str is a palindrome"""
    word = str(word)
    l = len(word)-1
    for i in range(l):
        if word[0+i] != word[-1-i]:
            return(False)
    return(True)


def checker():
    ans=[]
    for i in range(999, 100, -1):
        for k in range(999, 100, -1):
            if is_pal(i*k):
                ans.append(i*k)
    return(ans)


print(max((checker())))