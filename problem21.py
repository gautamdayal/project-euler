
def divisors(n):
    divisors_list = []
    if n % 2 == 0:
        for i in range(1, (n//2) + 3):
            if n % i == 0:
                divisors_list.append(i)
    else:
        for i in range(1, (n//2) + 3, 2):
            if n % i == 0:
                divisors_list.append(i)
    return divisors_list

def d(n):
    return sum(divisors(n))

def isAmicable(n):
    a = n
    b = d(a)
    if a != b:
        if d(b) == a:
            return True
        else:
            return False

amicables = []
for i in range(1, 10001):
    if isAmicable(i):
        amicables.append(i)

print(sum(amicables))

# Output: 31626
