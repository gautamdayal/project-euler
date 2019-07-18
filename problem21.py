# absolutely terrible brute-force implementation.
def divSum(a):
    return sum([i for i in range(1, a // 2 + 1) if a % i == 0])

def isAmicable(a, b):
    return divSum(a) == b and divSum(b) == a

"""
for a in range(1,10000):
    for b in range(1,10000):
        if isAmicable(a, b):
            print(a, b)
"""

# ABOVE CODE IS WAYY TOO SLOW
