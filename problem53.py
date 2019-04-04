def factorial(n):
  if n < 0:
    raise ValueError(f'Value must be postive. You entered {n}') 
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1) 
    
def combinations(n, r):
  return factorial(n) / (factorial(r)*(factorial(n-r)))
  
count = 0
for n in range(1, 101):
  for r in range(1, n):
    if combinations(n, r) > 1000000:
      count += 1

print(count)

# Output: 4075
