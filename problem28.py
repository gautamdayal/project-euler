# Key to solving: top right number = square number ** 2

def diagonal(n):
    sums = [1]
    for i in range(1, n):
        diagonalSum = (4 * (2*i + 1) ** 2) - 12 * i
        sums.append(diagonalSum)
    return sum(sums)

print(diagonal(501))

# Output: 669171001
