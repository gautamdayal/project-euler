# terribly inefficient but works

for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a, b, c)
                break

# Output: 200 375 425
# Therefore product = 31875000
