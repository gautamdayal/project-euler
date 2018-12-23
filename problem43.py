from itertools import permutations
 
def splice(n):
    s = str(n)
    L = []
    d, u = 1, 4
    while u < 11:
        L.append(int(s[d:u]))
        d += 1
        u += 1
    return L
# cool num = number with properties specified in question.
def isCoolNum(n):
    L = splice(n)
    primes = [2, 3, 5, 7, 11, 13, 17]
    c = 0
    for i in range(len(L)):
        if L[i] % primes[i] == 0:
            c += 1
    if c == 7:
        return True
    else:
        return False

L = list(itertools.permutations('1234567890'))
pandigitals = [int(''.join(s)) for s in L]

print(sum([n for n in pandigitals if isCoolNum(n)]))

# Output: 16695334890
