def isPalindrome(n):
    return str(n) == str(n)[::-1]

products = []
for i in range(100, 1000):
    for n in range(100, 1000):
        products.append(i*n)
palindromes = [i for i in products if isPalindrome(i)]
print(max(palindromes))

# Output: 906609
