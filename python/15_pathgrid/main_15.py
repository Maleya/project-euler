from itertools import * 

# # a = list(combinations_with_replacement("DDRR",4))
# side = 2
# movesset = "D"*side+"R"*side
# # print(movesset)
# a = list(permutations(movesset,side*2))

# print(a)
# a = set(a)
# a = list(a)
# print(len(a))


"""
the final answer is actually 40!/(20!*20!)
from combinations with repition

(n pick k) = n! /(k!(n-k)!)

=> see argument about only picking the Rs in pdf

Easier to think about is that you have all the permutations 

P(40) = 40! 

But the number of repitions are not interesting so we remove those. 
how many ways can we arrange the D's?  => 20! ways
similarly the R's? => 20! ways

since they are indistinguishable. 

"""