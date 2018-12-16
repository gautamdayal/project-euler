# Returns a list with all duplicates removed
def purify(L):
    outL = []
    for item in L:
        if item not in outL:
            outL.append(item)
    return outL

L = []
for a in range(2, 101):
    for b in range(2, 101):
        L.append(a ** b)

print(len(purify(L)))

# Output: 9183
