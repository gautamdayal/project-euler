def factorial(n):
    if n < 0:
        raise ValueError(f'Value must be postive. You entered {n}') 
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

print(sum([int(c) for c in str(factorial(100))]))
