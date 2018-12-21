inFile = open('words.txt', 'r')

wordStr = inFile.readlines()[0]
wordStr = wordStr.replace(',', ' ')
wordStr = wordStr.replace("\"", '')
wordList = wordStr.split()

def charVal(c):
    return ord(c) - 64

def isTriangleWord(s):
    L = [triangleNumber(i) for i in range(1, 500)]
    return sum([getCharVal(c) for c in s]) in L

print(len([s for s in wordList if isTriangleWord(s)]))

# Output: 162
