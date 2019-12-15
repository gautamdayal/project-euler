# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math

def isPrime(n):
    if n == 1:
        return False
    else:
        return n==2 or not any(n%i==0 for i in range(2, (n//2)+1))

def goldbach(num, primelist):
    for prime in primelist:
        difference = num - prime
        by2 = difference / 2
        if str(math.sqrt(by2))[-1] == '0':
            return True
    return False

n = 33
primes = [i for i in range(1, 33) if isPrime(i)]
done = False
while not done:
    x = n
    n += 2
    if isPrime(n):
        primes.append(n)

    if not goldbach(n, primes):
        # output
        print(n)
        done = True

# Output: 5777
