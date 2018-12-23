# finish later. helper functions pasted below. 

def allsums(n):
    L = []
    a, b = n, 0
    while a != 0:
        L.append([a, b])
        a -= 1
        b += 1
    return purify(L)
    
def findPair(n):
    L = [pentaNum(n) for n in range(1, 500)]
    l = []
    for pair in allsums(n):
        a = pair[0]
        b = pair[1]
        if a in L and b in L:
            l.append(pair)
    return l

def findPair1(n):
    L = [pentaNum(n) for n in range(1, 500)]
    l = []
    for pair in allsums(n):
        a = pair[0]
        b = pair[1]
        diff = abs(a - b)
        if a in L and b in L and diff in L:
            l.append(pair)
    return l

def pentaNum(n):
    return n * (3 * n - 1) // 2
