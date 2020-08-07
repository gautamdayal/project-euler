import math2

# Calculating a list of primes to use for each factorisation
pre_sieve = math2.sieve(20162//2 + 1)

non_sums = []

# Computing a list of abundant integers
abundants = [i for i in range(1,20162) if math2.isAbundant(i, pre_sieve)]
print(f'the abundants are {abundants}')


for n in range(1, 20162):
    addends = []
    for abundant in abundants:
        # Breaking the loop when n is lower than current abundant
        if n < abundant:
            print(f'{n} is less than {abundant}')
            break
        # Else, checking whether a sum is possible and breaking when a pair is found
        else:
            if n - abundant in abundants:
                addends.append(abundant)
                addends.append(n-abundant)
                print(f'n={n} addends:{addends}')
                break

    # Add n with empty addends to non_sums
    if addends == []:
        non_sums.append(n)

print(f'\n Non sums are: \n {non_sums}')

# Final Output
print(sum(non_sums))

 # Output: 4179871
