# Using itertools library. Write own function later.

from itertools import *
L1 = list(permutations('1234567890'))
L2 = [''.join(tuple) for tuple in L1]
L3 = L3 = sorted([int(s) for s in L2])

print(L3[999999])

# Output: 2783915460
