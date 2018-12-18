# incomplete code
from math2 import *

def truncate(n):
    L = []
    strL = list(str(n))
    while 1:
        if len(strL) == 1:
            L.append(strL)
            break
        else:
            L.append(strL)
            strL = strL[1::]
            
    strL = list(str(n))[::-1]
    while 1:
        if len(strL) == 1:
            L.append(strL)
            break
        else:
            L.append(strL[::-1])
            strL = strL[1::]
            
    return [int(''.join(l)) for l in L]

def isTruncable(n):
    hits = 0
    for i in truncate(n):
        if not isPrime(i):
            hits += 1
    if hits > 0:
        return False
    else:
        return True
