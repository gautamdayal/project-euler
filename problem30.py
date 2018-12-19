def powerSum(n, p):
    digits = [int(c) for c in str(n)]
    return sum([i ** p for i in digits]) == n

print(sum([n for n in range(2, 1000000) if powerSum(n, 5)]))

# Output: 443839
