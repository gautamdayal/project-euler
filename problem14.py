def collatz(n):
    length = 0
    done = False
    while not done:
        if n == 1:
            done = True
        if n % 2 == 0:
            n /= 2
            length += 1
        elif n % 2 != 0:
            n = (3*n) + 1
            length += 1
    return length

