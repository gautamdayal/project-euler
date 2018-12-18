def fibonacci(n):
    n1, n2 = 0, 1
    
    for i in range(0, n):
        n1, n2 = n2, n1 + n2
        
    return n1

L = [fibonacci(i) for i in range(1, 35) if fibonacci(i) % 2 == 0]
print(sum(L))

# Output: 4613732
