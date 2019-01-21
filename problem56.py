def digitSum(n):
  digits = [int(c) for c in str(n)]
   return sum(digits)
   
sums = []
for a in range(1, 101):
    for b in range(1, 101):
        sums.append(digitSum(a ** b))

print(max(sums))

# Output: 972
