def triangleNumber(n):
    return int(n / 2 * (n + 1))

sumsquare = triangleNumber(100) ** 2
L = [i ** 2 for i in range(101)]

print(sumsquare - sum(L))

# Output: 25164150
