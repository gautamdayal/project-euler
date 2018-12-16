def factorial(n):
    if n < 0:
        raise ValueError(f'Value must be postive. You entered {n}') 
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
        
def isCurious(n):
    L = [int(i) for i in str(n)]
    return not (n == 1 or n == 2) and n == sum([factorial(i) for i in L])

print(sum([i for i in range(1, 100000) if isCurious(i)]))

# Output: 40730
