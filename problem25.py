def fibonacci(n):
    n1, n2 = 0, 1
    
    for i in range(0, n):
        n1, n2 = n2, n1 + n2
        
    return n1

while 1:
    if len(str(fibonacci(i))) == 1000:
        print(i)
        break
    i += 1

# Output: 4782
