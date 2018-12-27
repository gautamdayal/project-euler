 def doesSatisfy(n):
    factors = [2, 3, 4, 5, 6]
    products = [set([c for c in str(n * i)]) for i in factors]
    a = products[0]
    for x in products:
        if x != a:
            return False
    return True

for n in range(100000, 1000000):
    if doesSatisfy(n):
        print(n)
        
# Output: 142857
