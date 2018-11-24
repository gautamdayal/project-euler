def isPrime(n):
    return not (n == 2 or any(n % i == 0 for i in range(2, (n // 2) + 1)))

L = [i for i in range(300000) if isPrime(i)]
print(L[10001])

# Output: 104743
