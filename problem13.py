# use File I/O to extract numbers. 

inFile = open('bignumbers.txt', 'r')      # Change file name accordingly
inputs = inFile.readlines()
strList = [s.strip('\n') for s in inputs]
intList = [int(n) for n in strList]

print(str(sum(intList))[0:10])

# Output: 5537376230
