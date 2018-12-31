# Cheap solution. upload own binary converter soon.

def isPalindrome(n):
    return str(n) == str(n)[::-1]

for n in range(1000000):
    if isPalindrome(n) and isPalindrome(bin(n)[2::]):
        L.append(n)

print(sum(L))

# Output: 872187
