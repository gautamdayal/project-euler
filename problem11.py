
# setup

fin = open('pep11.txt', 'r')
input = fin.readlines()
rows = []

for row in input:
    rows.append([int(c) for c in row.split()])

def product(L):
    i = 1
    for n in L:
        i *= n
    return i
products = []

# diagonal

for y in range(17):
    for x in range(17):
        diagonal = []
        for i in range(4):
            diagonal.append(rows[y+i][x+i])
        products.append(product(diagonal))
for y in range(17):
    for x in range(3, 20):
        diagonal = []
        for i in range(4):
            diagonal.append(rows[y+i][x-i])
        products.append(product(diagonal))

# vertical

for y in range(17):
    for x in range(20):
        vertical = []
        for i in range(4):
            vertical.append(rows[y+i][x])
        products.append(product(vertical))

# horizontal

for y in range(20):
    for x in range(17):
        horizontal = []
        for i in range(4):
            horizontal.append(rows[y][x+i])
        products.append(product(horizontal))

print(max(products))

# Output: 70600674
